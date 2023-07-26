from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
from modules.insurance import InsurancePredict

app = Flask(__name__)

@app.route("/")
def home():
    return 'API MODELLING'

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data,index = [0])
    predict_code =  InsurancePredict().runModel(df, typed='single')
    
    result_predict = 'Intrested' if predict_code==1 else 'Not Intrested'
    
    return jsonify({
        "status":"Predicted",
        "predict_code":predict_code,
        "result":result_predict,
        "data":data
    })