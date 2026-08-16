from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, request

from feature_engineering import engineer_features

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "housing_optimized_random_forest.joblib"

app = Flask(__name__)
model = joblib.load(MODEL_PATH)

REQUIRED_FIELDS = [
    "area", "bedrooms", "bathrooms", "stories",
    "mainroad", "guestroom", "basement", "hotwaterheating",
    "airconditioning", "parking", "prefarea", "furnishingstatus",
]

ALLOWED_YES_NO = {"yes", "no"}
ALLOWED_FURNISHING = {"furnished", "semi-furnished", "unfurnished"}


@app.get("/")
def home():
    return jsonify({
        "message": "Housing Price Prediction API is running",
        "model": "Optimized Random Forest Regressor",
        "endpoint": "POST /predict",
        "status": "healthy",
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy", "model_loaded": True})


@app.post("/predict")
def predict():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    invalid_binary = [
        field for field in [
            "mainroad", "guestroom", "basement", "hotwaterheating",
            "airconditioning", "prefarea"
        ]
        if str(data[field]).lower() not in ALLOWED_YES_NO
    ]
    if invalid_binary:
        return jsonify({
            "error": "Binary fields must be 'yes' or 'no'.",
            "fields": invalid_binary,
        }), 400

    furnishing = str(data["furnishingstatus"]).lower()
    if furnishing not in ALLOWED_FURNISHING:
        return jsonify({
            "error": "furnishingstatus must be furnished, semi-furnished, or unfurnished."
        }), 400

    try:
        row = data.copy()
        for field in ["area", "bedrooms", "bathrooms", "stories", "parking"]:
            row[field] = float(row[field])
        for field in [
            "mainroad", "guestroom", "basement", "hotwaterheating",
            "airconditioning", "prefarea"
        ]:
            row[field] = str(row[field]).lower()
        row["furnishingstatus"] = furnishing

        features = engineer_features([row])
        prediction = float(model.predict(features)[0])

        return jsonify({
            "predicted_price": round(prediction, 2),
            "currency": "KES",
            "model": "Optimized Random Forest Regressor",
        })

    except (TypeError, ValueError) as exc:
        return jsonify({"error": f"Invalid input: {exc}"}), 400
    except Exception as exc:
        return jsonify({"error": f"Prediction failed: {exc}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
