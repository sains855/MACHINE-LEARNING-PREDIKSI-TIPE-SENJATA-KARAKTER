from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load Model, Scaler, dan Label Encoder
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')
le_weapon = joblib.load('label_encoder_weapon.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Mengambil data dari form
        try:
            data = {
                'Lv': float(request.form['Lv']),
                'Rarity': float(request.form['Rarity']),
                'Element_Enc': int(request.form['Element']),
                'Role_Enc': int(request.form['Role']),
                'Ascension_Enc': int(request.form['Ascension']),
                'Base HP': float(request.form['HP']),
                'Base ATK': float(request.form['ATK']),
                'Base DEF': float(request.form['DEF'])
            }
            
            # Ubah ke DataFrame untuk scaling
            df_input = pd.DataFrame([data])
            X_scaled = scaler.transform(df_input)
            
            # Prediksi
            prediction_numeric = model.predict(X_scaled)
            prediction_name = le_weapon.inverse_transform(prediction_numeric)[0]
            
            return render_template('index.html', result=prediction_name)
        except Exception as e:
            return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)