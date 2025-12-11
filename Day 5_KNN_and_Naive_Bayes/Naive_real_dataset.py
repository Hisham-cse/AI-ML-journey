# TEXT CLASSIFICATION (MULTINOMIAL NB)
# ------------------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# -------------------------
# STEP 1: Load Dataset Properly
# -------------------------

try:
    spam_df = pd.read_csv("spam.csv", encoding="latin-1")
except:
    raise Exception("ERROR: spam.csv not found. Place it in the same folder!")

# Many spam.csv files have extra useless columns, so keep ONLY first two.
spam_df = spam_df.iloc[:, :2]
spam_df.columns = ["label", "text"]

# -------------------------
# STEP 2: Clean Dataset
# -------------------------

# Remove rows where label or text is missing
spam_df = spam_df.dropna(subset=["label", "text"])

# Convert text to string
spam_df["text"] = spam_df["text"].astype(str)

# Map labels
spam_df["label"] = spam_df["label"].map({"spam": 1, "ham": 0})

# Remove rows where mapping failed
spam_df = spam_df.dropna(subset=["label"])

# Final check
print("Rows after cleaning:", len(spam_df))
print(spam_df.head())

if len(spam_df) == 0:
    raise Exception("ERROR: Your spam.csv file contains NO valid data. Please use a correct spam dataset.")

# -------------------------
# STEP 3: Vectorize
# -------------------------

vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(spam_df["text"])
y = spam_df["label"]

# -------------------------
# STEP 4: Train/Test Split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# STEP 5: Train Model
# -------------------------

model = MultinomialNB()
model.fit(X_train, y_train)

# -------------------------
# STEP 6: Predict
# -------------------------

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Output

# python .\Naive_real_dataset.py
# Rows after cleaning: 10
#    label                                               text
# 0      0  Go until jurong point crazy available only in ...
# 1      0                            Ok lar joking wif u oni
# 2      1  Free entry in 2 a wkly comp to win FA Cup fina...
# 3      0        U dun say so early hor u c already then say
# 4      1  WINNER As a valued customer you have been sele...

# Accuracy: 1.0

# Classification Report:
#                precision    recall  f1-score   support

#            0       1.00      1.00      1.00         2

#     accuracy                           1.00         2
#    macro avg       1.00      1.00      1.00         2
# weighted avg       1.00      1.00      1.00         2

