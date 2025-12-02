from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
emails = [
    "Win Money Now",
    "You have won a free prize",
    "Claim your reward",
    "Hello Friend, How Are You",
    "Lets Meet Tomorrow",
    "Your Assignment is due",
]
labels = [1, 1, 1, 0, 0, 0]  # spam = 1, not spam = 0
# Step 1: Convert text to numbers
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(emails)

# Step 2: Train the Model
model = MultinomialNB()
model.fit(x, labels)
# Step 3: Test Emails
test_email1 = ["Congratulations! You are selected"]
test_email2 = ["Congratulations! You won 50 Million"]

# Convert emails to numeric vectors
test_x1 = vectorizer.transform(test_email1)
test_x2 = vectorizer.transform(test_email2)

# Predictions
pred1 = model.predict(test_x1)[0]
pred2 = model.predict(test_x2)[0]
# Output result
def print_result(email, prediction):
    print(f"EMAIL: {email}")
    if prediction == 1:
        print("RESULT: SPAM\n")
    else:
        print("RESULT: NOT SPAM\n")

print_result(test_email1[0], pred1)
print_result(test_email2[0], pred2)
