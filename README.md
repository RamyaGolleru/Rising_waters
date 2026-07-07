# Rising waters
## 📌 Project Overview

Floods are among the most devastating natural disasters, causing significant loss of life, property damage, and displacement every year. Traditional flood forecasting methods often fail to provide timely and accurate predictions, limiting the ability of authorities to take preventive action.

This project develops a **Machine Learning-based Flood Prediction System** that analyzes historical weather data to predict the likelihood of flood occurrences. The system is trained using multiple supervised learning algorithms, and the best-performing model is integrated into a **Flask web application** for real-time flood risk prediction.

The application is designed for future deployment on **IBM Cloud**, making it scalable and accessible from anywhere.

---

## 🎯 Objectives

- Predict flood occurrence using historical weather data.
- Compare the performance of multiple machine learning algorithms.
- Deploy the best-performing model in a user-friendly Flask web application.
- Assist disaster management teams in early flood warning and resource planning.

---

## 🚀 Features

- Predicts flood risk based on weather parameters.
- Uses multiple machine learning algorithms for comparison.
- Interactive web interface built with Flask.
- High prediction accuracy using XGBoost.
- Ready for IBM Cloud deployment.
- Easy-to-use interface for authorities and disaster management teams.

---

## 🛠 Technologies Used

### Programming Language
- Python 3.8+

### Machine Learning Libraries
- NumPy
- Pandas
- Scikit-learn
- XGBoost
- PyTorch

### Data Visualization
- Matplotlib

### Web Development
- Flask
- HTML
- CSS
- JavaScript

### Deployment
- IBM Cloud

---

## 🤖 Machine Learning Algorithms

The following algorithms were trained and evaluated:

- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- XGBoost Classifier

### Best Model

✅ **XGBoost**

**Accuracy:** **96.55%**

The trained XGBoost model is saved and used by the Flask web application for flood prediction.

---

## 📊 Dataset Features

The model is trained using historical weather data containing features such as:

- Annual Rainfall
- Cloud Visibility
- Seasonal Rainfall
- Temperature
- Humidity
- Weather Patterns
- Flood Occurrence (Target)

---

## 💻 Project Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Best Model Selection
7. Model Saving
8. Flask Web Application
9. IBM Cloud Deployment

---

## 📂 Project Structure

```
Flood-Prediction/
│
├── dataset/
│   └── flood_data.csv
│
├── models/
│   └── xgboost_model.pkl
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📖 Use Cases

### Scenario 1: Early Flood Warning

A meteorologist enters rainfall and cloud visibility data for a flood-prone district. The model predicts a high flood probability, enabling authorities to issue evacuation alerts in advance.

---

### Scenario 2: Disaster Response

Disaster management officials monitor multiple regions during monsoon season. The system instantly classifies flood risk levels, helping prioritize rescue teams and relief resources.

---

### Scenario 3: Model Validation

Government analysts evaluate the trained model using historical flood data. The XGBoost classifier achieves **96.55% accuracy**, demonstrating reliable performance.

---

## ⚙ Hardware Requirements

- Intel Core i3 Processor or above
- Minimum 4 GB RAM
- Minimum 2 GB Free Storage
- Internet Connection

---

## 💾 Software Requirements

- Windows / Linux / macOS
- Python 3.8+
- Anaconda Navigator or Jupyter Notebook
- Flask Framework
- HTML
- CSS
- JavaScript
- IBM Cloud Account

---

## 📥 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/flood-prediction.git
```

### Navigate to the Project Folder

```bash
cd flood-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📈 Model Performance

| Algorithm | Accuracy |
|-----------|----------|
| Decision Tree | Evaluated |
| Random Forest | Evaluated |
| K-Nearest Neighbors | Evaluated |
| **XGBoost** | **96.55%** |

---

## 👥 Team Members

| Name | Role |
|------|------|
| Vutukuri Naga Sravani | Team Lead |
| Ramya Golleru | Member |
| Jaldula Neeraja | Member |
| Doma Charan Teja | Member |
| Kuuchimanchi Aditya Sai Vamsi Krishna | Member |

---

## 🧑‍💻 Skills Required

- Machine Learning
- Supervised Learning
- Decision Trees
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost
- NumPy
- Matplotlib
- Scikit-learn
- PyTorch
- Flask
- HTML
- CSS
- JavaScript

---

## ☁ Future Enhancements

- Real-time weather API integration
- Live flood alerts
- GIS-based flood visualization
- SMS and Email notifications
- Mobile application support
- IoT sensor integration

---

## 📜 License

This project is developed for educational and research purposes.

---

## 🙏 Acknowledgements

- IBM SkillsBuild
- Scikit-learn
- XGBoost
- Flask
- Python Community

---

**Developed by Team –Rising waters**
