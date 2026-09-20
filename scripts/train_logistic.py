import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

val = pd.read_csv("val.csv")
test = pd.read_csv("test.csv")

# Combine datasets
df = pd.concat([val, test], ignore_index=True)

X = df.drop(columns=["URL", "Label"])
y = df["Label"]

model = LogisticRegression(
    max_iter=10000,
    solver='lbfgs'
)

model.fit(X, y)

joblib.dump(model, "phishing_detection_model_logistic_regression.pkl")

print("Saved Logistic Regression model")
print("Accuracy:", accuracy_score(y, model.predict(X)))