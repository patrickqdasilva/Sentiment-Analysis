from flask import Flask, jsonify, request, render_template
import os
from utilities import make_prediction

# Create the Flask app and set the model path
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form['input_text']
    try:
        type(data) == str
    except KeyError:
        return jsonify({'error': 'No text entered'})
    prediction = make_prediction(data)
    try:
        result = jsonify(prediction)
    except TypeError as e:
        return jsonify({'error': str(e)})
    
    # Render the prediction template and pass the prediction to it
    return render_template('prediction.html', prediction=prediction)

if __name__ == '__main__':
    app.run()