import pandas as pd
import numpy as np

def process_df(df):
    #just look at one year for now
    df = df.convert_objects(convert_numeric=True)
    #normalize by number of officers in department
    for column in ['ftgangoff','ftdrugoff','ftterroff','numcpo',
               'white','black','hispanic','asian','nathaw',
               'amerind','multrace','unkrace','male','female']:
        df[column] = df[column].div(df['swnftemp'],axis='index')
    df = df.reset_index().drop('level_0',1)
    df = df[df['zipcode']!=27611] #remove nc state highway patrol
    df['black_over_white'] = df['black'].div(df['white'],axis='index')
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna()
    return df

def drop(df):
    return df.drop(['city','index','state','zipcode','agency','hispanic',
                 'asian','nathaw','amerind','multrace','unkrace',
                 'male','female','lessthanplcy','drivhis'],1)




from sklearn.preprocessing import OneHotEncoder
class Scaler:
    def __init__(self,df,label=False):
        self.num_categories = ['black_over_white','swnftemp','ftdrugoff','ftterroff',
                               'numcpo','white','black','population']
        num_categories = list(self.num_categories)
        if label: num_categories.append('rpsi')
        X_int = np.array(df.drop(num_categories,1))
        X_num = None
        if label:
            X_num = np.array(df[num_categories].drop('rpsi',1))
        else:
            X_num = np.array(df[num_categories])

        self.enc = OneHotEncoder(sparse=False) #otherwise hard to combined
        self.enc.fit(X_int)
        self.mean = np.mean(X_num, axis=0)
        self.std = np.std(X_num, axis=0)
    def scale(self,df,label=False):
        num_categories = list(self.num_categories)
        if label: num_categories.append('rpsi')
        X_int = np.array(df.drop(num_categories,1))
        self.X_int = self.enc.transform(X_int)
        X_num = None
        if label:
            X_num = np.array(df[num_categories].drop('rpsi',1))
        else:
            X_num = np.array(df[num_categories])
        self.X_num_scaled = (X_num-self.mean)/self.std
        X = np.concatenate([self.X_num_scaled,self.X_int],axis=1)
        y = None
        if label:
            y = np.array(df['rpsi'])
            return X,y
        return X
