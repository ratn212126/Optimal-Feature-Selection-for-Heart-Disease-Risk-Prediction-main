from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("models/full_features/rf_model.pkl")

@app.route("/")
def home():
    return "Heart Disease Risk Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    prediction = model.predict([data])
    return jsonify({"prediction": int(prediction[0])})
