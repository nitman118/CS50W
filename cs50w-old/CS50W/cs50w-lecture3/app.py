from flask import Flask, render_template
import datetime

app=Flask(__name__)

@app.route("/")
def index():
    now=datetime.datetime.now()
    # headline ="Hello, headline"
    new_year=now.month==1 and now.day==1
    return render_template("index.html", new_year=new_year)

# @app.route("/<string:name>")
# def nitish(name):
#     name=name.capitalize()
#     return render_template("index.html", headline="Hello, "+name)
