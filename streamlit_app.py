import requests
import streamlit as st

st.set_page_config(
    page_title="Housing Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Housing Price Predictor")
st.write("Enter the property details below to generate a house-price prediction.")

api_url = st.text_input(
    "Prediction API URL",
    value="http://127.0.0.1:5000/predict"
)

area = st.number_input("Area (sq ft)", min_value=100.0, value=7420.0, step=100.0)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=20, value=4, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2, step=1)
stories = st.number_input("Stories", min_value=1, max_value=10, value=3, step=1)

col1, col2 = st.columns(2)
with col1:
    mainroad = st.selectbox("Main road", ["yes", "no"])
    guestroom = st.selectbox("Guest room", ["yes", "no"])
    basement = st.selectbox("Basement", ["yes", "no"])
    hotwaterheating = st.selectbox("Hot water heating", ["yes", "no"])
with col2:
    airconditioning = st.selectbox("Air conditioning", ["yes", "no"])
    parking = st.number_input("Parking spaces", min_value=0, max_value=10, value=2, step=1)
    prefarea = st.selectbox("Preferred area", ["yes", "no"])
    furnishingstatus = st.selectbox(
        "Furnishing status",
        ["furnished", "semi-furnished", "unfurnished"]
    )

if st.button("Predict House Price", type="primary"):
    payload = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "parking": parking,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus,
    }

    try:
        response = requests.post(api_url, json=payload, timeout=20)
        result = response.json()

        if response.ok:
            st.success(
                f"Predicted price: KES {result['predicted_price']:,.2f}"
            )
            st.caption(
                f"Model: {result.get('model', 'Optimized Random Forest Regressor')}"
            )
        else:
            st.error(result.get("error", "Prediction request failed."))
    except requests.RequestException as exc:
        st.error(
            "Could not connect to the prediction API. "
            "Start Flask first and check the API URL."
        )
        st.code(str(exc))
