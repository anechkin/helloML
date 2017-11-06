#!ipython --version

#Flask already installed
from flask import Flask

#creates an app object from Flask
app = Flask(__name__)

#request defined
@app.route("/")
def hello():
    return "Hello Flask World!"

#app.run() starts the web server and ready to handle the request. 
#But at this moment, it can handle only one request.
if __name__ == "__main__":
    app.run()