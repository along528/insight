# Insight Health Data Science

# ![pageres](image.png)
## Are you profiling me? 
www.areyouprofiling.me

This presents the work related to a project built by Alex Long for the Insight Health Data Science program in Boston during the summer of 2016. The project identifies and predicts those police departments in the US that are most susceptible to racial profiling. Beyond that it also seeks to highlight certain traits that seem to be correlated with racial profiling. The results are presented online at www.areyouprofiling.me. The site uses traffic stop data from North Carolina, Illinois, and Connecticut along with 2010 Census data and police department survey data collected by the Department of Justice.

Included are the input data sets and the code for running the web application along with studies and models of the data.  Datasets are processes using PostgreSQL and studied further in a series of python Jupyter notebooks using the python scientific computing stack indlucing pandas, scikit-learn, and matplotlib. The web application framework is built using Flask and Bootstrap with interactive visualizations built using D3 and Bokeh. 

### Installation
If you have Anaconda, the python dependencies can be setup by simply building a conda environment 
```
conda env create -f environment.yml
```
Then whenever running the app in a new shell activate the environment first
```
source activate insight
```

### Running the web application
To run locally, do
```
cd app/
./run.py
```
For the Bokeh visualizations to work you must also run the following simultaneously
```
bokeh serve --host localhost:5000 --host localhost:5006
```
Then, in your browser navigate to localhost:5000

To run a persistent server, you should have gunicorn and supervisor installed, then do
```
cd app/
sudo supervisord -c gunicorn.conf
```
To stop running do
```
sudo pkill -f supervisord
```

### Exploration
The modeling and data exploration was performed using a series of Jupyter notebooks contained in models/ and studies/. They can be viewed easily directly through github or can be tinkered with on your own by starting a Jupyter notebook server by running
```
jupyter notebook
```

### Getting the data
The raw and processed input data sets as well as the output data from the model are stored as PostgreSQL dumps and can be retrieved and loaded easily as long as you have PostgreSQL installed.

To download the sql data and load into separate databases just run
```
cd data
source download.sh
source load_all.sh
```
Note: The data does not need to be downloaded to run the web app.

### Built With
 * scikit-learn
 * pandas
 * matplotlib
 * Bokeh
 * Flask
 * Bootstrap
 * D3.js
 * Jupyter
 * SQLAlchemy
 * psycopg2
