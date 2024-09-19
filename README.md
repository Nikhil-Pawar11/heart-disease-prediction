# Heart Disease Prediction API

This repository contains a Flask-based API that predicts whether a patient is at risk of heart disease based on various health indicators. The prediction is powered by a pre-trained machine learning model.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Input JSON Example](#input-json-example)
- [Response Example](#response-example)
- [Model Information](#model-information)
- [Testing with Postman](#testing-with-postman)
- [Contributing](#contributing)
- [License](#license)

## Overview

This API is designed to help predict the likelihood of heart disease in a patient based on medical and environmental data. It leverages a machine learning model trained on relevant health data to provide predictions in real time.

The application accepts health-related information through a POST request in JSON format and returns whether or not the patient is likely to have heart disease.

## Features
- **Predictive API**: Provides heart disease prediction based on input parameters.
- **Easy to Use**: Send a POST request with patient data to receive predictions.
- **Scalable**: Can be deployed on any platform that supports Flask and Python.
- **Machine Learning Model**: Trained using medical datasets, giving accurate and fast predictions.

## How It Works
1. The API accepts a JSON object containing a patient’s health data.
2. The data is fed into a pre-trained machine learning model.
3. The model predicts whether the patient is likely to have heart disease.
4. The result is returned in a JSON response.

## Tech Stack
- **Backend**: Flask
- **Machine Learning**: Scikit-learn, joblib (for model serialization)
- **Data Processing**: Pandas
- **Environment**: Python 3.8+
- **Dependencies**:
    - Flask
    - Pandas
    - Joblib

## Installation

Follow these steps to run the application locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/Nikhil-Pawar11/heart-disease-prediction.git
    cd heart-disease-prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the pre-trained model: Place the `heart_disease_model.joblib` file in the `model/` directory, or modify the path in `app.py` if the model is stored elsewhere.

5. Run the Flask app:
    ```bash
    flask run
    ```

## Usage

Once the app is running, you can make a POST request to the `/predict` endpoint with patient data in JSON format. Below is an example of how to use the API:

### API Endpoint
- **URL**: `http://127.0.0.1:5000/predict`
- **Method**: POST
- **Content-Type**: `application/json`

### Input JSON Example
```json
{
  "Age": 60,
  "RestingBP": 120,
  "Cholesterol": 180,
  "FastingBS": 0,
  "MaxHR": 180,
  "Oldpeak": 0.0,
  "Sex_F": 1.0,
  "Sex_M": 0.0,
  "ChestPainType_ASY": 0.0,
  "ChestPainType_ATA": 1.0,
  "ChestPainType_NAP": 0.0,
  "ChestPainType_TA": 0.0,
  "RestingECG_LVH": 0.0,
  "RestingECG_Normal": 1.0,
  "RestingECG_ST": 0.0,
  "ExerciseAngina_N": 1.0,
  "ExerciseAngina_Y": 0.0,
  "ST_Slope_Down": 0.0,
  "ST_Slope_Flat": 0.0,
  "ST_Slope_Up": 1.0,
  "Temp": 25.0,
  "NO2_Mean": 20.0,
  "O3_Mean": 0.01,
  "SO2_Mean": 1.0,
  "CO_Mean": 0.4
}
```
## Response Example
The API returns a prediction in the following format:

```json
{
  "prediction": "Heart Disease"
}
```
## Possible values for prediction:

- **"Heart Disease"**: The model predicts that the patient is likely to have heart disease.
- **"No Heart Disease"**: The model predicts that the patient is unlikely to have heart disease.

## Model Information
The machine learning model used for this prediction is a binary classifier, trained on a heart disease dataset. It considers various medical and environmental factors to make a prediction. The model is stored in the `heart_disease_model.joblib` file, which is loaded at runtime.

### Features Used by the Model:

- **Age**: The age of the patient, which is a significant risk factor for heart disease. Older individuals typically have a higher risk.

- **RestingBP (Resting Blood Pressure)**: The blood pressure measured when the patient is at rest. High resting blood pressure can indicate cardiovascular issues.

- **Cholesterol**: The total cholesterol level in the blood. High cholesterol levels are associated with an increased risk of heart disease.

- **FastingBS (Fasting Blood Sugar)**: Indicates whether the patient's fasting blood sugar is greater than 120 mg/dl. High fasting blood sugar can be a risk factor for diabetes, which is related to heart disease.

- **MaxHR (Maximum Heart Rate)**: The maximum heart rate achieved during exercise. A lower maximum heart rate can indicate potential heart problems.

- **Oldpeak**: The difference in ST segment from rest to exercise, measured in mm. It reflects the presence of ischemia; higher values can indicate heart disease.

- **Sex_F (Female)**: A binary variable indicating if the patient is female (1.0 if female, 0.0 otherwise). Gender is a factor in heart disease risk.

- **Sex_M (Male)**: A binary variable indicating if the patient is male (1.0 if male, 0.0 otherwise). Like sex_F, it affects risk assessment.

- **ChestPainType_ASY (Atypical Angina)**: Indicates the presence of atypical angina (1.0 if present, 0.0 otherwise). Atypical angina can suggest a higher risk of heart issues.

- **ChestPainType_ATA (Typical Angina)**: Indicates the presence of typical angina (1.0 if present, 0.0 otherwise). This type is a classic indicator of heart disease.

- **ChestPainType_NAP (Non-Anginal Pain)**: Indicates if the patient experiences non-anginal pain (1.0 if present, 0.0 otherwise). Non-anginal pain generally indicates a lower risk.

- **ChestPainType_TA (Tachycardia)**: Indicates the presence of tachycardia (1.0 if present, 0.0 otherwise). This can be a sign of underlying heart issues.

- **RestingECG_LVH (Left Ventricular Hypertrophy)**: Indicates the presence of left ventricular hypertrophy (1.0 if present, 0.0 otherwise). This is an abnormality that can be linked to heart disease.

- **RestingECG_Normal**: Indicates if the resting electrocardiogram shows normal results (1.0 if normal, 0.0 otherwise). Normal results suggest a lower risk of heart issues.

- **RestingECG_ST (ST-T Wave Abnormality)**: Indicates the presence of ST-T wave abnormalities (1.0 if present, 0.0 otherwise). Such abnormalities can indicate heart problems.

- **ExerciseAngina_N (No Exercise Angina)**: Indicates whether the patient experiences angina during exercise (1.0 if no angina, 0.0 if yes). The absence of angina is generally a positive sign.

- **ExerciseAngina_Y (Yes Exercise Angina)**: Indicates whether the patient experiences angina during exercise (1.0 if yes, 0.0 if no). The presence of angina can indicate a higher risk.

- **ST_Slope_Down**: Indicates the slope of the ST segment during exercise (1.0 if downsloping, 0.0 otherwise). A downsloping ST segment can be associated with heart disease.

- **ST_Slope_Flat**: Indicates if the ST segment is flat (1.0 if flat, 0.0 otherwise). A flat ST segment suggests a stable condition.

- **ST_Slope_Up**: Indicates if the ST segment is upsloping (1.0 if upsloping, 0.0 otherwise). An upsloping ST segment is generally considered a favorable finding.

- **Temp**: The temperature during the test, which can affect cardiovascular function. While not a direct risk factor, it can provide context.

- **NO2_Mean**: The average nitrogen dioxide level, which is an air pollutant. High levels can be associated with cardiovascular diseases.

- **O3_Mean**: The average ozone level, which can also impact cardiovascular health, particularly in individuals with pre-existing conditions.

- **SO2_Mean**: The average sulfur dioxide level. Similar to NO2 and O3, elevated SO2 can have adverse effects on heart health.

- **CO_Mean**: The average carbon monoxide level. High levels can impair oxygen delivery in the blood, potentially affecting heart health.


## Testing with Postman
1. Open Postman and set the method to `POST`.

2. Enter the URL `http://127.0.0.1:5000/predict`.

3. Set the **Content-Type** header to `application/json`.

4. In the **Body** tab, choose `raw` and paste the example JSON:

   ```json
   {
     "Age": 60,
     "RestingBP": 120,
     "Cholesterol": 180,
     "FastingBS": 0,
     "MaxHR": 180,
     "Oldpeak": 0.0,
     "Sex_F": 1.0,
     "Sex_M": 0.0,
     "ChestPainType_ASY": 0.0,
     "ChestPainType_ATA": 1.0,
     "ChestPainType_NAP": 0.0,
     "ChestPainType_TA": 0.0,
     "RestingECG_LVH": 0.0,
     "RestingECG_Normal": 1.0,
     "RestingECG_ST": 0.0,
     "ExerciseAngina_N": 1.0,
     "ExerciseAngina_Y": 0.0,
     "ST_Slope_Down": 0.0,
     "ST_Slope_Flat": 0.0,
     "ST_Slope_Up": 1.0,
     "Temp": 25.0,
     "NO2_Mean": 20.0,
     "O3_Mean": 0.01,
     "SO2_Mean": 1.0,
     "CO_Mean": 0.4
   }

5. Click Send. You should receive a JSON response with the prediction.
    ```json
    {
        "prediction": "Heart Disease"
    }
## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

### To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request detailing your changes.
