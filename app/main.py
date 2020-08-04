from app.code import startx,temp

from flask import Flask, render_template
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view():
        return render_template("home.html")
@app.route("/DashBoard")
def dashboard():
    return "<p>"+str(temp)+"</p>"