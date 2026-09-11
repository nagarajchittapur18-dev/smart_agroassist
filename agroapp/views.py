from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# import google as genai
from google.genai import Client
from django.conf import settings

import os
import joblib
import numpy as np
from PIL import Image
from google import genai
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tensorflow.keras.models import load_model

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# =====================================================
# LOAD TEACHABLE MACHINE MODEL
# =====================================================

model = load_model("agroapp/ml_model/keras_model.h5")

# =====================================================
# LOAD LABELS
# =====================================================

with open("agroapp/ml_model/labels.txt", "r") as f:

    class_names = [line.strip() for line in f.readlines()]
# ===============================
# LOGIN VIEW
# ===============================
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:

            login(request, user)
            return redirect("dashboard")

        else:

            return render(request,
                          "login.html",
                          {"error": "Invalid username or password"})

    return render(request, "login.html")


# ===============================
# REGISTER VIEW
# ===============================
def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():

            return render(request,
                          "login.html",
                          {"error": "Username already exists",
                           "show_register": True})

        User.objects.create_user(username=username,
                                 password=password)

        return redirect("login")

    return redirect("login")


# ===============================
# LOGOUT VIEW
# ===============================
def logout_view(request):

    logout(request)
    return redirect("login")


# ===============================
# DASHBOARD VIEW
# ===============================
@login_required
def dashboard_view(request):

    context = {

        "weather": {
            "temp": 28,
            "rain": 20,
            "humidity": 65
        },

        "soil": {
            "ph": 6.5,
            "n": 40,
            "p": 25,
            "k": 30
        },

        "best_crop": "Rice",

        "alerts": [
            "Check irrigation schedule",
            "Fertilizer due tomorrow"
        ]
    }

    return render(request,
                  "dashboard.html",
                  context)


# ===============================
# ML CROP RECOMMENDATION VIEW
# ===============================

@login_required
def crop_recommendation_view(request):

    prediction = None

    if request.method == "POST":

        import joblib
        import os
        from django.conf import settings

        try:

            N = float(request.POST.get("N"))
            P = float(request.POST.get("P"))
            K = float(request.POST.get("K"))
            temperature = float(request.POST.get("temperature"))
            humidity = float(request.POST.get("humidity"))
            ph = float(request.POST.get("ph"))
            rainfall = float(request.POST.get("rainfall"))

            model_path = os.path.join(
                settings.BASE_DIR,
                "ml_model",
                "crop_model.pkl"
            )

            model = joblib.load(model_path)

            prediction = model.predict([[
                N,
                P,
                K,
                temperature,
                humidity,
                ph,
                rainfall
            ]])[0]

        except:

            prediction = "Prediction error. Please check inputs."

    return render(
        request,
        "crop_recommendation.html",
        {"prediction": prediction}
    )

# ===============================
# FERTILIZER RECOMMENDATION VIEW
# ===============================
@login_required
def fertilizer_recommendation_view(request):

    fertilizer_result = None
    recommendation_detail = None

    if request.method == "POST":

        try:

            nitrogen = int(request.POST.get("nitrogen"))
            phosphorus = int(request.POST.get("phosphorus"))
            potassium = int(request.POST.get("potassium"))

            if nitrogen < 40:
                fertilizer_result = "Urea"
                recommendation_detail = "Nitrogen level is low. Apply Urea fertilizer."

            elif phosphorus < 40:
                fertilizer_result = "DAP"
                recommendation_detail = "Phosphorus level is low. Apply DAP fertilizer."

            elif potassium < 40:
                fertilizer_result = "MOP"
                recommendation_detail = "Potassium level is low. Apply MOP fertilizer."

            else:
                fertilizer_result = "Balanced Soil"
                recommendation_detail = "Your soil nutrients are balanced. No fertilizer required now."

        except:

            fertilizer_result = "Invalid input"
            recommendation_detail = "Please enter valid numeric values."

    return render(
        request,
        "fertilizer_recommendation.html",
        {
            "fertilizer_result": fertilizer_result,
            "recommendation_detail": recommendation_detail
        }
    )

