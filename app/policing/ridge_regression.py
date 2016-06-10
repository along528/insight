import pandas as pd
import pickle
pickle_directory = "/Users/along528/insight/models/pickle/"
model = pickle.load(open(pickle_directory+"dumb_ridge_regression.p","rb"))
scaler = pickle.load(open(pickle_directory+"scaler.p","rb"))

import munging

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2

dbname = 'traffic_police_combined'
username = 'along528'
pswd = 'password'
## 'engine' is a connection to a database
## Here, we're using postgres, but sqlalchemy can connect to other things too.
engine = create_engine('postgresql://%s:%s@localhost/%s'%(username,pswd,dbname))
print engine.url



def prediction(features):
	#will this remove some police departemtns
	#even though it might look like they should be there?
	features = munging.process_df(features)
	metadata = features[['agency','city','state','zipcode']]
	features = munging.drop(features)
	X = scaler.scale(features)
	y = model.predict(X)
	features['RPSI'] = y
	output = pd.concat([metadata,features],axis=1)
	#output.to_sql('prediction',engine,if_exists='replace')
	return output




