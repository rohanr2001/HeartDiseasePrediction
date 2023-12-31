# -*- coding: utf-8 -*-
"""heartdiseaseprediction-dwdm-ipynb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/rohanr2001/2bb029a3aebde129df4a0e501ae3f9a2/heartdiseaseprediction-dwdm-ipynb.ipynb

# Heart Disease Prediction Application
# Datawarehouse and DataMining Project

**Importing the dependancies**
"""

import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.metrics import plot_confusion_matrix
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score

"""**Data Collection and Processing**"""

dataFrame = pd.read_csv('/content/heart.csv')
dataFrame.head()

dataFrame.shape

dataFrame.info()

dataFrame.describe()

#checking the distribution of Target variable
dataFrame['target'].value_counts()

"""1-->Presence of Heart Disease

0-->No Presence of Heart Disease
"""

rcParams['figure.figsize'] = 20, 14
dataFrame.hist()

"""**Splitting the Features and Target of the DataFrame.**"""

X = dataFrame.drop(columns = 'target', axis = 1)
Y = dataFrame['target']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, stratify = Y, random_state = 2)

print(X_train.shape, X_test.shape)

print(y_train.shape, y_test.shape)

"""# **Model training**

*Logistic Regression**
"""

LRmodel = LogisticRegression()

LRmodel.fit(X_train, y_train)

#Model Evaluation

#Accuracy, Precision, F1-score, Recall, RocAuc on training Data

X_train_prediction = LRmodel.predict(X_train)

training_data_accuracy = accuracy_score(X_train_prediction, y_train)
training_data_precision = precision_score(X_train_prediction, y_train)
training_data_f1 = f1_score(X_train_prediction, y_train)
training_data_recall = recall_score(X_train_prediction, y_train)
training_data_roc_auc = roc_auc_score(X_train_prediction, y_train)


print("Accuracy on Training Data(LR): ", training_data_accuracy)
print("Precision on Training Data(LR): ", training_data_precision)
print("F1-score on Training Data(LR): ", training_data_f1)
print("Recall on Training Data(LR): ", training_data_recall)
print("Roc_Auc Score on Training Data(LR): ", training_data_roc_auc)

#Accuracy, Precision, F1-score, Recall, RocAuc on Testing Data

X_test_prediction = LRmodel.predict(X_test)

testing_data_accuracy = accuracy_score(X_test_prediction, y_test)
testing_data_precision = precision_score(X_test_prediction, y_test)
testing_data_f1 = f1_score(X_test_prediction, y_test)
testing_data_recall = recall_score(X_test_prediction, y_test)
testing_data_roc_auc = roc_auc_score(X_test_prediction, y_test)

print("Accuracy on Testing Data(LR): ", testing_data_accuracy)
print("Precision on Testing Data(LR): ", testing_data_precision)
print("F1-score on Testing Data(LR): ", testing_data_f1)
print("Recall on Testing Data(LR): ", testing_data_recall)
print("Roc_Auc Score on Testing Data(LR): ", testing_data_roc_auc)

rcParams['figure.figsize'] = 14, 8
plot_confusion_matrix(LRmodel, X_test, y_test)

"""**Support Vector Classifier**"""

svc_scores = []
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
for i in range(len(kernels)):
  svc_classifier = SVC(kernel = kernels[i])
  svc_classifier.fit(X_train, y_train)
  svc_scores.append(svc_classifier.score(X_test, y_test))

plt.bar(kernels, svc_scores)
for i in range(len(kernels)):
  plt.text(i, svc_scores[i], svc_scores[i])

svc_classifier = SVC(kernel = 'linear')
svc_classifier.fit(X_train, y_train)

X_train_prediction = svc_classifier.predict(X_train)

training_data_accuracyS = accuracy_score(X_train_prediction, y_train)
training_data_precisionS = precision_score(X_train_prediction, y_train)
training_data_f1S = f1_score(X_train_prediction, y_train)
training_data_recallS = recall_score(X_train_prediction, y_train)
training_data_roc_aucS = roc_auc_score(X_train_prediction, y_train)


print("Accuracy on Training Data(SVM): ", training_data_accuracyS)
print("Precision on Training Data(SVM): ", training_data_precisionS)
print("F1-score on Training Data(SVM): ", training_data_f1S)
print("Recall on Training Data(SVM): ", training_data_recallS)
print("Roc_Auc Score on Training Data(SVM): ", training_data_roc_aucS)

