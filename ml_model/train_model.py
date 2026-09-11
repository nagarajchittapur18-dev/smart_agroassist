import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# =========================================================
# 1. LOAD DATASET
# =========================================================

DATASET_PATH = "crop_data.csv"
MODEL_PATH = "crop_model.pkl"

data = pd.read_csv(DATASET_PATH)

print("\nDataset loaded successfully!")
print("Dataset shape:", data.shape)


# =========================================================
# 2. CLEAN COLUMN NAMES
# =========================================================

data.columns = data.columns.str.strip()

print("\nColumns found:")
print(list(data.columns))


# =========================================================
# 3. REMOVE UNNECESSARY COLUMNS
# =========================================================

# Remove accidental Excel/index columns if present
columns_to_remove = []

for column in data.columns:
    if column.lower().startswith("unnamed"):
        columns_to_remove.append(column)

if "id" in data.columns:
    columns_to_remove.append("id")

if columns_to_remove:
    data = data.drop(columns=columns_to_remove)
    print("\nRemoved columns:", columns_to_remove)


# =========================================================
# 4. CHECK REQUIRED COLUMNS
# =========================================================

required_columns = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall",
    "label"
]

missing_columns = [
    column for column in required_columns
    if column not in data.columns
]

if missing_columns:
    print("\nERROR: Missing columns:")
    print(missing_columns)
    print("\nYour dataset must contain:")
    print(required_columns)
    raise SystemExit


# =========================================================
# 5. REMOVE EMPTY ROWS
# =========================================================

data = data.dropna()

print("\nDataset after removing empty rows:")
print(data.shape)


# =========================================================
# 6. REMOVE DUPLICATE ROWS
# =========================================================

before_duplicates = len(data)

data = data.drop_duplicates()

after_duplicates = len(data)

print("\nDuplicate rows removed:",
      before_duplicates - after_duplicates)

print("Final dataset size:", data.shape)


# =========================================================
# 7. DEFINE FEATURES AND TARGET
# =========================================================

features = [
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall"
]

X = data[features]
y = data["label"]


# =========================================================
# 8. SPLIT DATA INTO TRAINING AND TESTING
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# =========================================================
# 9. CREATE DECISION TREE MODEL
# =========================================================

model = DecisionTreeClassifier(
    random_state=42
)


# =========================================================
# 10. TRAIN MODEL
# =========================================================

print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed!")


# =========================================================
# 11. TEST MODEL
# =========================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n========================================")
print("MODEL PERFORMANCE")
print("========================================")

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# =========================================================
# 12. TRAIN FINAL MODEL ON ALL DATA
# =========================================================

print("\nTraining final model using complete dataset...")

model.fit(X, y)


# =========================================================
# 13. SAVE MODEL
# =========================================================

joblib.dump(model, MODEL_PATH)

print("\n========================================")
print("MODEL SAVED SUCCESSFULLY!")
print("========================================")

print("Model file:", MODEL_PATH)
print("Dataset file:", DATASET_PATH)
print("Total training records:", len(data))
print("Features:", features)
print("========================================\n")