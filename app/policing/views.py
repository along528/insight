from flask import render_template
from policing import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from flask import request
from a_Model import ModelIt

user = 'along528' #add your username here (same as previous postgreSQL)                      
host = 'localhost'
dbname = 'traffic_police_combined'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Miguel' },
       )

@app.route('/db_fancy')
def db_page_fancy():
    sql_query = """
                SELECT agency,zipcode,year,white,black,rpsi FROM combined_rpsi_searches_over_stops_black_over_white WHERE year = 2006;          
                """
    query_results=pd.read_sql_query(sql_query,con)
    agencies = []
    for i in range(0,query_results.shape[0]):
        agencies.append(dict(agency=query_results.iloc[i]['agency'], zipcode=query_results.iloc[i]['zipcode'], rpsi=query_results.iloc[i]['rpsi']))
    return render_template('rpsi_db.html',agencies=agencies)
 
@app.route('/input')
def cesareans_input():
    return render_template("input.html")

@app.route('/output')
def cesareans_output():
  #pull 'birth_month' from input field and store it
  patient = request.args.get('birth_month')
    #just select the Cesareans  from the birth dtabase for the month that the user inputs
  query = "SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean' AND birth_month='%s'" % patient
  print query
  query_results=pd.read_sql_query(query,con)
  print query_results
  births = []
  for i in range(0,query_results.shape[0]):
      births.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
      the_result = ''
  #return render_template("output.html", births = births, the_result = the_result)
  the_result = ModelIt(patient,births)
  return render_template("output.html", births = births, the_result = the_result)
