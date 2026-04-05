import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("/Users/salmata/Downloads/Online Retail.xlsx")

print("Original shape:", df.shape)
print(df.head())
df.info()

df = df.dropna(subset=["CustomerID"])

df = df[df["Quantity"] > 0]

df = df[df["UnitPrice"] > 0]


df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nCleaned shape:", df.shape)
print(df.head())


df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]


snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)


rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalPrice": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

print("\nRFM table:")
print(rfm.head())
print(rfm.describe())


rfm["Target"] = (rfm["Frequency"] > 3).astype(int)

print("\nTarget distribution:")
print(rfm["Target"].value_counts())

from sklearn.model_selection import train_test_split

X = rfm[["Recency", "Monetary"]]
y = rfm["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


y_prob = model.predict_proba(X_test)[:, 1]
print("\nROC-AUC:", roc_auc_score(y_test, y_prob))

from sklearn.metrics import roc_curve

fpr, tpr, _ = roc_curve(y_test, y_prob)

plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test)
y_prob_knn = knn.predict_proba(X_test)[:, 1]

print("\n--- KNN Results ---")
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("\nClassification Report:\n", classification_report(y_test, y_pred_knn))
print("ROC-AUC:", roc_auc_score(y_test, y_prob_knn))
