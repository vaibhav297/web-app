from app.code import startx, temp, len_mth, mth_list,week_list,len1,len2,actual_list

from flask import Flask, render_template
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view():
        return render_template("home.html")

@app.route("/DashBoard")
def dashboard():
    return render_template("DashBoard.html", temp=temp, len1=len1,len2=len2,len_mth=len_mth,mth_list=mth_list,week_list=week_list, actual_list = actual_list)

