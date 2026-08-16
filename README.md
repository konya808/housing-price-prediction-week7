# 🏠 Housing Price Prediction — Week 7 Deployment

## 1. Project Description

This project deploys the optimized **Random Forest Regressor** developed during Week 6 of the AnalystLab Africa Data Science Internship.

The model predicts residential property prices using property characteristics such as area, bedrooms, bathrooms, stories, amenities, parking, preferred area, and furnishing status.

The Week 7 deployment converts the trained machine-learning model into a practical application that users can interact with through a **Flask REST API** and an interactive **Streamlit interface**.

The trained model is saved and reused without retraining.

---

## 2. Problem Statement

House prices vary according to several property characteristics, including property size, number of bedrooms and bathrooms, number of stories, available amenities, parking spaces, preferred-area status, and furnishing status.

The objective of this project is to develop a machine-learning solution that can estimate the price of a house from these characteristics and make the trained model accessible for real-world use through an API and web interface.

---

## 3. Week 7 Objectives

The deployment focuses on the following objectives:

- Save and reuse the trained machine-learning model.
- Build a prediction API using Flask.
- Test the prediction endpoint with sample input data.
- Create a Streamlit user interface.
- Connect the user interface to the prediction API.
- Display prediction results to users.
- Document the project and API.
- Prepare the application for cloud deployment.

These objectives follow the AnalystLab Africa Week 7 requirement of making a trained machine-learning model available for real-world use through an API or simple web application. :contentReference[oaicite:1]{index=1}

---

# 4. Machine Learning Model

### Model Used

**Optimized Random Forest Regressor**

The optimized model developed during Week 6 is saved using Joblib as:

