import os
from tensorflow.keras.models import load_model

print("Loading model...")

print(os.path.exists("agroapp/ml_model/keras_model.h5"))

model = load_model("agroapp/ml_model/keras_model.h5")

print("Model loaded successfully!")

model.summary()