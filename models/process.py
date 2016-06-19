import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2

dbname = 'combined_profiling'
username = 'along528'
pswd = 'password'
con = None
con = psycopg2.connect(database = dbname, user = username, host='localhost', password=pswd)


dbname = 'combined_profiling'
username = 'along528'
pswd = 'password'
## 'engine' is a connection to a database
## Here, we're using postgres, but sqlalchemy can connect to other things too.
engine = create_engine('postgresql://%s:%s@localhost/%s'%(username,pswd,dbname))
print engine.url


def get_data(munge=True,with_traffic=True):
    db_name = 'traffic_joined_with_features'
    if not with_traffic:
        db_name = 'all_pd_joined_features'
    sql_query = "SELECT  * FROM %s;" % (db_name)

    #data = munging.process_df(pd.read_sql_query(sql_query,con))
    data = pd.read_sql_query(sql_query,con).drop('index',axis=1)
    data = data.set_index('surveyid',drop=True)
    if not munge: 
        return data
    traffic_features = [ 'stops_total', 'searches_total', 'hits_total', 'stops_white', 'searches_white',
     'hits_white', 'stops_black', 'searches_black', 'hits_black']
    other_features = ['total',
                    'urban','rural', 
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
		     'totacad', 'totfield', 'totinsrv', 'white', 'black', 
		     'hispanic', 'asian', 'nathaw', 'amerind', 'multrace',
                     'unkrace', 'male', 'female', 'totgender', 'chiefmin', 
		     'chiefmax', 'sgtmin', 'sgtmax', 'entrymin', 'entrymax', 
		     'nummrkcars', 'numothmrk', 'numumkcars',
                     'numothunm', 'numplanes', 'numcopters', 'numboats', 
		     'nummotor', 'numcarcam',
                     'numfixcam', 'nummobcam', 'population']
    features = list(other_features)
    if with_traffic:
        features+=traffic_features
    data = data[features]
    data = data.replace(' ',0)
    data = data.replace([np.inf, -np.inf], np.nan)
    data = data.dropna()
    data = data.apply(lambda x: pd.to_numeric(x))
    return data
                      
def split_data(data):
    test = data.sample(frac=0.2,random_state=20)
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
        #drop remaining traffic features
        data = data.drop(['stops_total', 'searches_total', 'hits_total', 
			  'stops_white', 'searches_white',
                          'hits_white', 'stops_black', 'searches_black', 
			  'hits_black'],axis=1)
	do_rpsi = True
    #create per_capita features from census population
    population = data['total']
    per_capita = data.drop('total',axis=1)
    per_capita = per_capita.div(population,axis=0)
    per_capita.rename(columns=lambda x: x+'_per_capita',inplace=True)
    data = pd.concat([data,per_capita],axis=1)
    data['total'] = population
    
    if do_rpsi:
        data['rpsi'] = rpsi
        data = data[data['rpsi']<10]
    #data = data[data['total']>10000]

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


def categorize(rpsi):
    if rpsi >=0 and rpsi <=1.3:
        return 0
    elif rpsi > 1.3 and rpsi < 2.5:
        return 1
    else: return 2