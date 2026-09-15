# 🌱 Smart AgroAssist

> AI-Powered Smart Agriculture Assistant for Crop Recommendation, Plant Disease Detection, Fertilizer Guidance, and Agricultural Assistance.

Smart AgroAssist is an AI-powered agriculture support platform developed using **Django, Machine Learning, Deep Learning, and Generative AI**.

The system helps farmers and agriculture users make better decisions by providing crop recommendations based on soil and environmental conditions, detecting plant diseases from leaf images, providing fertilizer-related guidance, and answering agriculture-related questions through an AI chatbot.

---

## 📌 Project Overview

Agriculture depends heavily on factors such as soil nutrients, temperature, humidity, pH, rainfall, crop health, and timely decision-making.

Traditional agricultural decision-making can be difficult when expert assistance is not immediately available.

**Smart AgroAssist** addresses this problem by combining Machine Learning, Deep Learning, and Generative AI into a single web-based platform.

The system provides four major functionalities:

1. 🌾 Crop Recommendation
2. 🦠 Plant Disease Detection
3. 🌿 Fertilizer Recommendation
4. 🤖 AI Agriculture Chatbot

---

# ✨ Features

## 🌾 1. Crop Recommendation

The Crop Recommendation module recommends a suitable crop based on:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

A **Decision Tree Machine Learning model** is used for prediction.

### Input Example

```text
Nitrogen     : 90
Phosphorus   : 42
Potassium    : 43
Temperature  : 20.8°C
Humidity     : 82%
pH           : 6.5
Rainfall     : 202 mm
### OUTPUT 
Recommended Crop: Rice

2. Plant Disease Detection
Users can upload an image of a plant leaf.

The Deep Learning model analyzes the image and predicts the possible disease.
Leaf Image
    ↓
Image Upload
    ↓
Django Backend
    ↓
MobileNetV2 Deep Learning Model
    ↓
Disease Prediction
    ↓
Top-3 Predictions
    ↓
Disease Information
    ↓
Symptoms + Recommended Actions + Prevention


3. Fertilizer Recommendation
The fertilizer module provides fertilizer-related guidance based on crop and agricultural input information.

It is designed to help users understand suitable fertilizer requirements and improve crop management decisions.

4. AI Agriculture Chatbot
Smart AgroAssist includes an AI-powered agriculture chatbot.

The chatbot uses Google Gemini to answer agriculture-related questions.

Users can ask questions about topics such as:

Crops

Plant diseases

Fertilizers

Soil

Farming practices

Crop management

General agricultural assistance

The chatbot can also understand questions written in Kannada.

Technologies Used
Backend
Python

Django

Django Templates

MySQL

Machine Learning
Scikit-learn

Decision Tree

NumPy

Pandas

Deep Learning
TensorFlow

Keras

MobileNetV2

Transfer Learning

Fine-Tuning

Pillow

Generative AI
Google Gemini API

Google GenAI Python SDK

Frontend
HTML

CSS

JavaScript

Bootstrap / custom styling

Development Tools
Visual Studio Code

Git

GitHub

PowerShell

System Architecture
                         SMART AGROASSIST
                               │
                ┌──────────────┴──────────────┐
                │                             │
             Frontend                     Django Backend
                │                             │
                │              ┌──────────────┼──────────────┐
                │              │              │              │
                │          Crop Model    Disease Model   Gemini AI
                │              │              │              │
                │         Decision Tree   MobileNetV2    Agriculture
                │              │              │           Chatbot
                │              │              │
                └──────────────┴──────────────┴──────────────┘
                               │
                             MySQL
                               │
                         Application Data

Project Structure
smart_agroassist/
│
├── agroapp/
│   ├── migrations/
│   │
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── crop_recommendation.html
│   │   ├── disease_detection.html
│   │   ├── fertilizer.html
│   │   └── ...
│   │
│   ├── disease_service.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── ml_model/
│   ├── crop_data.csv
│   ├── crop_model.pkl
│   │
│   └── disease_model/
│       ├── disease_model_v5.keras
│       ├── class_names_v5.txt
│       ├── disease_evaluation_report_v5.txt
│       └── disease_info.json
│
├── media/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md







