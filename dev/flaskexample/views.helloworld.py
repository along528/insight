from flask import render_template
from flaskexample import app

@app.route('/')
@app.route('/index')
def index():
   user = { 'nickname': 'Miguel' } # fake user
   return render_template("index.html",
             title = 'Home',
	     user = user)
"""
def index():
   user = { 'nickname': 'Miguel' } # fake user
   return '''
            <html>
             <head>
               <title>Home Page</title>
             </head>
             <body>
               <h1>Hello, ''' + user['nickname'] + '''</h1>
             </body>
            </html>
          '''
"""

#def index():
#   return "Hello, World!"
