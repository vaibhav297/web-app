
from flask import Flask 
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return "<h1>This is finance vision page</h1>"
