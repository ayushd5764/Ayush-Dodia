# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:12:22 2021

@author: Administrator
"""

#importing required libraries
from flask import Flask, request, render_template
import numpy as np
import re
import requests
import pandas as pd

#initializing the flask app
app = Flask(__name__)

def check(output):

    url = "https://facial-emotion-recognition.p.rapidapi.com/cloudVision/facialEmotionRecognition"
    
    querystring = {"source":output,"sourceType":"url"}
    
    payload = '''{\r\n    \"source\": "'''+output+'''" ,\r\n    \"sourceType\": \"url\"\r\n}'''
    headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "d730d682demshbfaf2fc584babdap15184djsnd2eec3eec4be",
    'x-rapidapi-host': "facial-emotion-recognition.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)
    
    a = response.json()['emotions']
    #converting the output to a dataframe using pandas
    df = pd.DataFrame(data=a)
    b = [i for i in range(1,len(a)+1)]
    ind={}
    for i in b:
        ind[i-1]="Person {:d}".format(i)
    #renaming the index and column names
    df=df.rename(index=ind)
    df.columns = ['Joy','Sorrow','Anger','Surprise','Under Exposed','Blurred','Hear Wear']
    df=df.replace(['VERY_UNLIKELY','UNLIKELY','VERY_LIKELY','LIKELY'], ["Very Unlikely","Unlikely","Very Likely","Likely"])
    #converting the dataframe to HTML table
    df_html = df.to_html(classes='mystyle', justify="center",col_space=90)
    
    return df_html
    

#home page
@app.route('/')
def home():
    return render_template('base.html')

#Summarizer page
@app.route('/predict',methods=['POST'])
def predict():
    output=request.form['output']
    df_html=check(output)
    return render_template('base.html',table_html=df_html)

    
if __name__ == "__main__":
    app.run(debug=True)