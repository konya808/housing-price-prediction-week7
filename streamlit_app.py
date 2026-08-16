import requests
import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Haven | Housing Price Predictor",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* ---------- Global ---------- */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    .stApp {
        background:
            radial-gradient(circle at 8% 5%, rgba(231, 190, 220, 0.24), transparent 28%),
            radial-gradient(circle at 92% 8%, rgba(203, 191, 235, 0.22), transparent 30%),
            #fcf9fb;
        color: #302a32;
    }

    .main .block-container {
        max-width: 1180px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    /* ---------- Hide Streamlit clutter ---------- */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* ---------- Hero ---------- */
    .hero {
        background: linear-gradient(
            135deg,
            rgba(255, 247, 251, 0.98),
            rgba(244, 237, 250, 0.98)
        );
        border: 1px solid rgba(112, 88, 118, 0.10);
        border-radius: 28px;
        padding: 42px 46px;
        margin-bottom: 28px;
        box-shadow: 0 18px 55px rgba(82, 59, 83, 0.08);
        position: relative;
        overflow: hidden;
    }

    .hero::after {
        content: "";
        position: absolute;
        width: 230px;
        height: 230px;
        right: -70px;
        top: -90px;
        border-radius: 50%;
        background: rgba(211, 181, 222, 0.18);
    }

    .eyebrow {
        color: #9b6d92;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.25rem;
        line-height: 1.08;
        color: #352b35;
        margin: 0;
        position: relative;
        z-index: 2;
    }

    .hero-subtitle {
        color: #746a74;
        font-size: 1.05rem;
        line-height: 1.7;
        max-width: 690px;
        margin-top: 15px;
        position: relative;
        z-index: 2;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.76);
        border: 1px solid rgba(112, 88, 118, 0.12);
        border-radius: 999px;
        padding: 8px 14px;
        margin-top: 22px;
        color: #5e5360;
        font-size: 0.82rem;
        font-weight: 600;
    }

    .status-dot {
        width: 8px;
        height: 8px;
        background: #8dba9d;
        border-radius: 50%;
        display: inline-block;
    }

    /* ---------- Section headings ---------- */
    .section-heading {
        font-family: 'Playfair Display', serif;
        font-size: 1.65rem;
        color: #3b303b;
        margin: 8px 0 5px 0;
    }

    .section-caption {
        color: #817680;
        font-size: 0.91rem;
        margin-bottom: 18px;
    }

    /* ---------- Cards ---------- */
    .info-card {
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid rgba(112, 88, 118, 0.10);
        border-radius: 22px;
        padding: 22px 24px;
        box-shadow: 0 10px 32px rgba(82, 59, 83, 0.055);
        margin-bottom: 18px;
    }

    .info-label {
        color: #9b6d92;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 7px;
    }

    .info-value {
        color: #3c333d;
        font-size: 1rem;
        font-weight: 600;
    }

    /* ---------- Input styling ---------- */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        border-radius: 13px !important;
        border-color: rgba(112, 88, 118, 0.16) !important;
        background-color: rgba(255,255,255,0.82) !important;
    }

    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within {
        border-color: #b78aae !important;
        box-shadow: 0 0 0 1px #b78aae !important;
    }

    label {
        color: #544953 !important;
        font-weight: 600 !important;
    }

    /* ---------- API box ---------- */
    .api-card {
        background: #f5eff7;
        border: 1px solid rgba(112, 88, 118, 0.10);
        border-radius: 18px;
        padding: 18px 20px;
        margin: 10px 0 28px 0;
    }

    .api-title {
        font-size: 0.72rem;
        color: #96718e;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .api-url {
        color: #514550;
        font-family: monospace;
        font-size: 0.86rem;
        word-break: break-all;
    }

    /* ---------- Button ---------- */
    .stButton > button {
        width: 100%;
        min-height: 54px;
        border-radius: 16px;
        border: none;
        background: linear-gradient(135deg, #a8759f, #8d739f);
        color: white;
        font-size: 1rem;
        font-weight: 700;
        letter-spacing: 0.01em;
        box-shadow: 0 12px 28px rgba(141, 115, 159, 0.25);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 16px 32px rgba(141, 115, 159, 0.30);
    }

    /* ---------- Prediction result ---------- */
    .prediction-card {
        background: linear-gradient(135deg, #fff8fb, #f4eff8);
        border: 1px solid rgba(167, 125, 159, 0.18);
        border-radius: 26px;
        padding: 30px;
        margin-top: 24px;
        box-shadow: 0 18px 48px rgba(82, 59, 83, 0.09);
        text-align: center;
    }

    .prediction-label {
        color: #9b6d92;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
    }

    .prediction-price {
        font-family: 'Playfair Display', serif;
        color: #3b303b;
        font-size: 2.75rem;
        font-weight: 700;
        margin: 8px 0;
    }

    .prediction-model {
        color: #776d76;
        font-size: 0.84rem;
    }

    /* ---------- Snapshot ---------- */
    .snapshot {
        background: rgba(255,255,255,0.82);
        border: 1px solid rgba(112, 88, 118, 0.10);
        border-radius: 22px;
        padding: 24px;
        margin-top: 24px;
        box-shadow: 0 10px 32px rgba(82, 59, 83, 0.055);
    }

    .snapshot-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.35rem;
        color: #40353f;
        margin-bottom: 18px;
    }

    .metric-box {
        background: #faf6fa;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
    }

    .metric-name {
        color: #8b7e89;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .metric-value {
        color: #40353f;
        font-size: 1.05rem;
        font-weight: 700;
        margin-top: 3px;
    }

    /* ---------- Footer ---------- */
    .footer {
        text-align: center;
        color: #91858f;
        font-size: 0.78rem;
        margin-top: 45px;
        padding-top: 20px;
        border-top: 1px solid rgba(112, 88, 118, 0.10);
    }

    /* ---------- Mobile ---------- */
    @media (max-width: 768px) {
        .hero {
            padding: 30px 24px;
        }

        .hero-title {
            font-size: 2.35rem;
        }

        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Machine Learning · Real Estate Analytics</div>
        <h1 class="hero-title">Find the value<br>behind the home.</h1>
        <div class="hero-subtitle">
            A machine-learning powered housing valuation tool that estimates
            property prices from key characteristics using an optimized
            Random Forest model.
        </div>
        <div class="status-pill">
            <span class="status-dot"></span>
            Prediction engine ready
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# API CONFIGURATION
# ---------------------------------------------------------
st.markdown(
    """
    <div class="section-heading">Prediction engine</div>
    <div class="section-caption">
        Your property details are securely sent to the deployed prediction API.
    </div>
    """,
    unsafe_allow_html=True,
)

api_url = st.text_input(
    "Prediction API URL",
    value="https://housing-price-prediction-api-8wq8.onrender.com/predict",
    label_visibility="collapsed",
)

st.markdown(
    f"""
    <div class="api-card">
        <div class="api-title">Live API endpoint</div>
        <div class="api-url">{api_url}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# INPUT DEFAULTS
# ---------------------------------------------------------
area = 7420.0
bedrooms = 4
bathrooms = 2
stories = 3
parking = 2

# ---------------------------------------------------------
# PROPERTY DETAILS
# ---------------------------------------------------------
st.markdown(
    """
    <div class="section-heading">Property details</div>
    <div class="section-caption">
        Tell us a little about the property you're evaluating.
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns(2, gap="large")

with left:
    st.markdown(
        '<div class="info-card"><div class="info-label">Property size</div>'
        '<div class="info-value">Core property characteristics</div></div>',
        unsafe_allow_html=True,
    )

    area = st.number_input(
        "Area (sq ft)",
        min_value=100.0,
        value=7420.0,
        step=100.0,
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=20,
        value=4,
        step=1,
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2,
        step=1,
    )

    stories = st.number_input(
        "Stories",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
    )

    parking = st.number_input(
        "Parking spaces",
        min_value=0,
        max_value=10,
        value=2,
        step=1,
    )

with right:
    st.markdown(
        '<div class="info-card"><div class="info-label">Property features</div>'
        '<div class="info-value">Amenities & location indicators</div></div>',
        unsafe_allow_html=True,
    )

    mainroad = st.selectbox(
        "Main road",
        ["yes", "no"],
        index=0,
    )

    guestroom = st.selectbox(
        "Guest room",
        ["yes", "no"],
        index=0,
    )

    basement = st.selectbox(
        "Basement",
        ["yes", "no"],
        index=0,
    )

    hotwaterheating = st.selectbox(
        "Hot water heating",
        ["yes", "no"],
        index=0,
    )

    airconditioning = st.selectbox(
        "Air conditioning",
        ["yes", "no"],
        index=0,
    )

    prefarea = st.selectbox(
        "Preferred area",
        ["yes", "no"],
        index=0,
    )

    furnishingstatus = st.selectbox(
        "Furnishing status",
        ["furnished", "semi-furnished", "unfurnished"],
        index=0,
    )

# ---------------------------------------------------------
# PREDICTION ACTION
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "Estimate Property Value  →",
    type="primary",
)

# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------
if predict:
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

    with st.spinner("Analyzing the property..."):
        try:
            response = requests.post(
                api_url,
                json=payload,
                timeout=90,
            )

            result = response.json()

            if response.ok:
                predicted_price = result["predicted_price"]
                model_name = result.get(
                    "model",
                    "Optimized Random Forest Regressor",
                )

                st.markdown(
                    f"""
                    <div class="prediction-card">
                        <div class="prediction-label">
                            Estimated property value
                        </div>
                        <div class="prediction-price">
                            KES {predicted_price:,.2f}
                        </div>
                        <div class="prediction-model">
                            Powered by {model_name}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # -----------------------------------------
                # PROPERTY SNAPSHOT
                # -----------------------------------------
                st.markdown(
                    """
                    <div class="snapshot">
                        <div class="snapshot-title">
                            Your property snapshot
                        </div>
                    """,
                    unsafe_allow_html=True,
                )

                s1, s2, s3, s4 = st.columns(4)

                with s1:
                    st.markdown(
                        f"""
                        <div class="metric-box">
                            <div class="metric-name">Area</div>
                            <div class="metric-value">{area:,.0f} sq ft</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with s2:
                    st.markdown(
                        f"""
                        <div class="metric-box">
                            <div class="metric-name">Bedrooms</div>
                            <div class="metric-value">{bedrooms}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with s3:
                    st.markdown(
                        f"""
                        <div class="metric-box">
                            <div class="metric-name">Bathrooms</div>
                            <div class="metric-value">{bathrooms}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with s4:
                    st.markdown(
                        f"""
                        <div class="metric-box">
                            <div class="metric-name">Parking</div>
                            <div class="metric-value">{parking} spaces</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                st.markdown("</div>", unsafe_allow_html=True)

            else:
                st.error(
                    result.get(
                        "error",
                        "Prediction request failed.",
                    )
                )

        except requests.RequestException as exc:
            st.error(
                "We couldn't reach the prediction engine. "
                "Please check the API connection and try again."
            )
            st.code(str(exc))

        except (ValueError, KeyError):
            st.error(
                "The API returned an unexpected response. "
                "Please check the deployed API."
            )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        Housing Price Prediction · Week 7 Model Deployment<br>
        Optimized Random Forest Regressor · Flask API · Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)