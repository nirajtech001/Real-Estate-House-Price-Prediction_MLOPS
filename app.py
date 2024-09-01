from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load your model (ensure your model file is in the same directory or provide the correct path)
regmodel = pickle.load(open('model1.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('home.html')

# Define the categorical attribute names and the possible values for each
categorical_attributes = {
    'N_BEDROOM': [1, 2, 3, 4],
    'N_BATHROOM': [1, 2],
    'N_ROOM': [2, 3, 4, 5, 6],
    'AREA': ['AREA_Adyar', 'AREA_Anna_Nagar', 'AREA_Chrompet', 'AREA_KK_Nagar', 'AREA_Karapakkam', 'AREA_T_Nagar', 'AREA_Velachery'],
    'SALE_COND': ['SALE_COND_AbNormal', 'SALE_COND_AdjLand', 'SALE_COND_Family', 'SALE_COND_Normal_Sale', 'SALE_COND_Partial'],
    'PARK_FACIL': ['PARK_FACIL_No', 'PARK_FACIL_Yes'],
    'BUILDTYPE': ['BUILDTYPE_Commercial', 'BUILDTYPE_House', 'BUILDTYPE_Others'],
    'UTILITY_AVAIL': ['UTILITY_AVAIL_AllPub', 'UTILITY_AVAIL_ELO', 'UTILITY_AVAIL_NoSeWa', 'UTILITY_AVAIL_NoSewr'],
    'STREET': ['STREET_Gravel', 'STREET_No_Access', 'STREET_Paved'],
    'MZZONE': ['MZZONE_A', 'MZZONE_C', 'MZZONE_I', 'MZZONE_RH', 'MZZONE_RL', 'MZZONE_RM']
}

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    form_data = request.form.to_dict()

    # Separate numerical and categorical data
    numerical_data = {}
    categorical_data = {}

    for key, value in form_data.items():
        if key in categorical_attributes:
            categorical_data[key] = value
        else:
            numerical_data[key] = float(value)

    # Perform one-hot encoding on categorical data
    encoded_data = []

    for key, values in categorical_attributes.items():
        for val in values:
            encoded_data.append(1 if categorical_data.get(key) == val else 0)

    # Combine numerical data and encoded categorical data
    final_data = np.array(list(numerical_data.values()) + encoded_data).reshape(1, -1)

    # Make the prediction using the model
    output = regmodel.predict(final_data)[0]

    # Render the result on the home page
    return render_template("home.html", prediction_text=f"Predicted Price: {output:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
