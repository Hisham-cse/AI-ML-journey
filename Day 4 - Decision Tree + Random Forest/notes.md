# 📘 Day 4 Notes — Decision Trees & Random Forest (Ensemble Learning)

## 🎯 Objective

Understand:

- How Decision Trees work internally  
- How splitting criteria (Gini, Entropy) function  
- What overfitting in trees looks like  
- How Random Forest improves performance using ensemble learning  
- How to tune tree-based models  
- When to use Trees vs Logistic Regression  

---

## 🟦 1. What is a Decision Tree?

A **Decision Tree** is a supervised ML algorithm used for:

- Classification  
- Regression  

It works like a **flowchart**:

- Each internal node = a question on a feature  
- Each branch = outcome of the question  
- Each leaf node = final prediction  

It mimics **human decision-making**.

---

## 🟦 2. Example of a Decision Tree (Concept)

```text
Is Age > 45?
 │
 ├─ Yes → Is BP High?
 │         ├─ Yes → Disease
 │         └─ No  → No Disease
 │
 └─ No → No Disease
```
Trees split data based on the **best question** to ask at each step.

---

## 🟦 3. Key Terminology

- **Root Node** → First split  
- **Decision Node** → Intermediate split  
- **Leaf Node** → Final prediction  
- **Depth** → Length of the longest path  
- **Pruning** → Cutting unnecessary branches  
- **Feature Importance** → How important a feature is in decisions  

---

## 🟦 4. How Does a Decision Tree Decide the Best Split?

Uses **impurity measures**:

### ✅ Gini Impurity
- Measures misclassification likelihood  
- Range:  
  - `0` → Pure (only one class)  
  - `> 0` → Mixed classes  
- **Lower Gini = better split**

### ✅ Entropy (Information Gain)
- Measures **disorder**  
- High entropy → Mixed classes  
- Low entropy → Pure classes  
- **Information Gain = Entropy before split – Entropy after split**  
- Split with **maximum information gain** is selected.  

---

## 🟦 5. Stopping Criteria in Decision Trees

Tree stops growing when:

- `max_depth` is reached  
- Node becomes pure  
- `min_samples_leaf` is reached  
- No further information gain is possible  

Without stopping → **overfitting happens**.

---

## 🟦 6. Overfitting in Decision Trees

Decision Trees **memorize training data easily**.

### Symptoms:
- Training accuracy ≈ 100%  
- Test accuracy is low  

### Solutions:
- Limit `max_depth`  
- Set `min_samples_split`  
- Set `min_samples_leaf`  
- Use pruning  
- Use Random Forest  

---

## 🟦 7. What is Random Forest?

A **Random Forest** is an ensemble of many Decision Trees.

Instead of relying on a single tree:

- Builds **multiple trees**  

Each tree sees:

- A **random subset of data**  
- A **random subset of features**  

### Final Prediction:
- **Majority voting** (Classification)  
- **Average prediction** (Regression)  

---

## 🟦 8. Why Random Forest is Better Than a Single Tree?

| Decision Tree     | Random Forest          |
|-------------------|------------------------|
| High variance     | Low variance           |
| Overfits easily   | Resistant to overfitting |
| Unstable          | Very stable            |
| Sensitive to noise| Robust to noise        |

✅ **Random Forest = High accuracy + Stability**

---

## 🟦 9. Bagging (Bootstrap Aggregation)

Random Forest uses **Bagging**:

- Sample data **with replacement**  
- Train a tree on each random sample  
- Combine predictions  

✅ This **reduces variance dramatically**.

---

## 🟦 10. Feature Importance in Random Forest

Random Forest can automatically tell:

- Which feature **contributes most**  
- Which features can be **ignored**  

### Useful for:
- Medical diagnosis  
- Finance risk modeling  
- Feature selection before deep learning  

---

## 🟦 11. Hyperparameters to Tune

### ✅ Decision Tree:
- `max_depth`  
- `min_samples_split`  
- `min_samples_leaf`  
- `criterion` (`gini` / `entropy`)  

### ✅ Random Forest:
- `n_estimators`  
- `max_depth`  
- `min_samples_split`  
- `max_features`  

---

## 🟦 12. Classification vs Regression Trees

| Classification Tree      | Regression Tree      |
|--------------------------|----------------------|
| Uses Gini / Entropy      | Uses MSE             |
| Outputs class            | Outputs number       |
| Used for spam, disease   | Used for house price |

---

## 🟦 13. When to Use Decision Trees?

Use Decision Trees when:

- Data is **non-linear**  
- You want **model interpretability**  
- You want **rule-based predictions**  

---

## 🟦 14. When to Use Random Forest?

Use Random Forest when:

- Single tree is **overfitting**  
- **High accuracy** is required  
- Data is **noisy**  
- Interpretability is **less important** than performance  

---

## 🟦 15. Advantages & Disadvantages

### ✅ Decision Tree – Pros
- Easy to understand  
- No feature scaling needed  
- Works on both classification & regression  

### ❌ Decision Tree – Cons
- Overfits easily  
- Unstable with small changes in data  

### ✅ Random Forest – Pros
- High accuracy  
- Less overfitting  
- Handles missing values well  

### ❌ Random Forest – Cons
- Slower than a single tree  
- Harder to interpret  
- More memory usage  

---

## 🟦 16. Interview Takeaways

You can now confidently answer:

- How does a Decision Tree work?  
- What is Gini impurity?  
- Difference between Gini and Entropy?  
- Why do Decision Trees overfit?  
- What is Random Forest?  
- What is bagging?  
- Why is Random Forest better than a single tree?  
- Difference between bagging and boosting?  
- What is feature importance?  

---

## 🟦 17. Final Summary

✔ Learned Decision Tree fundamentals  
✔ Understood Gini vs Entropy  
✔ Learned stopping criteria and overfitting control  
✔ Understood Random Forest as an ensemble  
✔ Learned Bagging technique  
✔ Understood feature importance  
✔ Learned when to use Trees vs Logistic Regression  
✔ Gained interview-ready understanding of tree-based models  

---

## 📚 Day 4 Resources

### 🎥 Video Resources

- Decision Trees Intuition — StatQuest  
- Random Forest Explained — StatQuest  
- Decision Tree with Scikit-learn  

### 📖 Reading Materials

Decision Tree — GeeksforGeeks
https://www.geeksforgeeks.org/decision-tree-implementation-python/

Random Forest — Machine Learning Mastery
https://machinelearningmastery.com/random-forest-ensemble-machine-learning/

Gini vs Entropy Explained
https://www.geeksforgeeks.org/gini-index-vs-entropy/

### 🧑‍💻 Practice Materials

Scikit-learn Decision Tree Docs
https://scikit-learn.org/stable/modules/tree.html

Scikit-learn Random Forest Docs
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

Kaggle Tree-Based Practice
https://www.kaggle.com/learn/decision-trees