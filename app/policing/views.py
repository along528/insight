from flask import render_template
import numpy as np
from policing import app
import pandas as pd
from flask import request,send_file
from os import sys
from collections import OrderedDict
import plotting

@app.route('/bullet')
def bullet():
    return render_template('bullet.html')

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

data = pd.read_csv('app_db.csv')
ratios = {}
ratios['hits_over_searches.csv'] = pd.read_csv('hits_over_searches.csv')
ratios['searches_over_stops.csv'] = pd.read_csv('searches_over_stops.csv')


@app.route('/scatter')
def scatter():
    img = plotting.get_scatter()
    return send_file(img,mimetype='image/png')
 
@app.route('/')
@app.route('/index')
@app.route('/input')
def input():
    return render_template("input.html")


@app.route('/output')
def output():
  agency = request.args.get('agency')
  results=data[data['agency'].str.contains(agency.title())]
  if np.shape(results)[0]==0:
      return render_template("input_retry.html")
  results = results.sort(columns=['population'],ascending=False).reset_index()
  results = results[results.index==0]
  features = results.drop(['index','surveyid','agency','city','state','zipcode'],axis=1)

  results_series = results.ix[0,:]
  #results = clean_df(results)
  #results = results[['Agency','City','State','Zipcode', 'Population','White','Black','Racialprplcy','RPSI']]
  #results['Racial Profiling Policy?'] = results['Racialprplcy'].map(lambda x: "Yes" if x==1 else "No") 
  #results = results[['Agency','City','State','Zipcode', 'Population','White','Black','Racial Profiling Policy?','RPSI']]
  #results.rename(columns={'Black':'Fraction of Black Officers','White':'Fraction of White Officers'}, inplace=True)
  #results_html=get_html(results)
  rpsi = -1
  if results_series['is_measured']:
	  rpsi = results_series['rpsi']
	  moreorless = 'LESS'
	  if rpsi > 1.3 and rpsi<2.5: moreorless = 'MORE'
	  elif rpsi > 2.5: moreorless = 'VERY'
  else:
          rpsi = results_series['rpsi_predicted']
	  moreorless = 'LESS'
	  if rpsi == 1: moreorless = 'MORE'
	  elif rpsi == 2: moreorless = 'VERY'


  inequality = "equal"
  if rpsi > 1: inequality = "more"
  if rpsi < 1: inequality = "less"

  summary = ""
  summary = 'The '+results_series['agency']+' is <b>'+moreorless+' SUSCEPTIBLE</b> to racial profiling '
  if results_series['is_measured']:
      summary +='with black drivers being %3.1f times %s likely to be searched than white drivers.' % (rpsi,inequality)
  else:
      summary+=' according to predictions comparing it to similar police departments where traffic stop information is available.'
  test = {}
  test['blah'] = 'woot'

  average = data.mean()

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
		summary=summary,
		surveyid=str(results_series['surveyid']),
  		policing_db = results_html)
