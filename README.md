# 🌊 Flood Probability Prediction System

A Machine Learning based Flood Risk Prediction System that predicts flood probability using environmental, geographical, and infrastructure-related factors.

The project uses **XGBoost Regression** with a **Flask Web Application** interface to estimate flood probability and classify flood risk.

---

## 📌 Project Overview

Flood prediction is a complex problem influenced by rainfall patterns, drainage conditions, environmental changes, and human activities.

This project uses machine learning to analyze multiple flood-related parameters and generate:

- Flood Probability Percentage
- Flood Risk Classification
  - HIGH FLOOD RISK
  - LOW FLOOD RISK

---

## 🚀 Features

✅ Machine Learning based flood prediction  
✅ XGBoost regression model  
✅ Flask web interface  
✅ Automatic model training  
✅ Data preprocessing using StandardScaler  
✅ Real-time flood probability prediction  
✅ Risk classification system  
✅ User-friendly input form  

---

# 🏗️ Project Structure

```
RISING WATER/

│
├── app.py
├── flood.csv
├── floods.save
├── transform.save
│
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── chance.html
│   └── no_chance.html
│
├── static/
│   └── main.css
│
└── README.md
```

---

# 📊 Dataset Information

Dataset file:

```
flood.csv
```

Target Variable:

```
FloodProbability
```

Input Features:

```
MonsoonIntensity
TopographyDrainage
RiverManagement
Deforestation
Urbanization
ClimateChange
DamsQuality
Siltation
AgriculturalPractices
Encroachments
IneffectiveDisasterPreparedness
DrainageSystems
CoastalVulnerability
Landslides
Watersheds
DeterioratingInfrastructure
PopulationScore
WetlandLoss
InadequatePlanning
PoliticalFactors
```

---

# 🧠 Machine Learning Model

## Algorithm Used

### XGBoost Regression

Why XGBoost?

- Handles complex relationships
- High prediction accuracy
- Works well with structured datasets
- Resistant to overfitting

---

## Data Processing Pipeline

```
CSV Dataset
     |
     |
Feature Selection
     |
     |
Train/Test Split
     |
     |
Standard Scaling
     |
     |
XGBoost Training
     |
     |
Model Export
     |
     |
Flask Prediction API
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>
```

Move into project folder:

```bash
cd RISING-WATER
```

---

## 2. Install Dependencies

Install required libraries:

```bash
pip install flask
pip install pandas
pip install numpy
pip install scikit-learn
pip install xgboost
pip install openpyxl
```

---

# ▶️ Running the Application

Start Flask server:

```bash
python app.py
```

The application will run at:

```
http://127.0.0.1:5000/
```

---

# 🌐 Application Pages

## Home Page

```
/http://127.0.0.1:5000/
```

Displays project introduction.

---

## Prediction Page

```
/Predict
```

Allows users to enter flood parameters.

---

## Prediction Result

The system returns:

Example:

```
Flood Probability: 78.45%

Risk Level:
HIGH FLOOD RISK
```

or

```
Flood Probability: 25.30%

Risk Level:
LOW FLOOD RISK
```

---

# 🧪 Sample Input

Example values:

```
MonsoonIntensity = 8
TopographyDrainage = 6
RiverManagement = 5
Deforestation = 7
Urbanization = 8
ClimateChange = 7
DamsQuality = 5
Siltation = 6
AgriculturalPractices = 5
Encroachments = 8
IneffectiveDisasterPreparedness = 7
DrainageSystems = 6
CoastalVulnerability = 9
Landslides = 4
Watersheds = 5
DeterioratingInfrastructure = 7
PopulationScore = 8
WetlandLoss = 6
InadequatePlanning = 7
PoliticalFactors = 5
```

---

# 💾 Model Files

After training, the system generates:

## Model

```
floods.save
```

Contains the trained XGBoost model.

## Scaler

```
transform.save
```

Contains feature scaling configuration.

---

# 🔄 Retraining the Model

Delete:

```
floods.save
transform.save
```

Run:

```bash
python app.py
```

The system will automatically retrain using:

```
flood.csv
```

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Framework

- Flask

## Machine Learning

- XGBoost
- Scikit-learn

## Data Processing

- Pandas
- NumPy

## Frontend

- HTML
- CSS

---

# 📈 Future Improvements

Possible enhancements:

- Real-time weather API integration
- Satellite rainfall data integration
- GIS flood mapping
- Deep learning models
- Mobile application support
- Live disaster alerts

---

# 👨‍💻 Author

Flood Prediction System Project

---

# 📜 License

This project is developed for educational and research purposes.
