import requests
import json


with open('model.pkl', 'rb') as f:
  newdata = pickle.load(f)

response = requests.post("http://127.0.0.1:5000/predict", json = {'data': newdata})
data  = response.json()
prediction = data['prediction']
print("Good day to you. The prediction for the data is:", prediction)