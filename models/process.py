import pandas as pd
import numpy as np
import modeling

use_sql = True
try:
    from sqlalchemy import create_engine
    from sqlalchemy_utils import database_exists, create_database
    import psycopg2
    dbname = 'combined_profiling'
    username = 'along528'
    pswd = 'password'
    con = psycopg2.connect(database = dbname, user = username, host='localhost', password=pswd)
    engine = create_engine('postgresql://%s:%s@localhost/%s'%(username,pswd,dbname))
except ImportError:
    use_sql = False

traffic_features = [ 'stops_total', 'searches_total', 'hits_total', 'stops_white', 'searches_white',
     'hits_white', 'stops_black', 'searches_black', 'hits_black']
per_capita_features = ['urban','rural', 
                     'institutionalized_all', 'institutionalized_adult_all',
                     'institutionalized_adult_federal_detention_all',
                     'institutionalized_adult_federal_prison_all',
                     'institutionalized_adult_state_prison_all',
                     'institutionalized_adult_local_jail_all',
                     'institutionalized_juvenile_all',
                     'institutionalized_white', 'institutionalized_adult_white',
                     'institutionalized_adult_federal_detention_white',
                     'institutionalized_adult_federal_prison_white',
                     'institutionalized_adult_state_prison_white',
                     'institutionalized_adult_local_jail_white',
                     'institutionalized_juvenile_white', 
		     'institutionalized_black',
                     'institutionalized_adult_black', 
		     'institutionalized_adult_federal_detention_black',
                     'institutionalized_adult_federal_prison_black',
                     'institutionalized_adult_state_prison_black',
                     'institutionalized_adult_local_jail_black', 
                     'institutionalized_juvenile_black',
                     'population_white', 'population_black', 
		     'total_income_estimate_all',
                     'total_income_estimate_white', 'total_income_estimate_black', 
		     'swnauthemp', 'swnftemp', 'swnptemp', 'civftemp', 
		     'civptemp', 'totftemp', 'totptemp', 'ftreserveswn', 
		     'ptreserveswn', 'ftreserveciv', 'ptreserveciv', 'ftgangoff',
                     'ptgangoff', 'ftdrugoff', 'ptdrugoff', 'ftterroff', 'pterroff', 
		     'fthumtrfoff', 'pthumtrfoff', 'numrespoff', 'numcpo', 
		     'numsro', 'numpatr', 'numinvst', 'numjail',
                     'numcrtsec', 'numprocserv', 'opbudget','drugforf', 
		     'totfield', 'totinsrv', 
		     'chiefmin', 
		     'chiefmax', 'sgtmin', 'sgtmax', 'entrymin', 'entrymax', 
		     'nummrkcars', 'numothmrk', 'numumkcars',
                     'numothunm', 'numplanes', 'numcopters', 'numboats', 
		     'nummotor', 'numcarcam',
                     'numfixcam', 'nummobcam']
		     #'violent_crime_total', 'murder_and_nonnegligent_manslaughter', 'forcible_rape', 'robbery', 'aggravated_assault', 'property_crime_total', 'burglary', 'larceny_theft', 'motor_vehicle_theft']

officer_demographic_features = ['white', 'black', 'hispanic', 'asian', 'nathaw', 'amerind', 'multrace', 'unkrace'] #, 'male','female']

other_features = ['total','totacad']
training_features = per_capita_features+other_features+officer_demographic_features
    

def get_data(munge=True,with_traffic=True,drop_features=True,db_name='traffic_joined_with_features'):
    if not with_traffic:
        db_name = 'all_pd_joined_features'
    sql_query = "SELECT  * FROM %s;" % (db_name)

    data = None
    if use_sql:
        data = pd.read_sql_query(sql_query,con).drop('index',axis=1)
    else:
	data = pd.read_csv(db_name+'.csv')

    data = data.set_index('surveyid',drop=True)
    if not munge: 
        return data

    
    
    if drop_features:
        features = list(training_features)
        if with_traffic:
            features+=traffic_features
        data = data[features]
    
    data = data.replace(' ',0)
    data = data.replace([np.inf, -np.inf], np.nan)
    data = data.dropna()
    data = data.apply(lambda x: pd.to_numeric(x,errors='ignore'))
   

    #replace default max values
    default_max = 999999
    for column in data.columns.tolist():
        if default_max  in data[column].values:
            mean = data[data[column]!=default_max][column].mean()
	    data.ix[data[column]==default_max,column] = mean


    return data
                      
def split_data(data,frac=0.2):
    test = data.sample(frac=frac,random_state=20)
    val = data[data.index.isin(test.index.values.tolist())==False]
    return test,val