```text
housing_optimized_random_forest.joblib

The deployment loads this saved model directly, meaning the model does not need to be retrained every time the application starts.

The API also uses the Week 6 feature-engineering process contained in:

feature_engineering.py

5. Input Features

The model receives the following housing characteristics:

Feature	Description
area	Property area in square feet
bedrooms	Number of bedrooms
bathrooms	Number of bathrooms
stories	Number of stories
mainroad	Whether the property is connected to the main road
guestroom	Whether the property has a guest room
basement	Whether the property has a basement
hotwaterheating	Whether hot-water heating is available
airconditioning	Whether air conditioning is available
parking	Number of parking spaces
prefarea	Whether the property is in a preferred area
furnishingstatus	Furnishing status of the property

6. Technologies Used
Technology	Purpose
Python	Main programming language
Pandas	Data handling
NumPy	  Numerical operations
Scikit-learn	 Machine-learning model
Joblib	 Model saving and loading
Flask	 Prediction REST API
Requests	 API testing and communication
Streamlit	 Interactive user interface
Git 	Version control
GitHub 	Source-code hosting
Render 	Cloud deployment

7. Prediction API

The project uses Flask to expose the trained model through a REST API.

GET /

Checks whether the Housing Price Prediction API is running.

Example response
{
  "endpoint": "POST /predict",
  "message": "Housing Price Prediction API is running",
  "model": "Optimized Random Forest Regressor",
  "status": "healthy"
}
GET /health

Checks the health of the API and confirms that the trained model has been loaded successfully.

POST /predict

Accepts housing information in JSON format and returns the predicted house price.

Input Format
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
Output Format
{
  "currency": "KES",
  "model": "Optimized Random Forest Regressor",
  "predicted_price": 8553854.26
}

The prediction value changes according to the property information submitted to the API.

8. API Testing

The prediction API was tested locally using:

python test_api.py

The API successfully returned:

Status: 200

with the following prediction:

{
  "currency": "KES",
  "model": "Optimized Random Forest Regressor",
  "predicted_price": 8553854.26
}

This confirms that:

The Flask API is running.
The saved model loads successfully.
The prediction endpoint accepts the required input.
The API successfully returns a prediction.

9. Streamlit User Interface

A Streamlit interface was created to make the model easier for users to interact with.

Instead of manually sending JSON requests to the API, users can enter the property information through a form.

The interface collects:

Area
Bedrooms
Bathrooms
Stories
Main road status
Guest room status
Basement status
Hot-water heating status
Air-conditioning status
Parking spaces
Preferred-area status
Furnishing status

The submitted information is sent to the Flask /predict endpoint and the predicted house price is displayed on the Streamlit interface.

Run Streamlit
streamlit run streamlit_app.py

The local application is normally available at:

http://localhost:8501
Successful UI Test

The Streamlit application successfully generated:

Predicted price: KES 8,652,269.52

This confirms that the complete local application flow works:

User Input
     ↓
Streamlit Interface
     ↓
Flask Prediction API
     ↓
Feature Engineering
     ↓
Saved Random Forest Model
     ↓
Prediction
     ↓
Streamlit Result
10. Setup Instructions
Step 1 — Clone the Repository
git clone https://github.com/konya808/housing-price-prediction-week7.git

Move into the project directory:

cd housing-price-prediction-week7
Step 2 — Create a Virtual Environment
python -m venv .venv
Step 3 — Activate the Virtual Environment
Windows
.venv\Scripts\activate

If PowerShell prevents script activation, the project's Python executable can be used directly:

.venv\Scripts\python.exe
Step 4 — Install Dependencies
pip install -r requirements.txt
11. How to Run the Project
Start the Flask API

Run:

python app.py

The API runs locally at:

http://127.0.0.1:5000
Test the API

Open a second terminal and run:

python test_api.py

A successful test returns:

Status: 200

and a predicted house price.

Start the Streamlit Application

Keep the Flask API running.

Open another terminal and run:

streamlit run streamlit_app.py

The Streamlit interface can then be opened in the browser.

12. Deployment

The project includes a render.yaml configuration file for cloud deployment of the Flask API on Render.

The intended deployment architecture is:

GitHub Repository
        ↓
      Render
        ↓
 Flask Prediction API
        ↓
 Feature Engineering
        ↓
Saved Random Forest Model
        ↓
 Predicted House Price

After the Flask API is deployed, the Streamlit application can communicate with the public /predict endpoint instead of the local API URL.

Deployment Status
GitHub repository: Completed
Local Flask API: Working
Local API testing: Successful
Local Streamlit application: Working
Render deployment: Next step
Demo video: To be recorded
LinkedIn post: To be prepared
13. Project Structure
Housing_Week7_Deployment/
│
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
14. Week 7 Requirement Checklist
Week 7 Requirement	Status
Save trained model using Joblib	✅ Completed
Build prediction API using Flask	✅ Completed
Load saved model	✅ Completed
Create prediction endpoint	✅ Completed
Test API with sample input	✅ Completed
Confirm predictions are returned	✅ Completed
Create Streamlit user interface	✅ Completed
Allow users to enter data through a form	✅ Completed
Connect interface to the model/API	✅ Completed
Display prediction results	✅ Completed
Create comprehensive README	✅ Completed
Upload source code to GitHub	✅ Completed
Deploy API/application	🔄 In Progress
Record 2–5 minute demo video	⏳ Pending
Prepare LinkedIn post	⏳ Pending

The Week 7 handbook requires the saved model, GitHub source code, working API/deployed application, README, demo video, and LinkedIn post/link as the main deliverables.

15. Key Lessons Learned

This deployment demonstrates that developing a machine-learning model is only one part of a complete data-science workflow.

The project provided practical experience in:

Saving and reusing a trained machine-learning model.
Building a REST API with Flask.
Testing an API using sample requests.
Connecting a user interface to a machine-learning API.
Using Streamlit to make predictions accessible to users.
Structuring a machine-learning project for GitHub.
Preparing a machine-learning application for cloud deployment.

The deployment process demonstrates how a trained model can move from a development environment into a practical application that users can interact with.

16. Internship Context

This project was completed as part of the AnalystLab Africa Data Science Internship — Week 7: Model Deployment & Real-World Application.

Week 7 focuses on making a trained machine-learning model available for real-world use through an API or simple web application.

The project implements the required workflow:

Trained Model
     ↓
Saved Joblib Model
     ↓
Flask Prediction API
     ↓
API Testing
     ↓
Streamlit User Interface
     ↓
Cloud Deployment

17. GitHub Repository

Repository:

https://github.com/konya808/housing-price-prediction-week7

Technologies & Skills Demonstrated

Python • Machine Learning • Random Forest Regression • Scikit-learn • Flask • REST API • Streamlit • Joblib • Git • GitHub • Model Deployment