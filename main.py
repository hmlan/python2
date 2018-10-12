from flask import Flask,render_template,request
import requests
app = Flask('_name_')
@app.route("/")
def home():
    return render_template("home.html",resp=None)
