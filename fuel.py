from flask import Flask,request,jsonify
import json


app = Flask(__name__)


@app.route('/')
def home():
    return 'Fuel Calculator'

@app.route('/mileage', methods=['POST'])
def predict():
    data = json.loads(request.data)
    print(data)
    return 'omm'

if __name__ == '__main__':
    app.run(debug=True)

# Car mileage = No. of Kms/ Quantity Of Fuel Used

