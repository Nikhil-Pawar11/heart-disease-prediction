from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model from local storage
model = joblib.load(r'C:\Users\Nikhil\Documents\Heart disease\model\heart_disease_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Convert input data to DataFrame
    df = pd.DataFrame([data])
    
    # Make prediction
    prediction = model.predict(df)
    
    # Return result
    result = 'Heart Disease' if prediction[0] == 1 else 'No Heart Disease'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
