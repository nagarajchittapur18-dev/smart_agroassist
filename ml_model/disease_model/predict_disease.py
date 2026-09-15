import os
import sys
import numpy as np
import tensorflow as tf
from PIL import Image


# --------------------------------------------------
# Configuration
# --------------------------------------------------

MODEL_PATH = "disease_model_v3.keras"
CLASS_NAMES_PATH = "class_names_v3.txt"

IMG_SIZE = (224, 224)

# Confidence bands
HIGH_CONFIDENCE = 0.70
MEDIUM_CONFIDENCE = 0.40


# --------------------------------------------------
# Load model
# --------------------------------------------------

print("Loading disease detection model...")

model = tf.keras.models.load_model(MODEL_PATH)

print("Model loaded successfully.")


# --------------------------------------------------
# Load class names
# --------------------------------------------------

with open(CLASS_NAMES_PATH, "r", encoding="utf-8") as f:
    class_names = [line.strip() for line in f if line.strip()]

print(f"Number of classes: {len(class_names)}")


# --------------------------------------------------
# Image preprocessing
# --------------------------------------------------

def preprocess_image(image_path):

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    image = Image.open(image_path).convert("RGB")

    image = image.resize(IMG_SIZE)

    image_array = np.array(image, dtype=np.float32)

    # Do NOT apply MobileNetV2 preprocessing here.
    # The saved V3 model already performs preprocessing internally.

    image_array = np.expand_dims(image_array, axis=0)

    return image_array


# --------------------------------------------------
# Disease prediction
# --------------------------------------------------

def predict_disease(image_path):

    image = preprocess_image(image_path)

    predictions = model.predict(image, verbose=0)[0]

    # Get top 3 predictions
    top_indices = np.argsort(predictions)[::-1][:3]

    results = []

    for index in top_indices:

        disease_name = class_names[index]
        confidence = float(predictions[index])

        results.append({
            "disease": disease_name,
            "confidence": confidence
        })

    return results


# --------------------------------------------------
# Confidence interpretation
# --------------------------------------------------

def confidence_level(confidence):

    if confidence >= HIGH_CONFIDENCE:
        return "HIGH"

    elif confidence >= MEDIUM_CONFIDENCE:
        return "MEDIUM"

    else:
        return "LOW"


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":

    if len(sys.argv) < 2:

        print("\nUsage:")
        print("python predict_disease.py <image_path>")

        print("\nExample:")
        print(
            'python predict_disease.py "C:\\Users\\Nagaraj\\Desktop\\leaf.jpg"'
        )

        sys.exit(1)

    image_path = sys.argv[1]

    print("\n" + "=" * 60)
    print("SMART AGROASSIST - DISEASE DETECTION")
    print("=" * 60)

    try:

        results = predict_disease(image_path)

        top_prediction = results[0]

        print("\nTOP PREDICTION")
        print("-" * 60)

        print(
            f"Disease    : {top_prediction['disease']}"
        )

        print(
            f"Confidence : {top_prediction['confidence'] * 100:.2f}%"
        )

        print(
            f"Level      : "
            f"{confidence_level(top_prediction['confidence'])}"
        )

        print("\nTOP 3 PREDICTIONS")
        print("-" * 60)

        for i, result in enumerate(results, start=1):

            print(
                f"{i}. {result['disease']} "
                f"({result['confidence'] * 100:.2f}%)"
            )

        print("\nINTERPRETATION")
        print("-" * 60)

        confidence = top_prediction["confidence"]

        if confidence >= HIGH_CONFIDENCE:

            print(
                "The model has relatively high confidence "
                "in the top prediction."
            )

        elif confidence >= MEDIUM_CONFIDENCE:

            print(
                "The model has moderate confidence. "
                "Consider the Top-3 predictions."
            )

        else:

            print(
                "The model has low confidence. "
                "Please upload a clearer leaf image "
                "with good lighting and minimal background."
            )

    except Exception as e:

        print("\nERROR:")
        print(e)