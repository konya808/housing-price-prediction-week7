import json
from app import app

sample_house = {
    "area": 7420,
    "bedrooms": 4,
    "bathrooms": 2,
    "stories": 3,
    "mainroad": "yes",
    "guestroom": "no",
    "basement": "no",
    "hotwaterheating": "no",
    "airconditioning": "yes",
    "parking": 2,
    "prefarea": "yes",
    "furnishingstatus": "furnished",
}

client = app.test_client()
response = client.post("/predict", json=sample_house)
print("Status:", response.status_code)
print(json.dumps(response.get_json(), indent=2))
