from flask import render_template
from policing import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from flask import request
import ridge_regression
from os import sys

user = 'along528' #add your username here (same as previous postgreSQL)                      
host = 'localhost'
dbname = 'traffic_police_combined'
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
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Miguel' },
       )

@app.route('/db')
def db_page_fancy():
    sql_query = """
                SELECT agency,zipcode,year,white,black,rpsi FROM combined_rpsi_searches_over_stops_black_over_white WHERE year = 2006;          
                """
    results=get_html(clean_df(pd.read_sql_query(sql_query,con)))
    return render_template('rpsi_db.html', policing_db=results)
 
@app.route('/input')
def input():
    return render_template("input.html")

@app.route('/output_old')
def output_old():
  agency = request.args.get('agency')
  query = "SELECT agency,zipcode,year,white,black,rpsi \
  	   FROM combined_rpsi_searches_over_stops_black_over_white \
	   WHERE year = 2006 AND (agency LIKE '%"+agency.upper()+"%');" 
  results=get_html(clean_df(pd.read_sql_query(query,con)))
  #the_result = ModelIt(patient,births)
  return render_template("output.html", policing_db = results)

@app.route('/output')
def output():
  agency = request.args.get('agency')
  query = "SELECT * \
  	   FROM survey_features \
	   WHERE (agency LIKE '%"+agency.upper()+"%');" 
  features=pd.read_sql_query(query,con)
  results = ridge_regression.prediction(features)
  results = clean_df(results)
  results = results[['Agency','City','State','Zipcode', 'Population','White','Black','Racialprplcy','RPSI']]
  results['Racial Profiling Policy?'] = results['Racialprplcy'].map(lambda x: "Yes" if x==1 else "No") 
  results = results[['Agency','City','State','Zipcode', 'Population','White','Black','Racial Profiling Policy?','RPSI']]
  results.rename(columns={'Black':'Fraction of Black Officers','White':'Fraction of White Officers'}, inplace=True)
  results_html=get_html(results)
  #the_result = ModelIt(patient,births)
  return render_template("output.html", policing_db = results_html)
