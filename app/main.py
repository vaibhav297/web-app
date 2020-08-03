from app.code import startx
from flask import Flask
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view():
        return "<h1>hello</h1>"