def add_features(data_tmp):
    data = pd.DataFrame(data_tmp)
    
    do_rpsi = False
    rpsi = None
    if 'searches_black' in data.columns.tolist():
        #create rpsi label
        num = data['searches_black'] * data['stops_white'] 
        denom = data['stops_black'] * data['searches_white']
        rpsi = num.div(denom)
	data = data[data['searches_total']>=100]
	data = data[data['stops_black']>=100]
        #drop remaining traffic features
        data = data.drop(['stops_total', 'searches_total', 'hits_total', 
			  'stops_white', 'searches_white',
                          'hits_white', 'stops_black', 'searches_black', 
			  'hits_black'],axis=1)
	do_rpsi = True
    #create per_capita features from census population
    data[training_features] = data[training_features].apply(lambda x: pd.to_numeric(x))
    #calculate per capita features
    per_capita_data = data[per_capita_features]
    population = data['total']
    per_capita_data = per_capita_data.div(population,axis=0)
    per_capita_data.rename(columns=lambda x: x+'_per_capita',inplace=True)
    data = pd.concat([data,per_capita_data],axis=1)

    #calculate officer demographic features per total officers
    #and compute diversity index as
    #1 - prob(same_race)
    #where prob(same_race) is the probability
    #to randomly select to officers of the same race from the department
    officer_demographics= data[officer_demographic_features]
    def correct(x):
    	if x < 0: return 0.
    	return x
    total_officers = officer_demographics.sum(axis=1)
    officer_demographics_norm = officer_demographics.div(total_officers,axis=0)
    officer_demographics_minus_one = officer_demographics - 1
    for col in officer_demographics_minus_one.columns.tolist():
        officer_demographics_minus_one[col] = \
		officer_demographics_minus_one[col].map(correct)
    total_officers_minus_one = total_officers - 1
    officer_demographics_minus_one_norm = \
    	officer_demographics_minus_one.div(total_officers_minus_one,axis=0)
    probabilities = officer_demographics_minus_one_norm*officer_demographics_norm
    diversity_index = 1 - probabilities.sum(axis=1)
    diversity_index
    data['diversity_index'] = diversity_index

    officer_demographics_norm.rename(columns=lambda x: x+'_per_totofficers',
   				    inplace=True)

    data = pd.concat([data,officer_demographics_norm],axis=1)
    
    if do_rpsi:
        data['rpsi'] = rpsi
	#data = data[data['rpsi'] < 10]
    data = data[data['total']>10000]

    #build comparison features
    data['black_over_white_population_disparity'] =\
    	data['population_black'].div(data['population_white'],axis=0).fillna(1)
    data['black_over_white_income_disparity'] =\
    	data['total_income_estimate_black'].div(data['total_income_estimate_white'],axis=0).fillna(1)
    data['black_over_white_population_disparity'] =\
    	data['population_black'].div(data['population_white'],axis=0).fillna(1)
    data['black_over_white_institutionalized_disparity'] =\
    	data['institutionalized_black'].div(data['institutionalized_white'],axis=0).fillna(1)
    data['black_over_white_institutionalized_adult_disparity'] =\
    	data['institutionalized_adult_black'].div(data['institutionalized_adult_white'],axis=0).fillna(1)
    data['black_over_white_institutionalized_adult_federal_detention_disparity'] =\
    	data['institutionalized_adult_federal_detention_black'].div(\
	data['institutionalized_adult_federal_detention_white'],axis=0).fillna(1)
    data['black_over_white_institutionalized_adult_federal_prison_disparity'] =\
    	data['institutionalized_adult_federal_prison_black'].div(\
	data['institutionalized_adult_federal_prison_white'],axis=0).fillna(1)
    data['black_over_white_institutionalized_adult_state_prison_disparity'] = \
    	data['institutionalized_adult_state_prison_black'].div(\
	data['institutionalized_adult_state_prison_white'],axis=0).fillna(1)
    data['black_over_white_institutionalized_adult_local_jail_disparity'] =\
    	data['institutionalized_adult_local_jail_black'].div(\
	data['institutionalized_adult_local_jail_white'],axis=0).fillna(1)
    data['black_over_white_institutionalized_juvenile_disparity'] =\
    	data['institutionalized_juvenile_black'].div(\
	data['institutionalized_juvenile_white'],axis=0).fillna(1)
    #compare deomgraphics in police department and in population
    for race in ['black','white']:
        num = data[race].div(data['swnftemp'],axis=0)
        denom = data['population_'+race].div(data['total'],axis=0)
        data[race+'_officer_disparity'] = num.div(denom)
    data['black_over_white_officer_disparity'] =\
    	data['black_officer_disparity'].div(data['white_officer_disparity'])
    data = data.replace([np.inf, -np.inf], np.nan)
    data = data.dropna()
    return data


def get_split_add_data(munge=True,with_traffic=True,db_name='traffic_joined_with_features',frac=.2):
    test,val = split_data(get_data(munge=munge,with_traffic=with_traffic,db_name=db_name),frac=frac)
    return add_features(test),add_features(val)


class Processor:
    def __init__(self,df,categorize=True,label='rpsi'):
    	#input the validation data (not the test data)
        self.df = df
	self.categorize = categorize
	self.label = label

	
	X_unscaled = None
	if self.label in self.df.columns.tolist():
	    X_unscaled = np.array(self.df.drop(self.label,1))
	else:
	    X_unscaled = np.array(self.df)
	self.mean = np.mean(X_unscaled, axis=0)
	self.std = np.std(X_unscaled, axis=0)
    def get_scaled_Xy(self,unscaled_df):
        X_unscaled = None
	has_label = True
        if 'rpsi' in unscaled_df.columns.tolist():
	    X_unscaled = np.array(unscaled_df.drop(self.label,1))
	else:
	    X_unscaled = np.array(unscaled_df)
	    has_label = False
        X = (X_unscaled - self.mean)/self.std
	#X = X[np.isfinite(X)]

	y = None
	if has_label:
	    if self.categorize:
	        y = np.array(unscaled_df[self.label].map(modeling.categorize))
	    else:
	        y = np.array(unscaled_df[self.label])
	y = y
	return X,y
        
        
