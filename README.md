# Real Estate House Price Prediction - Chennai

This project provides a machine learning model that predicts house prices in Chennai based on various factors, including location, size, amenities, and historical price trends. The solution is packaged as a Flask web application and deployed using Docker.

## Features
- **Accurate House Price Predictions**: Leverages a regression model fine-tuned for the Chennai real estate market.
- **User-Friendly Interface**: Accessible through a web application built with Flask.
- **Containerized Deployment**: Uses Docker for easy and consistent deployment.
- **Scalable Hosting**: Deployed on Render for seamless access.

## Project Structure
```
.
├── Dockerfile               # Docker configuration file
├── README.md                # Project documentation
├── Real_Estate_House_Price_Prediction1.ipynb # Jupyter notebook for model training
├── app.py                   # Flask application
├── model1.pkl               # Trained regression model
├── requirements.txt         # Python dependencies
└── templates/               # HTML templates for the web app
```


### Prerequisites
- Python 3.x
- Docker
- Render account (for deployment)

### Data Exploration and Cleaning:
1. **Initial Data Load**: The dataset is loaded using Pandas. Basic inspection includes shape and a preview of the data.
2. **Missing Values**: Analysis of missing values and different strategies to handle them:
   - Filling using mode and mean.
   - Using auxiliary columns for intelligent imputation.
3. **Data Cleaning**:
   - Dropping duplicates.
   - Replacing erroneous and inconsistent values.
   - Converting data types and handling categorical variables.
4. **Exploratory Data Analysis (EDA)**:
   - **Univariate Analysis**: Histograms and bar plots for various features like `INT_SQFT`, `N_BEDROOM`, and `N_BATHROOM`.
   - **Bivariate Analysis**: Scatter plots to examine relationships between features like `INT_SQFT` and `SALES_PRICE`.
   - Group-wise aggregation and visualization for categorical features.

### Data Transformation:
- One-hot encoding is applied to categorical features for model compatibility.

### Model Building and Evaluation:
1. **Model Training**:
   - It's uses Regression Based Models for Training
2. **Performance Metrics**:
   - The notebook calculates the Root Mean Squared Error (RMSE) and R-squared to evaluate the model.
3. **Model Serialization**:
   - The model is saved using `pickle` and `joblib`.

Would you like me to expand the README to include this detailed process?

### Local Development
1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd Real-Estate-House-Price-Prediction_MLOPS-main
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**:
   ```bash
   python app.py
   ```

4. **Access the app**:  
   Visit `http://127.0.0.1:5000` in your browser.

### Docker Deployment
1. **Build the Docker image**:
   ```bash
   docker build -t house-price-prediction .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 house-price-prediction
   ```

### Deployment on Render
1. Create a new web service on Render.
2. Connect your repository and specify the Dockerfile for deployment.

### Demonstration
![image](https://github.com/user-attachments/assets/30cb72cf-1cf0-42eb-bf6a-be4a88c06fc7)


## Usage
1. Enter the required details (location, size, amenities) on the web interface.
2. Click "Predict" to get the estimated house price.

## Model Information
The regression model was trained using historical data and fine-tuned to account for location-specific trends in Chennai's real estate market.


---