# ===============================
# DISEASE DETECTION VIEW
# ===============================

# LOAD LABELS
# =====================================================

with open("agroapp/ml_model/labels.txt", "r") as f:

    class_names = [line.strip() for line in f.readlines()]


# =====================================================
# DISEASE DETECTION VIEW
# =====================================================

def disease_detection(request):

    result = None

    if request.method == "POST" and request.FILES.get("leaf_image"):

        image = request.FILES["leaf_image"]

        fs = FileSystemStorage()

        filename = fs.save(image.name, image)

        image_path = fs.path(filename)

        image_url = fs.url(filename)

        # ============================================
        # IMAGE PREPROCESSING
        # ============================================

        img = Image.open(image_path).convert("RGB")

        img = img.resize((224, 224))

        img_array = np.array(img)

        img_array = (img_array / 127.5) - 1

        img_array = np.expand_dims(img_array, axis=0)

        # ============================================
        # PREDICTION
        # ============================================

        prediction_array = model.predict(img_array)

        index = np.argmax(prediction_array)

        disease_name = class_names[index].strip()

        # Remove numbering if present
        disease_name = disease_name.replace("0 ", "")
        disease_name = disease_name.replace("1 ", "")
        disease_name = disease_name.replace("2 ", "")
        disease_name = disease_name.replace("3 ", "")

        confidence = round(
            float(np.max(prediction_array)) * 100,
            2
        )

        # ============================================
        # DISEASE KNOWLEDGE BASE
        # ============================================

        disease_data = {

            "EARLY BLIGHT": {

                "symptoms": [
                    "Brown circular spots on leaves",
                    "Yellowing around infected area",
                    "Dry patches spreading across leaf"
                ],

                "recommendation":
                    "Apply fungicide spray, remove infected leaves, and avoid overwatering."
            },

            "LATE BLIGHT": {

                "symptoms": [
                    "Dark water-soaked lesions",
                    "Rapid leaf decay",
                    "White fungal growth under leaves"
                ],

                "recommendation":
                    "Use copper-based fungicide and improve air circulation."
            },

            "Healthy": {

                "symptoms": [
                    "Leaf appears healthy and green"
                ],

                "recommendation":
                    "Plant is healthy. Continue proper care."
            }
        }

        # ============================================
        # GET DISEASE INFORMATION
        # ============================================

        disease_info = disease_data.get(

            disease_name,

            {
                "symptoms": [
                    "No symptom information available"
                ],

                "recommendation":
                    "Consult agriculture expert."
            }
        )

        # ============================================
        # RESULT OBJECT
        # ============================================

        result = {

            "name": disease_name,

            "confidence": confidence,

            "symptoms": disease_info["symptoms"],

            "recommendation": disease_info["recommendation"],

            "image_url": image_url
        }

    return render(

        request,

        "disease_detection.html",

        {
            "result": result
        }
    )

# CHATBOT VIEW
# ==============================
@login_required
def chatbot_view(request):

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    chat_history = []

    if request.method == "POST":

        message = request.POST.get("message", "").strip()

        if message:

            try:

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=f"""
You are Smart AgroAssist, an intelligent agricultural assistant.

Help users with:
- Crop recommendation
- Crop diseases
- Fertilizers
- Soil health
- Irrigation
- Farming practices
- Pest management
- General agriculture questions

Give simple, practical and easy-to-understand answers.

User question:
{message}
"""
                )

                reply = response.text

            except Exception as e:

                print("Gemini Error:", e)

                reply = "AI service temporarily unavailable."

            chat_history.append({
                "user": message,
                "bot": reply
            })

    return render(
        request,
        "chatbot.html",
        {
            "chat_history": chat_history
        }
    )
# ===============================
# PROFILE VIEW
# ===============================
@login_required
def profile_view(request):

    return render(request,
                  "profile.html")