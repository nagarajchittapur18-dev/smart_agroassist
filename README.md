# 🌱 Smart AgroAssist

> **AI-Powered Smart Agriculture Assistant for Crop Recommendation, Plant Disease Detection, Fertilizer Guidance, and Agricultural Assistance.**

Smart AgroAssist is an AI-powered agriculture support platform developed using **Django, Machine Learning, Deep Learning, and Generative AI**.

The system helps farmers and agriculture users make better decisions by providing crop recommendations based on soil and environmental conditions, detecting plant diseases from leaf images, providing fertilizer-related guidance, and answering agriculture-related questions through an AI-powered chatbot.

---

## 📌 Project Overview

Agriculture depends heavily on factors such as **soil nutrients, temperature, humidity, pH, rainfall, crop health, and timely decision-making**.

Traditional agricultural decision-making can be difficult when expert assistance is not immediately available.

**Smart AgroAssist** addresses this problem by combining **Machine Learning, Deep Learning, and Generative AI** into a single web-based platform.

The system provides four major functionalities:

1. 🌾 **Crop Recommendation**
2. 🦠 **Plant Disease Detection**
3. 🌿 **Fertilizer Recommendation**
4. 🤖 **AI Agriculture Chatbot**

---

# ✨ Features

## 🌾 1. Crop Recommendation

The Crop Recommendation module recommends a suitable crop based on soil and environmental conditions.

### Input Parameters

- 🧪 **Nitrogen (N)**
- 🧪 **Phosphorus (P)**
- 🧪 **Potassium (K)**
- 🌡️ **Temperature**
- 💧 **Humidity**
- 🧪 **Soil pH**
- 🌧️ **Rainfall**

The system uses a **Decision Tree Machine Learning algorithm** to predict the most suitable crop.

### Workflow

```text
Soil & Environmental Data
          ↓
     Data Processing
          ↓
    Decision Tree Model
          ↓
     Crop Prediction
          ↓
 Recommended Crop
```

### Example Input

```text
Nitrogen      : 90
Phosphorus    : 42
Potassium     : 43
Temperature   : 20.8 °C
Humidity      : 82 %
Soil pH       : 6.5
Rainfall      : 202 mm
```

### Example Output

```text
Recommended Crop: Rice
```

### Crop Recommendation Model Performance

| Metric | Result |
|---|---:|
| Dataset Records | 2,202 |
| Training Samples | 1,761 |
| Testing Samples | 441 |
| Algorithm | Decision Tree |
| Test Accuracy | **98.87%** |

> The accuracy reported above is based on the project's test dataset.

---

## 🦠 2. Plant Disease Detection

The Plant Disease Detection module allows users to upload a **plant leaf image** and receive an AI-based disease prediction.

The system uses a **MobileNetV2 Deep Learning model with Transfer Learning, Data Augmentation, Class Weighting, and Fine-Tuning**.

### Disease Detection Workflow

```text
Plant Leaf Image
       ↓
   Image Upload
       ↓
   Django Backend
       ↓
   MobileNetV2
       ↓
Disease Prediction
       ↓
    Top-3 Results
       ↓
Disease Information
       ↓
Symptoms + Actions + Prevention
```

The current disease detection model supports **27 plant leaf and disease classes**.

### Prediction Results

The system provides:

- 🔬 Possible Disease
- 🏷️ AI Class
- 🌱 Crop
- 📊 Confidence Score
- 📈 Confidence Level
- ✅ Prediction Status
- 🥇 Top-3 Predictions
- 📖 Disease Description
- 🩺 Symptoms
- 💊 Recommended Actions
- 🛡️ Prevention Methods

### Disease Detection Model

```text
MobileNetV2
     +
Transfer Learning
     +
Data Augmentation
     +
Class Weighting
     +
Fine-Tuning
```

### V5 Model Performance

| Metric | Result |
|---|---:|
| Test Images | 236 |
| Classes | 27 |
| Top-1 Accuracy | **52.97%** |
| Top-3 Accuracy | **76.69%** |
| Macro Precision | **0.54** |
| Macro Recall | **0.52** |
| Macro F1 Score | **0.50** |
| Weighted F1 Score | **0.51** |

### Model Improvement

The disease detection model was developed through multiple experiments.

| Model Version | Top-1 Test Accuracy |
|---|---:|
| V3 - MobileNetV2 | 47.03% |
| V4 - EfficientNetB0 Experiment | 42.37% |
| **V5 - MobileNetV2** | **52.97%** |

The V5 model improved Top-1 test accuracy by approximately **5.94 percentage points** compared with V3.

The V5 model also achieved a **76.69% Top-3 accuracy**, meaning the correct class appeared among the model's three highest-confidence predictions in approximately 76.69% of the test cases.

> ⚠️ **Disclaimer:** Disease predictions are AI-based preliminary indications and should not replace professional agricultural or plant pathology advice.

---

## 🌿 3. Fertilizer Recommendation

The Fertilizer Recommendation module provides fertilizer-related agricultural guidance to help users make better crop-management decisions.

The module is designed to assist users in understanding fertilizer requirements and improving crop management practices.

