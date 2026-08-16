# 🏠 Housing Price Prediction — Week 7 Deployment

## Project Overview
This project deploys the optimized Random Forest Regressor developed during Week 6 of the AnalystLab Africa Data Science Internship.

The model predicts house prices from property characteristics such as area, bedrooms, bathrooms, stories, amenities, parking, preferred area, and furnishing status.

## Week 7 Objectives
- Save and reuse the trained machine-learning model.
- Build a prediction API with Flask.
- Test the prediction endpoint.
- Provide a Streamlit user interface.
- Prepare the project for cloud deployment.
- Document the API and setup process.

## Model
**Optimized Random Forest Regressor**

The saved model is loaded from:
`housing_optimized_random_forest.joblib`

The API applies the Week 6 feature-engineering process before generating a prediction.

## Input Features
- area
- bedrooms
- bathrooms
- stories
- mainroad
- guestroom
- basement
- hotwaterheating
- airconditioning
- parking
- prefarea
- furnishingstatus

## API Endpoints

### `GET /`
Confirms that the API is running.

### `GET /health`
Returns the API health status and confirms that the model is loaded.

### `POST /predict`
Accepts housing information as JSON and returns the predicted house price.

Example request:

```json
{
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
  "furnishingstatus": "furnished"
}
```

Example response:

```json
{
  "predicted_price": 0.0,
  "currency": "KES",
  "model": "Optimized Random Forest Regressor"
}
```

The exact prediction depends on the saved Week 6 model.

## Run Locally

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
python app.py
```

The API will run on:

`http://127.0.0.1:5000`

In a second terminal, test it:

```bash
python test_api.py
```

## Run the Streamlit Interface

Keep Flask running, then open another terminal:

```bash
streamlit run streamlit_app.py
```

The Streamlit application will provide a form for entering property details and display the API prediction.

## Deployment
The included `render.yaml` prepares the Flask API for deployment on Render.

After deployment, the Streamlit API URL can be changed from the local URL to the deployed `/predict` endpoint.

## Project Structure

```text
Housing_Week7_Deployment/
├── app.py
├── streamlit_app.py
├── feature_engineering.py
├── test_api.py
├── housing_optimized_random_forest.joblib
├── Housing.csv
├── requirements.txt
├── render.yaml
├── .gitignore
└── README.md
```

## Internship Requirement
This deployment addresses the AnalystLab Africa Week 7 requirements for model reuse, prediction API development, API testing, user interface creation, project documentation, and deployment preparation.
