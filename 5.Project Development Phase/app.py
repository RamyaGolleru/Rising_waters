import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for

# Machine Learning Ecosystem Imports
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import xgboost as xgb

# =====================================================================
# 🧠 PHASE 1 & 2: AUTOMATED TRAINING & LEADERBOARD PIPELINE
# =====================================================================

def train_and_export_pipeline(data_path='flood dataset.xlsx'):
    print("==========================================================")
    print("🤖 CORE ENGINE: INITIALIZING MODEL TRAINING & EXPORT")
    print("==========================================================\n")
    
    # Check if real data exists, otherwise create temporary mock data
    if not os.path.exists(data_path):
        print(f"⚠️ Warning: '{data_path}' not found. Generating mock training data...")
        mock_data = {
            'ANNUAL': np.random.uniform(500, 3000, 500),
            'Cloud_Density_Level': np.random.choice(['Low', 'Medium', 'High'], 500),
            'Jun-Sep': np.random.uniform(200, 1500, 500),
            'Humidity': np.random.uniform(40, 95, 500),
            'Temperature': np.random.uniform(15, 42, 500),
            'Flood': np.random.choice([0, 1], 500, p=[0.7, 0.3])
        }
        df = pd.DataFrame(mock_data)
    else:
        df = pd.read_excel(data_path)

    # Ordinal Categorical Encoding
    ordinal_col = 'Cloud_Density_Level'
    if ordinal_col in df.columns:
        custom_map = {'Low': 0, 'Medium': 1, 'High': 2}
        df[ordinal_col] = df[ordinal_col].map(custom_map)
    
    # Generic Categorical Encoding
    categorical_cols = df.select_dtypes(exclude=['number']).columns.tolist()
    if categorical_cols:
        le = LabelEncoder()
        for col in categorical_cols:
            df[col] = le.fit_transform(df[col].astype(str))

    # Features (X) and Target (y) Isolation
    target_column = 'Flood'
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Stratified Train-Test Split (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Export fitted scaler configuration
    joblib.dump(scaler, 'transform.save')
    print("   ✅ Configuration Saved: 'transform.save' generated.")

    # Train Models for Leaderboard Benchmarking
    dt = DecisionTreeClassifier(random_state=42).fit(X_train_scaled, y_train)
    dt_acc = accuracy_score(y_test, dt.predict(X_test_scaled))

    rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train_scaled, y_train)
    rf_acc = accuracy_score(y_test, rf.predict(X_test_scaled))

    knn = KNeighborsClassifier(n_neighbors=5).fit(X_train_scaled, y_train)
    knn_acc = accuracy_score(y_test, knn.predict(X_test_scaled))

    xg_mod = xgb.XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42, eval_metric='logloss')
    xg_mod.fit(X_train_scaled, y_train)
    xgb_acc = accuracy_score(y_test, xg_mod.predict(X_test_scaled))

    # Leaderboard Display
    print("\n📊 MACHINE LEARNING LEADERBOARD PERFORMANCE RESULTS:")
    print(f"   - Decision Tree Accuracy:      {dt_acc * 100:.2f}%")
    print(f"   - Random Forest Accuracy:      {rf_acc * 100:.2f}%")
    print(f"   - K-Nearest Neighbors Acc:     {knn_acc * 100:.2f}%")
    print(f"   - XGBoost Classifier Acc:      {xgb_acc * 100:.2f}%")
    
    # Export XGBoost as the operational model architecture weights
    joblib.dump(xg_mod, 'floods.save')
    print("\n   ✅ Algorithm Weights Saved: 'floods.save' generated using XGBoost.")
    print("==========================================================\n")

# Run compilation step once to ensure '.save' files exist before starting server
train_and_export_pipeline()


# =====================================================================
# 🌐 PHASE 3: INTEGRATED FLASK INTERFACE ENVIRONMENT
# =====================================================================

app = Flask(__name__)

# Load saved deployment assets into memory
runtime_scaler = joblib.load('transform.save')
runtime_model = joblib.load('floods.save')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Predict')
def predict_form():
    return render_template('index.html')

@app.route('/chance')
def chance():
    return render_template('chance.html')

@app.route('/no_chance')
def no_chance():
    return render_template('no_chance.html')

@app.route('/predict_action', methods=['POST'])
def predict():
    try:
        # Extract the 5 explicit numerical features from user form submission
        f1 = float(request.form['feature_annual'])
        f2 = float(request.form['feature_visibility'])
        f3 = float(request.form['feature_monsoon'])
        f4 = float(request.form['feature_humidity'])
        f5 = float(request.form['feature_temperature'])
        
        # Structure into a 5-column Pandas DataFrame matching original feature order
        col_headers = ['ANNUAL', 'Cloud Visibility', 'Jun-Sep', 'Humidity', 'Temperature']
        live_raw_df = pd.DataFrame([[f1, f2, f3, f4, f5]], columns=col_headers)
        
        # Scale incoming raw metrics using original pipeline properties
        processed_vector = runtime_scaler.transform(live_raw_df)
        
        # Compute binary classification output inference array
        prediction_output = runtime_model.predict(processed_vector)[0]
        
        # Conditional UI layout routing decisions
        if prediction_output == 1:
            return redirect(url_for('chance'))
        else:
            return redirect(url_for('no_chance'))
            
    except Exception as operational_error:
        print(f"❌ System Exception: {str(operational_error)}")
        return render_template('index.html', error_msg=f"Error processing parameters: {str(operational_error)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)