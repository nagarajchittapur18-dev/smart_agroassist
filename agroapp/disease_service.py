import json
from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DISEASE_MODEL_DIR = BASE_DIR / "ml_model" / "disease_model"

MODEL_PATH = DISEASE_MODEL_DIR / "disease_model_v3.keras"
CLASS_NAMES_PATH = DISEASE_MODEL_DIR / "class_names_v3.txt"
DISEASE_INFO_PATH = DISEASE_MODEL_DIR / "disease_info.json"


# --------------------------------------------------
# Configuration
# --------------------------------------------------

IMG_SIZE = (224, 224)

HIGH_CONFIDENCE = 0.70
MEDIUM_CONFIDENCE = 0.40


# --------------------------------------------------
# Load model
# --------------------------------------------------

print("Loading Smart AgroAssist disease model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Disease model loaded successfully.")


# --------------------------------------------------
# Load class names
# --------------------------------------------------

with open(CLASS_NAMES_PATH, "r", encoding="utf-8") as file:
    class_names = [
        line.strip()
        for line in file
        if line.strip()
    ]


# --------------------------------------------------
# Load disease information
# --------------------------------------------------

with open(DISEASE_INFO_PATH, "r", encoding="utf-8") as file:
    disease_info = json.load(file)


# --------------------------------------------------
# Confidence level
# --------------------------------------------------

def get_confidence_level(confidence):

    if confidence >= HIGH_CONFIDENCE:
        return "HIGH"

    if confidence >= MEDIUM_CONFIDENCE:
        return "MEDIUM"

    return "LOW"


# --------------------------------------------------
# Prepare image
# --------------------------------------------------
def preprocess_image(image_file):

    image = Image.open(image_file).convert("RGB")

    image = image.resize(IMG_SIZE)

    image_array = np.array(
        image,
        dtype=np.float32
    )

    # Do NOT apply MobileNetV2 preprocessing here.
    # The saved V3 model performs preprocessing internally.

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    return image_array
# --------------------------------------------------
# Predict disease
# --------------------------------------------------

def predict_disease(image_file):

    image_array = preprocess_image(image_file)

    predictions = model.predict(
        image_array,
        verbose=0
    )[0]

    # Top 3 indexes
    top_indices = np.argsort(
        predictions
    )[::-1][:3]

    top_predictions = []

    for index in top_indices:

        disease_name = class_names[index]

        confidence = float(
            predictions[index]
        )

        top_predictions.append({
            "disease": disease_name,
            "confidence": confidence,
            "confidence_percent": round(
                confidence * 100,
                2
            ),
            "confidence_level": get_confidence_level(
                confidence
            )
        })


    # --------------------------------------------------
    # Top prediction
    # --------------------------------------------------

    top_prediction = top_predictions[0]

    disease_name = top_prediction["disease"]

    # Get information from JSON
    info = disease_info.get(
        disease_name,
        {}
    )


    # --------------------------------------------------
    # Low confidence handling
    # --------------------------------------------------

    if top_prediction["confidence"] < MEDIUM_CONFIDENCE:

        prediction_status = "UNCERTAIN"

        message = (
            "The model is uncertain about this prediction. "
            "Please upload a clear close-up image of the leaf "
            "with good lighting and minimal background."
        )

    else:

        prediction_status = "PREDICTION"

        message = (
            "This is an AI-based prediction and should be "
            "used as a preliminary indication."
        )


    # --------------------------------------------------
    # Final result
    # --------------------------------------------------

    result = {

        "disease": disease_name,

        "confidence": top_prediction[
            "confidence"
        ],

        "confidence_percent": top_prediction[
            "confidence_percent"
        ],

        "confidence_level": top_prediction[
            "confidence_level"
        ],

        "prediction_status": prediction_status,

        "message": message,

        "top_3": top_predictions,

        "common_name": info.get(
            "common_name",
            disease_name
        ),

        "crop": info.get(
            "crop",
            ""
        ),

        "description": info.get(
            "description",
            ""
        ),

        "symptoms": info.get(
            "symptoms",
            []
        ),

        "recommended_actions": info.get(
            "recommended_actions",
            []
        ),

        "prevention": info.get(
            "prevention",
            []
        )
    }

    return result