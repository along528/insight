from flask import render_template
import numpy as np
from policing import app
import pandas as pd
from flask import request,send_file
from os import sys
from collections import OrderedDict
import plotting
import json
from sets import Set
"""
run bokeh serve locally first
by doing either
bokeh serve --host localhost:5000 --host localhost:5006
or
bokeh serve --host '*'
the latter might be less secure
"""

from bokeh.client import push_session,pull_session
from bokeh.embed import autoload_server
from bokeh.plotting import figure, curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, HoverTool

url = 'http://54.203.148.173:5006'
data = pd.read_csv('app_db.csv')
ratios = {}
df_hit_rate = pd.read_csv('hits_over_searches.csv').rename(columns=lambda x: x+"_hit_rate")
df_search_rate = pd.read_csv('searches_over_stops.csv').rename(columns=lambda x: x+"_search_rate")
df_rates = pd.read_csv('traffic_rates.csv').dropna()
source_rates = ColumnDataSource(df_rates)

def format(figure):
	  figure.title_text_color = "white"
	  figure.background_fill_color = "black"
	  figure.border_fill_color = "black"
	  figure.outline_line_color = "white"
	  figure.xaxis.axis_line_color = "white"
	  figure.yaxis.axis_line_color = "white"
	  figure.xaxis.major_label_text_color = "white"
	  figure.yaxis.major_label_text_color = "white"
	  figure.xaxis.axis_label_text_color = "white"
	  figure.yaxis.axis_label_text_color = "white"
	  figure.xaxis.minor_tick_line_color = "white"
	  figure.yaxis.minor_tick_line_color = "white"
	  figure.xaxis.major_tick_line_color = "white"
	  figure.yaxis.major_tick_line_color = "white"
	  return figure


@app.route('/search')
def search(query=None,return_top_surveyid=False,num_br=3):
	
	if query==None:
	    query = request.args.get('agency_query')
	try:
	    if len(query)<3: return '<br>'*num_br
	except:
	    return '<br>'*num_br
	#look for agencies that match
	#take the intersection of any combination of words
	agency_matches_set =None
	if len(query)>=3:
	  for word in query.split():
	    if len(word)<3: continue
	    if agency_matches_set == None:
                agency_matches_set = Set(data[data['agency']\
			.str.contains(word.title())].index.tolist())
	    else:
                agency_matches_set  = agency_matches_set.\
			intersection(Set(data[data['agency'].str.\
				contains(word.title())].index.tolist()))
	        

	#look for states that match
	state_matches = []
	for word in query.split():
	    if len(word)!=2: continue
            state_matches+=data[data['state'].str.contains(\
	    	word.upper())].index.tolist()
	#if len(query)<3: 
        #	city_matches+=data[data['city'].str.contains(query.title())].index.tolist()

	state_matches_set = set(state_matches)
	matches_set = agency_matches_set #.union(city_matches_set)
	#if including the state still gives some matches,
	#update to this, assuming it narrows things down
	#if it returns no match, assume this means
	#that the user isn't typing a state and just use the agency.
	if len(state_matches)>0:
            tmp_matches_set = matches_set.intersection(state_matches_set)
	    if len(tmp_matches_set)!=0:
	       matches_set = tmp_matches_set

	matches = list(matches_set)

	
	matched_data = data[data.index.isin(matches)]
        matched_data = matched_data.sort(columns=['total'],ascending=False).reset_index()

	output = ''
	count = 0
	#sort by 
	for index,series in matched_data.iterrows():
	    agency = series['agency']
	    city = series['city']
	    state = series['state']
	    surveyid = series['surveyid']
	    print surveyid,agency,city,state
	    if return_top_surveyid:
	        return surveyid
	    output+="%s, %s, %s"  % (agency,city,state)
	    output+="<br>"
	    count+=1
	    if count >= 3: break
	if count==0 and return_top_surveyid:
	    return -1
	elif count==0:
	    return "No Match" +"<br>"*(num_br)
	output += "<br>"*(num_br-count)
	print output
	return output

@app.route('/test')
def test():
    return render_template('input.min.html')

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



@app.route('/scatter')
def scatter():
    img = plotting.get_scatter()
    return send_file(img,mimetype='image/png')
 
@app.route('/')
@app.route('/index')
@app.route('/input')
def input():

  hover = HoverTool( tooltips=[ ('Agency','<font color="#000000"> @agency, @city, @state</font>')])
  plot = format(figure(title="Hit Rate vs Search Rate Split by Race",plot_width=800, plot_height=400,tools=[hover,"pan","wheel_zoom","box_zoom","reset"]))
  plot.circle('black_search_rate','black_hit_rate',color="#dd3439",size=10,source=source_rates,legend="Black Drivers",alpha=0.7)
  plot.circle('white_search_rate','white_hit_rate',color="#257bf8",size=10,source=source_rates,legend="White Drivers",alpha=0.7)
  plot.xaxis.axis_label = "Searches / Stops"
  plot.yaxis.axis_label = "Hits / Searches"

  curdoc().add_root(plot)
  session = push_session(curdoc())
  bokeh_script = autoload_server(plot, session_id=session.id, url=url)
  bokeh_id = bokeh_script.split()[2].split('"')[1]
  print "script:"
  print bokeh_script
  print "id:"
  print bokeh_id
  return render_template("input.html",
		bokeh_script=bokeh_script)


