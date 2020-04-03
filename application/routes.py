from application import app
from flask import render_template, request, json, Response
import numpy as np
from sklearn import datasets
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/irisclassify", methods=['GET', 'POST'])
def irisclassify():
    username = request.form.get('username')
    
    sepallength = request.form.get("sepallength")
    sepalwidth = request.form.get("sepalwidth")
    petallength = request.form.get("petallength")
    petalwidth = request.form.get("petalwidth")

    data = [[sepallength, sepalwidth, petallength, petalwidth]]

    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    rfc = RandomForestClassifier(n_estimators = 100, n_jobs = 2)
    rfc.fit(X_train, y_train)
#   print 'Accuracy = %0.2f' % accuracy_score(y_test, rfc.predict(X_test)) 
#    return classification_report(y_test, rfc.predict(X_test))
    
    result = rfc.predict(data)
    return render_template("prediction.html", result=result)