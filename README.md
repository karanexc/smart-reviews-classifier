# 🛍️ Amazon Product Review Classifier

A machine learning project that classifies Amazon product reviews into **positive** or **negative** sentiment using NLP techniques and various ML algorithms.

---

## 📌 Project Overview

This end-to-end ML project involves:

- Preprocessing and cleaning Amazon review data
- Converting text into numerical features using **TF-IDF**
- Training multiple classifiers (Logistic Regression, SVM, XGBoost)
- Hyperparameter tuning with **GridSearchCV**
- Model comparison and selection
- Deploying the final model using **Streamlit**

---

## 🚀 Models Trained & Compared

| Model                    | Accuracy |
|-------------------------|----------|
| Logistic Regression     | 88.17%   |
| Support Vector Machine  | 87.80%   |
| XGBoost                 | 84.40%   |
| MultinomialNB           | 85.51%   |
| Ensemble (LogReg + SVM) | 88.03%   |

> Final model: **Logistic Regression** (selected based on highest test accuracy).

---

## 🧰 Tech Stack

- Python
- Scikit-learn
- XGBoost
- Pandas, NumPy
- Matplotlib
- nltk
- Streamlit
- Jupyter Notebook 

---


---

## 💡 How to Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/karanexc/smart-reviews-classifier.git
   cd smart-reviews-classifier
   ```

2. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the streamlit app**
   ```bash
   streamlit run streamlit_app.py
   ```

## 🧠 Model Inference Sample

###  Review Prediction

| Input                    | Sentiment |
|-------------------------|----------|
| "Absolutely loved it! Highly recommend."     | Positive (1)   |
| "Terrible product, complete waste of money."  | Negative (0)   |
| "It was okay, nothing special."                 | Negative (0)   |


## ⭐ Conclusion

- This project demonstrates an end-to-end ML pipeline from data preprocessing to deployment.
- It also emphasizes the importance of model evaluation and hyperparameter tuning in building a reliable sentiment analysis system.
