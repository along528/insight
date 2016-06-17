import pickle
features = pickle.load(open('best_features_names.p','rb'))
print features
for feature in features: print feature