X_test_prediction = svc_classifier.predict(X_test)

testing_data_accuracyS = accuracy_score(X_test_prediction, y_test)
testing_data_precisionS = precision_score(X_test_prediction, y_test)
testing_data_f1S = f1_score(X_test_prediction, y_test)
testing_data_recallS = recall_score(X_test_prediction, y_test)
testing_data_roc_aucS = roc_auc_score(X_test_prediction, y_test)

print("Accuracy on Testing Data(SVM): ", testing_data_accuracyS)
print("Precision on Testing Data(SVM): ", testing_data_precisionS)
print("F1-score on Testing Data(SVM): ", testing_data_f1S)
print("Recall on Testing Data(SVM): ", testing_data_recallS)
print("Roc_Auc Score on Testing Data(SVM): ", testing_data_roc_aucS)

"""**K-Nearest Neighbors**"""

knn_scores = []
for k in range(1, 20):
  knn_classifier = KNeighborsClassifier(n_neighbors=k)
  knn_classifier.fit(X_train, y_train)
  knn_scores.append(knn_classifier.score(X_test, y_test))
print(knn_scores)

rcParams['figure.figsize'] = 14, 8
plt.plot([k for k in range(1, 20)], knn_scores, color = 'red')

knn_classifier = KNeighborsClassifier(n_neighbors=2)
knn_classifier.fit(X_train, y_train)

#Accuracy, Precision, F1-score, Recall, RocAuc on training Data

X_train_prediction = knn_classifier.predict(X_train)

training_data_accuracyK = accuracy_score(X_train_prediction, y_train)
training_data_precisionK = precision_score(X_train_prediction, y_train)
training_data_f1K = f1_score(X_train_prediction, y_train)
training_data_recallK = recall_score(X_train_prediction, y_train)
training_data_roc_aucK = roc_auc_score(X_train_prediction, y_train)

print("Accuracy on Training Data(LR): ", training_data_accuracyK)
print("Precision on Training Data(LR): ", training_data_precisionK)
print("F1-score on Training Data(LR): ", training_data_f1K)
print("Recall on Training Data(LR): ", training_data_recallK)
print("Roc_Auc Score on Training Data(LR): ", training_data_roc_aucK)

#Accuracy, Precision, F1-score, Recall, RocAuc on Testing Data

X_test_prediction = knn_classifier.predict(X_test)

testing_data_accuracyK = accuracy_score(X_test_prediction, y_test)
testing_data_precisionK = precision_score(X_test_prediction, y_test)
testing_data_f1K = f1_score(X_test_prediction, y_test)
testing_data_recallK = recall_score(X_test_prediction, y_test)
testing_data_roc_aucK = roc_auc_score(X_test_prediction, y_test)

print("Accuracy on Testing Data(KNN): ", testing_data_accuracyK)
print("Precision on Testing Data(KNN): ", testing_data_precisionK)
print("F1-score on Testing Data(KNN): ", testing_data_f1K)
print("Recall on Testing Data(KNN): ", testing_data_recallK)
print("Roc_Auc Score on Testing Data(KNN): ", testing_data_roc_aucK)

rcParams['figure.figsize'] = 14, 8
plot_confusion_matrix(knn_classifier, X_test, y_test,cmap=plt.cm.Blues)
plt.grid(False)
plt.show()

"""# Prediction System

"""

input_data = (34,0,1,118,210,0,1,192,0,0.7,2,0,2)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1, -1)
print(input_data)

predictionLR = LRmodel.predict(input_data)
predictionKNN = knn_classifier.predict(input_data)
predictionSVC = svc_classifier.predict(input_data)

if predictionLR and predictionKNN and predictionSVC == 1:
  print("The person has a heart disease (1)")
else:
  print("The person does not has a heart disease (0)")

def heartdisease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):

  x = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
  predictionLR = LRmodel.predict(x.reshape(1, -1))
  predictionKNN = knn_classifier.predict(x.reshape(1, -1))
  predictionSVC = svc_classifier.predict(x.reshape(1, -1))
  yes="The person has a heart disease (1)"
  no="The person does not has a heart disease (0)"
  if predictionLR and predictionKNN and predictionSVC == 1 :
      return yes
  else:

    return no

import gradio as gr

outputs = gr.outputs.Textbox()

app = gr.Interface(fn=heartdisease, inputs=['number','number','number','number','number','number','number','number','number','number','number','number','number'], outputs=outputs,description="Heart Disease Prediction Application")

app.launch()
