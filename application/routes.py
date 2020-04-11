from application import app
from flask import render_template, request, json, jsonify, Response
import numpy as np
from flask import render_template
import pickle
import requests
import sys

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/irisclassify", methods=['GET', 'POST'])
def irisclassify():
   
    sepallength = request.form.get("sepallength")
    sepalwidth = request.form.get("sepalwidth")
    petallength = request.form.get("petallength")
    petalwidth = request.form.get("petalwidth")

    #url = "http://localhost:8082/api"
    url = "https://irisservice.herokuapp.com/api"

    data = json.dumps({"sepallength": sepallength, "sepalwidth": sepalwidth, "petallength": petallength, "petalwidth": petalwidth})
    results =  requests.post(url,data)
    
    print(data, file=sys.stdout)
    print(results.content.decode('UTF-8'), file=sys.stdout)

    return render_template("index.html", sepallength = sepallength, sepalwidth = sepalwidth, petallength = petallength, petalwidth = petalwidth, results=results.content.decode('UTF-8'))
    #return render_template("prediction.html", form_data=data, results=results.content.decode('UTF-8'))

