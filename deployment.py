from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
import joblib

def return_prediction(model, scaler, sample_json):
    s_len   = sample_json['sepal_length']
    s_width = sample_json['sepal_width']
    p_len   = sample_json['petal_length']
    p_width = sample_json['petal_width']
    flower = [[s_len, s_width, p_len, p_width]]

    classes = np.array(['setosa', 'versicolor', 'virginica'])
    flower = scaler.transform(flower)
    prediction = model.predict(flower)
    class_ind = np.argmax(prediction, axis=1)[0]
    return classes[class_ind]

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>FLASK APP IS RUNNING</h1>'

# Load model and scaler
flower_model = load_model("iris_model.h5")
flower_scaler = joblib.load("iris_scaler.pkl")

@app.route('/api/flower', methods=['POST'])
def flower_prediction():
    content = request.json
    try:
        results = return_prediction(flower_model, flower_scaler, content)
        return jsonify({'prediction': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)