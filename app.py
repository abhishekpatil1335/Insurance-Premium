import numpy as np
import pickle
import math
from flask import Flask, request , jsonify, render_template

app = Flask(__name__,template_folder="Template", static_folder= "staticfiles")
model = pickle.load(open('build.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['post'])

def predict():

    # Convert non-empty form values to floats
    float_features = [float(x) for x in request.form.values() if x.strip()]
    final_features= [np.array(float_features)]
    prediction = model. predict(final_features)
    if prediction ==0:
        return render_template('index.html', prediction_text="better health").format(prediction)
    else:
        return render_template('index.html', prediction_text="no better health ").format(prediction)

if __name__=="__main__":
    app.run(debug = True)