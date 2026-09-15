import numpy as np
import tensorflow as tf

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

# ============================================================
# SMART AGROASSIST
# DISEASE MODEL EVALUATION - VERSION 3
# ============================================================

TEST_DIR = "dataset/test"
MODEL_PATH = "disease_model_v3.keras"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

print("=" * 60)
print("SMART AGROASSIST")
print("DISEASE MODEL EVALUATION - VERSION 3")
print("=" * 60)

# ============================================================
# LOAD MODEL
# ============================================================

print("\nLoading model...")

model = tf.keras.models.load_model(
    MODEL_PATH
)

print("Model loaded successfully!")

# ============================================================
# LOAD TEST DATA
# ============================================================

print("\nLoading test dataset...")

test_ds = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False,
    label_mode="int"
)

class_names = test_ds.class_names
num_classes = len(class_names)

print("\nNumber of test classes:", num_classes)

for i, name in enumerate(class_names):
    print(f"{i}: {name}")

# ============================================================
# GENERATE PREDICTIONS
# ============================================================

print("\nGenerating predictions...")

y_true = []
y_prob = []

for images, labels in test_ds:

    predictions = model.predict(
        images,
        verbose=0
    )

    y_true.extend(
        labels.numpy()
    )

    y_prob.extend(
        predictions
    )

y_true = np.array(y_true)
y_prob = np.array(y_prob)

y_pred = np.argmax(
    y_prob,
    axis=1
)

# ============================================================
# TOP-1 ACCURACY
# ============================================================

accuracy = accuracy_score(
    y_true,
    y_pred
)

print("\n")
print("=" * 60)
print("TOP-1 ACCURACY")
print("=" * 60)

print(
    f"Accuracy: {accuracy * 100:.2f}%"
)

# ============================================================
# TOP-3 ACCURACY
# ============================================================

top3_correct = 0

for i in range(len(y_true)):

    top3_predictions = np.argsort(
        y_prob[i]
    )[-3:]

    if y_true[i] in top3_predictions:
        top3_correct += 1

top3_accuracy = (
    top3_correct /
    len(y_true)
)

print("\n")
print("=" * 60)
print("TOP-3 ACCURACY")
print("=" * 60)

print(
    f"Top-3 Accuracy: "
    f"{top3_accuracy * 100:.2f}%"
)

# ============================================================
# PRECISION / RECALL / F1
# ============================================================

print("\n")
print("=" * 60)
print("PRECISION / RECALL / F1 SCORE")
print("=" * 60)

report = classification_report(
    y_true,
    y_pred,
    labels=list(range(num_classes)),
    target_names=class_names,
    zero_division=0
)

print(report)

# ============================================================
# CONFUSION MATRIX
# ============================================================

print("\n")
print("=" * 60)
print("CONFUSION MATRIX")
print("=" * 60)

cm = confusion_matrix(
    y_true,
    y_pred,
    labels=list(range(num_classes))
)

print(cm)

# ============================================================
# BEST AND WORST CLASSES
# ============================================================

print("\n")
print("=" * 60)
print("CLASS PERFORMANCE")
print("=" * 60)

class_correct = np.zeros(
    num_classes,
    dtype=int
)

class_total = np.zeros(
    num_classes,
    dtype=int
)

for true_label, predicted_label in zip(
    y_true,
    y_pred
):

    class_total[true_label] += 1

    if true_label == predicted_label:
        class_correct[true_label] += 1

print("\nAccuracy by class:")

class_accuracies = []

for i in range(num_classes):

    if class_total[i] > 0:

        class_accuracy = (
            class_correct[i] /
            class_total[i]
        )

    else:

        class_accuracy = 0

    class_accuracies.append(
        class_accuracy
    )

    print(
        f"{class_names[i]}: "
        f"{class_accuracy * 100:.2f}% "
        f"({class_correct[i]}/"
        f"{class_total[i]})"
    )

# ============================================================
# SAVE REPORT
# ============================================================

with open(
    "disease_evaluation_v3.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "SMART AGROASSIST\n"
    )

    f.write(
        "DISEASE MODEL EVALUATION V3\n"
    )

    f.write(
        "=" * 60 + "\n\n"
    )

    f.write(
        f"Number of classes: "
        f"{num_classes}\n"
    )

    f.write(
        f"Top-1 Accuracy: "
        f"{accuracy * 100:.2f}%\n"
    )

    f.write(
        f"Top-3 Accuracy: "
        f"{top3_accuracy * 100:.2f}%\n\n"
    )

    f.write(
        "PRECISION / RECALL / F1\n"
    )

    f.write(
        report
    )

    f.write(
        "\n\nCONFUSION MATRIX\n"
    )

    f.write(
        str(cm)
    )

    f.write(
        "\n\nCLASS ACCURACY\n"
    )

    for i in range(num_classes):

        f.write(
            f"{class_names[i]}: "
            f"{class_accuracies[i] * 100:.2f}% "
            f"({class_correct[i]}/"
            f"{class_total[i]})\n"
        )

print("\n")
print("=" * 60)
print("EVALUATION COMPLETE")
print("=" * 60)

print(
    "Report saved to:"
)

print(
    "disease_evaluation_v3.txt"
)s