---

## 🤖 4. AI Agriculture Chatbot

Smart AgroAssist includes an **AI-powered agriculture chatbot** using **Google Gemini**.

Users can ask agriculture-related questions about:

- 🌾 Crops
- 🦠 Plant diseases
- 🌿 Fertilizers
- 🌱 Soil
- 💧 Irrigation
- 🌦️ Farming conditions
- 👨‍🌾 General farming practices
- 🌱 Crop management

The chatbot generates AI-powered responses to support agricultural decision-making.

The chatbot can also understand **Kannada-language queries**.

---

# 🛠️ Technologies Used

## Backend

- Python
- Django
- Django Templates

## Database

- MySQL

## Machine Learning

- Scikit-learn
- Decision Tree
- Pandas
- NumPy

## Deep Learning

- TensorFlow
- Keras
- MobileNetV2
- Transfer Learning
- Fine-Tuning

## Image Processing

- Pillow

## Generative AI

- Google Gemini API
- Google GenAI Python SDK

## Frontend

- HTML
- CSS
- JavaScript

## Development Tools

- Visual Studio Code
- Git
- GitHub
- PowerShell

---

# 🏗️ System Architecture

```text
                         SMART AGROASSIST
                                │
                                ↓
                       Django Web Application
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ↓                 ↓                 ↓
       Crop Recommendation  Disease Detection  AI Chatbot
              │                 │                 │
              ↓                 ↓                 ↓
       Decision Tree        MobileNetV2       Google Gemini
       ML Model             Deep Learning       Generative AI
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ↓
                         Application Results
                                │
                                ↓
                              MySQL
```

---

# 🔬 Machine Learning Methodology

## Crop Recommendation

The Crop Recommendation model uses seven input features:

```text
N
P
K
Temperature
Humidity
pH
Rainfall
```

### Training Pipeline

```text
Crop Recommendation Dataset
            ↓
       Data Cleaning
            ↓
      Feature Selection
            ↓
       Train/Test Split
            ↓
      Decision Tree Model
            ↓
        Model Training
            ↓
       Model Evaluation
            ↓
       crop_model.pkl
```

The trained model is stored as:

```text
ml_model/crop_model.pkl
```

---

# 🧠 Deep Learning Methodology

## Plant Disease Detection

The disease detection system uses **MobileNetV2** as the base architecture.

### Training Pipeline

```text
PlantDoc Dataset
      ↓
Dataset Preparation
      ↓
Class Validation
      ↓
Image Resizing
      ↓
Data Augmentation
      ↓
MobileNetV2
      ↓
Transfer Learning
      ↓
Fine-Tuning
      ↓
Model Evaluation
      ↓
V5 Disease Model
```

### Image Size

```text
224 × 224 pixels
```

### Data Augmentation

The V5 model uses:

- Random Flip
- Random Rotation
- Random Zoom
- Random Translation
- Random Contrast

### Fine-Tuning

The V5 model uses transfer learning with MobileNetV2 and fine-tunes later layers of the network.

Batch Normalization layers are kept frozen during fine-tuning to improve training stability.

---

# 📊 Model Performance Summary

| Model | Algorithm | Dataset/Test Data | Accuracy |
|---|---|---:|---:|
| Crop Recommendation | Decision Tree | 2,202 records | **98.87%** |
| Disease Detection V3 | MobileNetV2 | 236 test images | 47.03% |
| Disease Detection V4 | EfficientNetB0 | 236 test images | 42.37% |
| **Disease Detection V5** | **MobileNetV2** | **236 test images** | **52.97%** |

### Disease Detection V5 Additional Metrics

| Metric | Score |
|---|---:|
| Top-1 Accuracy | **52.97%** |
| Top-3 Accuracy | **76.69%** |
| Macro Precision | **0.54** |
| Macro Recall | **0.52** |
| Macro F1 | **0.50** |
| Weighted F1 | **0.51** |

---

# 📂 Dataset

## Crop Recommendation Dataset

The Crop Recommendation dataset contains the following features:

```text
N
P
K
temperature
humidity
ph
rainfall
label
```

Final dataset size:

```text
2,202 records
```

The trained model uses:

```text
N
P
K
Temperature
Humidity
pH
Rainfall
```

to predict the crop label.

---

## Plant Disease Dataset

The disease detection model was developed using a processed version of the **PlantDoc dataset**.

The project currently uses:

```text
27 classes
```

The original dataset and processed image dataset are intentionally excluded from the GitHub repository through `.gitignore`.

This keeps the repository smaller and avoids uploading the complete image dataset.

---

# 📁 Project Structure

```text
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
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/nagarajchittapur18-dev/smart_agroassist.git
```

## 2. Navigate to the Project

```bash
cd smart_agroassist
```

## 3. Create a Virtual Environment

### Windows

```powershell
python -m venv venv
```

## 4. Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

## 5. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# 🗄️ Database Configuration

Smart AgroAssist uses **MySQL** as the database.

Create the database:

```sql
CREATE DATABASE smart_agroassist_db;
```

Configure the database connection in Django's `settings.py`.

