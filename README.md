![Image](https://github.com/user-attachments/assets/3c0db88b-d974-474e-9c89-38fc151618d2)
# Real Estate Price Prediction Website

This repository showcases a real estate price prediction project that I built from scratch. It walks through the complete data science workflow—from building a machine learning model to deploying it with a user-friendly web interface.
The model predicts housing prices in Bangalore, based on parameters such as area (in square feet), number of bedrooms, and location. It uses a dataset sourced from Kaggle.

 ## Project Structure

**1. Model Building with Scikit-Learn**

Dataset: Bangalore Home Prices (from Kaggle)

Process:

- Data loading and preprocessing

- Outlier detection and removal

- Feature engineering

- Dimensionality reduction

- Model training using Linear Regression

- GridSearchCV for hyperparameter tuning

- K-Fold Cross Validation for performance evaluation

**2. Backend API with Flask**

- Built a Flask server to serve the trained ML model

- The server exposes a REST API that takes user inputs (square feet, location, BHK) and returns the predicted price

- Model is serialized using joblib for efficient loading

**3. Frontend UI**

Developed a website using HTML, CSS, and JavaScript

The interface allows users to:

- Select the location

- Enter the square footage and number of bedrooms

- Click a button to get the predicted home price

The UI makes an API call to the Flask backend and displays the result dynamically

## Technologies Used

- Python

- Pandas, NumPy

- Matplotlib

- Scikit-learn

- Flask

- HTML / CSS / JavaScript

- Jupyter Notebook

- VS Code 
