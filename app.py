
from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained ML model
with open('weight_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Predict weight
@app.route('/predict', methods=['POST'])
def predict():

    height = float(request.form['height'])

    # Predict using trained model
    prediction = model.predict(
        pd.DataFrame({'Height': [height]})
    )

    result = round(prediction[0], 2)

    return render_template(
        'index.html',
        prediction_text=f'Predicted Weight: {result} kg'
    )

if __name__ == '__main__':
    app.run(debug=True)
