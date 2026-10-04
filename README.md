🏠 House Price Prediction

A Machine Learning project that predicts the estimated price of a house based on its area, number of bedrooms, bathrooms, and parking spaces.

🚀 Project Overview

The House Price Prediction system uses Machine Learning regression algorithms to estimate house prices from property features.

The project compares two Machine Learning models:

- 📈 Linear Regression
- 🌳 Random Forest Regression

The trained Random Forest model is used in the Streamlit web application for house price prediction.

✨ Features

- 🏠 House price prediction
- 📐 Area-based prediction
- 🛏️ Bedroom input
- 🛁 Bathroom input
- 🚗 Parking space input
- 📈 Linear Regression model
- 🌳 Random Forest Regression model
- 📊 Model accuracy comparison
- 🖥️ Interactive Streamlit web interface

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

📂 Project Structure

House_Price_prediction/
│
├── house_data.csv
├── generate_dataset.py
├── train_model.py
├── house_price_model.pkl
├── app.py
└── README.md

🧠 Machine Learning Workflow

House Dataset
      ↓
Data Preparation
      ↓
Train/Test Split
      ↓
Linear Regression
      ↓
Random Forest Regression
      ↓
Model Comparison
      ↓
Best Model
      ↓
House Price Prediction

📊 Dataset

The project uses a synthetic dataset containing house information such as:

Feature| Description
area| House area in square feet
bedrooms| Number of bedrooms
bathrooms| Number of bathrooms
parking| Number of parking spaces
price| House price

The dataset contains 1000 generated records for demonstration and learning purposes.

«Note: This is a synthetic/demo dataset and should not be considered real-world property-market data.»

🤖 Models

1. Linear Regression

Linear Regression is used as a baseline regression model to predict house prices based on the input features.

2. Random Forest Regression

Random Forest Regression combines multiple decision trees to make predictions.

In this project, Random Forest produced better results on the generated dataset and is therefore used by the Streamlit application.

💻 Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project directory:

cd House_Price_prediction

Install the required libraries:

pip install pandas numpy scikit-learn streamlit

▶️ Run the Project

First, train the Machine Learning models:

python train_model.py

Then start the Streamlit application:

streamlit run app.py

The application will open in your browser.

🖥️ How to Use

1. Enter the house area in square feet.
2. Enter the number of bedrooms.
3. Enter the number of bathrooms.
4. Enter the number of parking spaces.
5. Click Predict House Price.
6. The application displays the estimated house price.

📌 Example

Example input:

Area: 2000 sq ft
Bedrooms: 3
Bathrooms: 2
Parking: 2

The trained Machine Learning model will generate an estimated house price based on these features.

⚠️ Disclaimer

This project is created for educational and demonstration purposes.

The dataset is synthetically generated, so the predictions should not be used for actual real-estate buying, selling, or financial decisions.

🔮 Future Improvements

- Use a real-world house price dataset
- Add location as a feature
- Add property age
- Add furnishing information
- Add graphical data analysis
- Compare more Machine Learning algorithms
- Improve the Streamlit UI
- Deploy the application online

👨‍💻 Project

House Price Prediction using Machine Learning

Built with ❤️ using Python and Machine Learning.
