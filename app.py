from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

MODEL_PATH = "models/full_features/rf_model.pkl"
model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return "Heart Disease Risk Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"] 
    prediction = model.predict([data])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
