# 🚀 AI-Based Supply Chain Demand Forecasting & Inventory Optimization Platform

# 📌 Project Overview

The **AI-Based Supply Chain Demand Forecasting & Inventory Optimization Platform** is a machine learning powered web application that helps businesses predict future product demand and manage inventory efficiently.

Demand forecasting is one of the most important challenges in supply chain management. Incorrect demand estimation can lead to:

* 📉 **Stockouts** (products unavailable when customers need them)
* 📦 **Overstocking** (extra inventory leading to higher storage cost)
* 💰 **Financial losses**

This system solves these problems using **Machine Learning models** that analyze historical sales data and forecast demand for upcoming months.

The predictions are displayed through a **Flask-based dashboard** which provides useful insights about inventory levels and product demand.

---

# 🎯 Objectives

The main objectives of this project are:

* Predict future product demand using Machine Learning
* Reduce inventory management errors
* Provide a visual dashboard for supply chain insights
* Demonstrate the practical application of AI in business operations

---

# 👨‍💻 Team Information

**Group Number:** 75

### Team Members        
| Vanshika Kushwah
| Upasana Porwal    

**Course:** B.Tech Computer Science (AI & ML)
**Year:** 2nd Year
**Section:** 2B

---

# ✨ Key Features

✔ AI-based demand forecasting
✔ Inventory monitoring dashboard
✔ Machine Learning model integration
✔ Prediction of next month demand
✔ Low stock detection system
✔ Inventory summary reporting
✔ Flask-based backend server
✔ Web-based dashboard interface

---

# 🧠 Machine Learning Component

The system uses a **machine learning regression model** trained on historical sales data.

### ML Workflow

1. Load historical sales dataset
2. Perform data preprocessing
3. Train a regression model using Scikit-learn
4. Save the trained model using Pickle
5. Load the model during runtime
6. Predict next month's demand

---

# ⚙️ System Workflow

```
Dataset
   ↓
Data Cleaning & Preprocessing
   ↓
Model Training
(train_model.py)
   ↓
Trained Model Saved
(saved_model.pkl)
   ↓
Prediction Module
(predict.py)
   ↓
Flask Backend
(app.py)
   ↓
Web Dashboard
(dashboard.html)
```

---

# 🏗 System Architecture

```
User
 ↓
Web Browser
 ↓
Flask Application
 ↓
Prediction Module
 ↓
Machine Learning Model
 ↓
Demand Prediction
 ↓
Dashboard Display
```

---

# 🛠 Technology Stack

## Programming Languages

* Python
* HTML
* CSS

## Frameworks & Libraries

* Flask
* Pandas
* NumPy
* Scikit-learn
* Pickle

## Tools

* Git
* GitHub
* VS Code

---

# 📂 Project Structure

```
miniProject
│
├── .github
│
├── backend
│   │
│   ├── __pycache__
│   │   ├── config.cpython-312.pyc
│   │   └── extensions.cpython-312.pyc
│   │
│   ├── data
│   │   └── sales_data_sample.csv
│   │
│   ├── ml
│   │   └── prophet_model.py
│   │
│   ├── models
│   │   ├── __init__.py
│   │   ├── predict.py
│   │   ├── train_model.py
│   │   └── user.py
│   │
│   ├── routes
│   │   ├── auth_routes.py
│   │   ├── dashboard_routes.py
│   │   ├── forecast_routes.py
│   │   └── inventory_routes.py
│   │
│   ├── services
│   │   ├── forecast_service.py
│   │   └── inventory_service.py
│   │
│   ├── static
│   │   │
│   │   ├── css
│   │   │   ├── dashboard.css
│   │   │   ├── forecast.css
│   │   │   ├── home.css
│   │   │   ├── inventory.css
│   │   │   └── login.css
│   │   │
│   │   └── js
│   │       ├── chart.js
│   │       ├── dashboard.js
│   │       ├── forecast.js
│   │       ├── home.js
│   │       ├── inventory.js
│   │       └── login.js
│   │
│   ├── templates
│   │   ├── dashboard.html
│   │   ├── forecast.html
│   │   ├── home.html
│   │   ├── inventory.html
│   │   └── login.html
│   │
│   ├── .env
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── extensions.py
│   ├── models.py
│   ├── requirements.txt
│   │
│   ├── sales.db
│   ├── sales_data_sample.csv
│   └── .gitignore
│
└── README.md
```

---

# 📊 Dashboard Preview
```
Dashboard showing:
• Predicted Demand
• Inventory Status
• Low Stock Alerts
• Inventory Summary
```

---

# ▶️ Installation & Setup Guide

Follow these steps to run the project locally.

## 1️⃣ Clone the repository

```
git clone https://github.com/upasana-dot/miniProject.git
```

## 2️⃣ Navigate to project directory

```
cd miniProject
```

## 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

## 4️⃣ Train the machine learning model

```
python backend/models/train_model.py
```

This will generate:

```
saved_model.pkl
```

## 5️⃣ Run the Flask server

```
python backend/app.py
```

## 6️⃣ Open the dashboard

Open the browser and visit:

```
http://127.0.0.1:5006/dashboard
```

---

# 📈 Future Improvements

Some features that can improve this project further:

* Real-time demand forecasting
* Multi-product prediction models
* Advanced analytics dashboard
* Secure authentication system
* Cloud deployment (AWS / Azure / GCP)
* API integration with ERP systems

---

# 👥 Contributors

Thanks to all contributors who worked on this project.

| Contributor      |
| ---------------- |
| Vanshika Kushwah |
| Upasana Porwal   |

---

# 📜 License

This project is developed for **academic purposes** as a Mini Project for **B.Tech Computer Science (AI & ML)**.

---

