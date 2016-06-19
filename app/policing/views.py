from flask import render_template
from policing import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from flask import request
import ridge_regression
from os import sys
from collections import OrderedDict

user = 'along528' #add your username here (same as previous postgreSQL)                      
host = 'localhost'
dbname = 'combined_profiling'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)

def clean_df(results):
    results['agency'] = results['agency'].str.title()
    results['agency'] = results['agency'].str.replace("'S","'s")
    results['agency'] = results['agency'].str.replace("ffs","ff's")
    results.columns = results.columns.str.title()
    columns = results.columns.tolist()
    columns[columns.index("Rpsi")] = "RPSI"
    results.columns = columns
    return results
def get_html(results):
    #return results.to_html(index=False, float_format = lambda x: "%3.2f" % (x)).replace("dataframe", "table table-hover")
    return results.to_html(index=False).replace("dataframe",
					       "table table-hover")



 
@app.route('/')
@app.route('/index')
@app.route('/input')
def input():
    return render_template("input.html")


@app.route('/output')
def output():
  agency = request.args.get('agency')
  query = "SELECT * \
  	   FROM app_db \
	   WHERE (agency LIKE '%"+agency.title()+"%');" 
  results=pd.read_sql_query(query,con)
  results = results.sort(columns=['population'],ascending=False).reset_index()
  results = results[results.index==0]
  features = results.drop(['index','surveyid','agency','city','state','zipcode'],axis=1)

  results_series = results.ix[0,:]
  #results = ridge_regression.prediction(features)
  #results = clean_df(results)
  #results = results[['Agency','City','State','Zipcode', 'Population','White','Black','Racialprplcy','RPSI']]
  #results['Racial Profiling Policy?'] = results['Racialprplcy'].map(lambda x: "Yes" if x==1 else "No") 
  #results = results[['Agency','City','State','Zipcode', 'Population','White','Black','Racial Profiling Policy?','RPSI']]
  #results.rename(columns={'Black':'Fraction of Black Officers','White':'Fraction of White Officers'}, inplace=True)
  #results_html=get_html(results)
  rpsi = results_series['rpsi']
  moreorless = 'LESS'
  if rpsi > 1.3 and rpsi<2.5: moreorless = 'MORE'
  elif rpsi > 2.5: moreorless = 'VERY'

  inequality = "equal"
  if rpsi > 1: inequality = "more"
  if rpsi < 1: inequality = "less"

  test = {}
  test['blah'] = 'woot'

  query = "SELECT * \
  	   FROM app_db;"
  results_all=pd.read_sql_query(query,con)

  average = results_all.mean()

  featuremap = OrderedDict()
  featuremap['entrymin'] = 'Minimum Officer Salary'
  featuremap['opbudget_per_capita'] = 'Operational Budget per capita'
  featuremap['urban_per_capita'] = 'Urban residents per capita'
  featuremap['population_black_per_capita'] = 'Black population per capita'
  featuremap['chiefmin'] = 'Minimum Chief Officer Salary'
  featuremap['entrymax'] = 'Maximum Officer Salary'
  featuremap['total_income_estimate_all_per_capita'] = 'Total Income per capita'
  featuremap['black_over_white_institutionalized_adult_local_jail_disparity'] =  'Black/White population in local jail'
  featuremap['total_income_estimate_white_per_capita'] = 'Total Income for white population per capita'
  featuremap['nummrkcars_per_capita'] = 'Number of marked cars per capita'
  featuremap['swnftemp_per_capita'] = 'Number of officers with arrest power per capita'
  featuremap['institutionalized_all_per_capita'] = 'Institutionalized residents per capita'
  featuremap['totacad'] = 'Total hours of training required for new recruits'
  featuremap['black_over_white_population_disparity'] = 'Black/White population disparity'

  
  descriptor = ''
  for feature in featuremap: 
  	 if results_series[feature] > 0.01:
         	descriptor +='The '+featuremap[feature].lower() +" is %3.2f as compared to the national average of %3.2f." % (results_series[feature],average[feature])
         else:
         	descriptor +='The '+featuremap[feature].lower() +" is %3.4f as compared to the national average of %3.4f." % (results_series[feature],average[feature])
         descriptor +='<br>'



  rpsi = "%3.2f" % (rpsi)
  print rpsi

  results_html=get_html(features)
  #the_result = ModelIt(patient,births)
  return render_template("output.html", 
  		agency=results_series['agency'], 
  		city=results_series['city'], 
  		state=results_series['state'], 
  		zipcode=results_series['zipcode'], 
		rpsi=rpsi,
		results_series=results_series,
		descriptor=descriptor,
		moreorless=moreorless,
		inequality=inequality,
  		policing_db = results_html)
