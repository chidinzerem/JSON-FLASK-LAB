from flask import Flask
import pickle
app = Flask(__name__)


with open('model.pkl', 'rb') as f:
  newdata = pickle.load(f)


@app.route("/predict", method=['POST'])
def predict():
    if request.method == 'POST'
        the_data = request.get_json(force=True)
        print(the_data ['data'])
        prediction = pipe.predict()
        return{'prediction': prediction.tolist()}

app.route('/')
def index():
    return 'index page'

app.route('/hello')
def hello():
    return 'hello, world'

import getpass

app.route('/api')
def me_api():
    username = getpass.getuser()
    return{
        
    }