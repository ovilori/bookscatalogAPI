'''Creating Web APIs with Python and Flask - https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#understanding-our-database-powered-api
    This file contains the code for an example API - Distant Reading Archive API which is a book catalog.
'''
#imports the flask library and other library.
import flask

#this creates the flask application object, containing data about the application & also methods that tell the app what to do.
app = flask.Flask(__name__)

#starts the debugger.
app.config["DEBUG"] == True

#mapping the function 'home' to the path '/' and specifying the type of HTTP request that is allowed.
@app.route('/', methods=['GET'])

#homepage - function containing the result that will be displayed in the browser.
def home():
    return "<h1>This site is a prototype API for distant reading of science fiction novels.</p>"

#this method runs the application server.
app.run()