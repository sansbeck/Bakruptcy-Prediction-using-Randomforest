# -*- coding: utf-8 -*-
"""Bankruptcy Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xmcqBcklJ68YXYoN54U6JN-ontiWCmF3
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score, f1_score
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler, SMOTE

warnings.filterwarnings("ignore")

df = pd.read_csv("/content/datasett.csv")

print(df.info())
print(df.describe())

print(df.isnull().sum())
print(df.duplicated().sum())

print(df["Bankrupt?"].value_counts(normalize=True))

print(df.shape)

features = ['ROA', 'Debt Ratio', 'NPS', 'Cash Flow']
X = df[features]
y = df['Bankrupt?']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

baseline_rf = RandomForestClassifier(random_state=42)
baseline_rf.fit(X_train, y_train)
y_pred_baseline = baseline_rf.predict(X_test)

print("Baseline Model")
print(f"Accuracy: {accuracy_score(y_test, y_pred_baseline)}")
print(f"Recall: {recall_score(y_test, y_pred_baseline)}")
print(f"F1 Score: {f1_score(y_test, y_pred_baseline)}")
print(confusion_matrix(y_test, y_pred_baseline))
print(classification_report(y_test, y_pred_baseline))

rus = RandomUnderSampler(random_state=42)
X_res, y_res = rus.fit_resample(X_train, y_train)
undersample_rf = RandomForestClassifier(random_state=42)
undersample_rf.fit(X_res, y_res)
y_pred_undersample = undersample_rf.predict(X_test)

print("\nRandom Forest with Undersampling")
print(f"Accuracy: {accuracy_score(y_test, y_pred_undersample)}")
print(f"Recall: {recall_score(y_test, y_pred_undersample)}")
print(f"F1 Score: {f1_score(y_test, y_pred_undersample)}")
print(confusion_matrix(y_test, y_pred_undersample))
print(classification_report(y_test, y_pred_undersample))

ros = RandomOverSampler(random_state=42)
X_res, y_res = ros.fit_resample(X_train, y_train)
oversample_rf = RandomForestClassifier(random_state=42)
oversample_rf.fit(X_res, y_res)
y_pred_oversample = oversample_rf.predict(X_test)

print("\nRandom Forest with Oversampling")
print(f"Accuracy: {accuracy_score(y_test, y_pred_oversample)}")
print(f"Recall: {recall_score(y_test, y_pred_oversample)}")
print(f"F1 Score: {f1_score(y_test, y_pred_oversample)}")
print(confusion_matrix(y_test, y_pred_oversample))
print(classification_report(y_test, y_pred_oversample))

smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X_train, y_train)
smote_rf = RandomForestClassifier(random_state=42)
smote_rf.fit(X_res, y_res)
y_pred_smote = smote_rf.predict(X_test)

print("\nRandom Forest with SMOTE")
print(f"Accuracy: {accuracy_score(y_test, y_pred_smote)}")
print(f"Recall: {recall_score(y_test, y_pred_smote)}")
print(f"F1 Score: {f1_score(y_test, y_pred_smote)}")
print(confusion_matrix(y_test, y_pred_smote))
print(classification_report(y_test, y_pred_smote))

print("\nImproved Metrics using SMOTE, Undersampling, and Oversampling")