@app.route('/output')
def output():
  surveyid = search(query=request.args.get('agency_query'),return_top_surveyid=True)
  print "ID",surveyid
  try:
     results=data[data['surveyid']==surveyid]
  except:
      return render_template("input.html")

  if np.shape(results)[0]==0:
      #return render_template("input_retry.html")
      return render_template("input.html")
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
	  if rpsi > 1.6 and rpsi<=2.2: moreorless = 'MORE'
	  elif rpsi > 2.2: moreorless = 'VERY'
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
      summary = 'The '+results_series['agency']+' is <b>'+moreorless+' SUSCEPTIBLE</b> to racial profiling '
      summary +='with black drivers being %3.1f times %s likely to be searched than white drivers.' % (rpsi,inequality)
  else:
      summary = 'The '+results_series['agency']+' is predicted to be <b>'+moreorless+' SUSCEPTIBLE</b> to racial profiling. '
      #summary+='according to comparisons to similar police departments where traffic stop information is available. '
      summary+='Agencies with this classification are predicted to search black drivers ' 
      if moreorless == 'MORE':
         summary+='60% to 120% more often than white drivers.'
      elif moreorless == 'LESS':
         summary+='more often than white drivers by no more than 60%.'
      elif moreorless == 'VERY':
         summary+='at least 120% more often white drivers.'


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


  alpha = 0.7
  legend_tag = ""
  has_traffic_data = results_series['is_measured'] #df_rates[df_rates.surveyid==surveyid].count!=0
  if has_traffic_data:
      alpha = 0.2
      legend_tag = " - Other Agencies"


  bokeh_script_rates_measured = ""
  if results_series['is_measured']:
  	  hover1 = HoverTool( tooltips=[ ('Agency','<font color="#000000"> @agency, @city, @state</font>')])
	  plot1 = format(figure(title="Hit Rate vs Search Rate Split by Race",plot_width=800, plot_height=400,tools=[hover1,"pan","wheel_zoom","box_zoom","reset"]))
	  plot1.circle('black_search_rate','black_hit_rate',color="#dd3439",size=10,
		      source=source_rates,legend="Black Drivers - Other Agencies",alpha=0.2)
	  plot1.circle('white_search_rate','white_hit_rate',color="#257bf8",size=10,
		      source=source_rates,legend="White Drivers - Other Agencies",alpha=0.2)
	  if has_traffic_data:
	      plot1.circle('black_search_rate','black_hit_rate',color="#dd3439",size=20,
		      source=ColumnDataSource(df_rates[df_rates.surveyid==surveyid]),
		      legend="Black Drivers - "+results_series['agency'], alpha=1.)
	      plot1.circle('white_search_rate','white_hit_rate',color="#257bf8",size=20,
		      source=ColumnDataSource(df_rates[df_rates.surveyid==surveyid]),
		      legend="White Drivers - "+results_series['agency'], alpha=1.)
	  plot1.xaxis.axis_label = "Searches / Stops"
	  plot1.yaxis.axis_label = "Hits / Searches"

	  curdoc().add_root(plot1)
	  session = push_session(curdoc())
	  bokeh_script_rates_measured = autoload_server(plot1, session_id=session.id, url=url)
	  print bokeh_script_rates_measured

  hover2 = HoverTool( tooltips=[ ('Agency','<font color="#000000"> @agency, @city, @state</font>')])
  plot2 = format(figure(title="Hit Rate vs Search Rate Split by Race",plot_width=800, plot_height=400,tools=[hover2,"pan","wheel_zoom","box_zoom","reset"]))
  plot2.circle('black_search_rate','black_hit_rate',color="#dd3439",size=10,
  	      source=source_rates,legend="Black Drivers",alpha=0.7)
  plot2.circle('white_search_rate','white_hit_rate',color="#257bf8",size=10,
              source=source_rates,legend="White Drivers",alpha=0.7)
  plot2.xaxis.axis_label = "Searches / Stops"
  plot2.yaxis.axis_label = "Hits / Searches"

  curdoc().add_root(plot2)
  session = push_session(curdoc())
  bokeh_script_about = autoload_server(plot2, session_id=session.id, url=url)
  print bokeh_script_about

  do_display = ""
  if not results_series['is_measured']:
  	#by setting this, it can be used in a section or 
	#div to turn off the display of that section
  	do_display = 'style="display:none"'


  results_html=get_html(features)
  #the_result = ModelIt(patient,births)
  return render_template("output.html", 
  		agency=results_series['agency'], 
  		city=results_series['city'], 
  		state=results_series['state'], 
  		zipcode=results_series['zipcode'], 
		rpsi=rpsi,
		bokeh_script_about=bokeh_script_about,
		bokeh_script_rates_measured=bokeh_script_rates_measured,
		do_display=do_display,
		#bokeh_id=bokeh_id,
		results_series=results_series,
		descriptor=descriptor,
		moreorless=moreorless,
		inequality=inequality,
		summary=summary,
		surveyid=str(results_series['surveyid']),
  		policing_db = results_html)
