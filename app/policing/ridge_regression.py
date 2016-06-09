import pandas as pd
import pickle
pickle_directory = "/Users/along528/insight/models/pickle/"
model = pickle.load(open(pickle_directory+"dumb_ridge_regression.p","rb"))
scaler = pickle.load(open(pickle_directory+"scaler.p","rb"))

import munging


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
	return output