Example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "smart_agroassist_db",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

> ⚠️ **Security:** Never commit your actual database password to GitHub.

---

# 🔐 Gemini API Configuration

The AI Agriculture Chatbot requires a Google Gemini API key.

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
```

The `.env` file is excluded from GitHub using `.gitignore`.

> ⚠️ Never publish your Gemini API key or other credentials in the repository.

---

# ▶️ Running the Application

Run Django migrations:

```powershell
python manage.py makemigrations
```

```powershell
python manage.py migrate
```

Start the development server:

```powershell
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

# 🧪 Testing the Application

## Crop Recommendation

1. Open the Crop Recommendation page.
2. Enter the soil and environmental parameters.
3. Submit the form.
4. View the recommended crop.

## Plant Disease Detection

1. Open the Disease Detection page.
2. Upload a clear plant leaf image.
3. Submit the image.
4. View the predicted disease.
5. Check the confidence score.
6. Review the Top-3 predictions.
7. View symptoms, recommended actions, and prevention information.

## Fertilizer Recommendation

1. Open the Fertilizer Recommendation page.
2. Enter the required agricultural information.
3. Submit the form.
4. View the fertilizer guidance.

## AI Agriculture Chatbot

1. Open the chatbot.
2. Enter an agriculture-related question.
3. Submit the question.
4. Receive an AI-generated response from Gemini.

---

# 📸 Screenshots

Add screenshots of the actual application to showcase the major modules.

Recommended screenshots:

## 🏠 Dashboard

```markdown
![Smart AgroAssist Dashboard](screenshots/dashboard.png)
```

## 🌾 Crop Recommendation

```markdown
![Crop Recommendation](screenshots/crop-recommendation.png)
```

## 🦠 Plant Disease Detection

```markdown
![Plant Disease Detection](screenshots/disease-detection.png)
```

## 🌿 Fertilizer Recommendation

```markdown
![Fertilizer Recommendation](screenshots/fertilizer.png)
```

## 🤖 AI Agriculture Chatbot

```markdown
![AI Agriculture Chatbot](screenshots/chatbot.png)
```

> Create a `screenshots` folder in the project root and place your screenshots inside it.

---

# 🔄 Application Workflow

```text
                              USER
                                │
                                ↓
                       SMART AGROASSIST
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ↓                 ↓                 ↓
       Crop Recommendation  Disease Detection  AI Chatbot
              │                 │                 │
              ↓                 ↓                 ↓
       Soil & Environment    Leaf Image       User Question
              │                 │                 │
              ↓                 ↓                 ↓
       Decision Tree         MobileNetV2      Google Gemini
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ↓
                         AI-Based Results
                                │
                                ↓
                       Agricultural Assistance
```

---

# 🎯 Project Objectives

The main objectives of Smart AgroAssist are:

- 🌾 Develop an AI-powered agriculture assistance platform.
- 🧪 Recommend suitable crops based on soil and environmental parameters.
- 🦠 Detect possible plant diseases from leaf images.
- 🌿 Provide fertilizer-related agricultural guidance.
- 🤖 Integrate Generative AI for agriculture-related question answering.
- 🌐 Provide agricultural assistance through a user-friendly web application.
- 🧠 Demonstrate the practical application of Machine Learning, Deep Learning, and Generative AI in agriculture.

---

# 🚀 Future Enhancements

Future versions of Smart AgroAssist can include:

- 📱 Android and iOS mobile application
- 🌦️ Real-time weather API integration
- 📍 Location-based agricultural recommendations
- 🌱 Additional crop varieties
- 🦠 More plant disease classes
- 🇮🇳 Multilingual agriculture assistant
- 🎙️ Voice-based agricultural assistant
- 📡 IoT-based soil monitoring
- 💧 Smart irrigation recommendations
- 🌾 Crop yield prediction
- 📊 Advanced farmer analytics
- 🔍 Explainable AI for disease predictions
- 👨‍🌾 Agricultural expert verification
- 🌐 Personalized agricultural recommendations

---

# ⚠️ Disclaimer

Smart AgroAssist provides **AI-based predictions and recommendations for educational and decision-support purposes**.

Plant disease predictions are preliminary and should not be considered a replacement for professional agricultural or plant pathology advice.

Users should consult qualified agricultural experts before making important crop-management decisions.

---

# 👨‍💻 Developer

## Nagaraj Chittapur

**MCA Student | AI/ML & Full-Stack Developer**

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Generative AI
- Full-Stack Development
- Python
- Django

---

# 🙏 Acknowledgements

This project was developed using several open-source technologies and resources.

Special thanks to the communities and projects behind:

- Django
- TensorFlow
- Keras
- Scikit-learn
- NumPy
- Pandas
- Pillow
- Google Gemini
- PlantDoc Dataset

---

# 📜 License

This project is developed for **academic, educational, and research purposes**.

The licensing terms and attribution requirements of external datasets and third-party resources should be respected according to their respective licenses.

---

# ⭐ Support

If you find **Smart AgroAssist** useful or interesting, consider giving the repository a ⭐ on GitHub.

Thank you for visiting the project! 🌱
