import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd 

app = Flask(__name__)
model = pickle.load(open('xg_model.pkl','rb'))


@app.route('/')
def startup():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = [float(x) for x in request.form.values()]
    print(features)
    # final_features = [np.array(features)]
    (speed,rpm,acc) = tuple(features)
    data = {'speed':speed,'rpm':rpm,'acc':acc}
    predict_df = pd.DataFrame([data])
    prediction = model.predict(predict_df)

    output = prediction[0]

    if output==0:
        output='Normal'
    elif output==1:
        output='Abnormal'
    else:
        output='Reckless'

    return render_template('index.html',prediction_text= 'Driver Behaviour currently : {}'.format(output))

if __name__=='__main__':
    app.run(debug = True)
