import streamlit as st
import pickle
import pandas as pd

# Page settings
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Load model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.result {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="title">🏠 House Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered house price estimation using Machine Learning</div>',
    unsafe_allow_html=True
)

st.divider()

# Input section
st.subheader("🏡 Enter House Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "📐 Area (sq ft)",
        min_value=100,
        max_value=10000,
        value=1500,
        step=100
    )

    bedrooms = st.number_input(
        "🛏️ Bedrooms",
        min_value=1,
        max_value=10,
        value=3
    )

with col2:
    bathrooms = st.number_input(
        "🛁 Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )

    parking = st.number_input(
        "🚗 Parking Spaces",
        min_value=0,
        max_value=10,
        value=1
    )

st.divider()

# Prediction
if st.button("🔮 Predict House Price", use_container_width=True):

    input_data = pd.DataFrame(
        [[area, bedrooms, bathrooms, parking]],
        columns=["area", "bedrooms", "bathrooms", "parking"]
    )

    prediction = model.predict(input_data)[0]

    st.success("Prediction completed successfully!")

    st.markdown(
        f"""
        <div class="result">
        💰 Estimated House Price<br><br>
        ₹{prediction:,.0f}
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# About section
st.subheader("🤖 About This Project")

st.write(
    "This project uses Machine Learning to estimate house prices "
    "based on area, number of bedrooms, bathrooms and parking spaces."
)

st.caption("Built with Python • Pandas • Scikit-learn • Streamlit")