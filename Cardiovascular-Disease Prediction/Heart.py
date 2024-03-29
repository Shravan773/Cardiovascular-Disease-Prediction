import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from keras.models import Sequential
from keras.layers import Dense, Dropout
from mlxtend.plotting import plot_confusion_matrix

# Load dataset
dataset = pd.read_csv('new.csv')

# GUI setup
root = tk.Tk()
root.title("Heart Disease Detection System")

# Set window size
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# Load background image
image2 = Image.open('images/14.jpg')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Heading
lbl = tk.Label(root, text="Heart Disease Detection System", font=('times', 35, 'bold'), height=1, width=32, bg="green", fg="white")
lbl.place(x=300, y=15)

# Function to display confusion matrix
def display_confusion_matrix(cm, title):
    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title(title, fontsize=18)
    plt.show()

# Function to display classification report
def display_classification_report(report):
    print("Classification Report:\n", report)

# Function to display accuracy
def display_accuracy(accuracy):
    print("Accuracy: {:.2f}%".format(accuracy * 100))

# SVM Model Training and Evaluation
def Model_Training():
    # Data preprocessing
    X = dataset.drop(columns=['target'])
    y = dataset['target']
    X = pd.get_dummies(X, columns=['cp', 'restecg', 'slope', 'ca', 'thal'])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=6)

    # Train SVM model
    svm_classifier = SVC(kernel='linear', random_state=6)
    svm_classifier.fit(X_train, y_train)
    svm_y_pred = svm_classifier.predict(X_test)

    # Evaluate SVM model
    svm_accuracy = accuracy_score(y_test, svm_y_pred)
    svm_classification_report = classification_report(y_test, svm_y_pred)
    svm_confusion_matrix = confusion_matrix(y_test, svm_y_pred)

    # Display results
    display_classification_report(svm_classification_report)
    display_confusion_matrix(svm_confusion_matrix, title='SVM Confusion Matrix')
    display_accuracy(svm_accuracy)

# Random Forest Model Training and Evaluation
def RF():
    # Data preprocessing
    X = dataset.drop(columns=['target'])
    y = dataset['target']
    X = pd.get_dummies(X, columns=['cp', 'restecg', 'slope', 'ca', 'thal'])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=6)

    # Train Random Forest model
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=6)
    rf_classifier.fit(X_train, y_train)
    rf_y_pred = rf_classifier.predict(X_test)

    # Evaluate Random Forest model
    rf_accuracy = accuracy_score(y_test, rf_y_pred)
    rf_classification_report = classification_report(y_test, rf_y_pred)
    rf_confusion_matrix = confusion_matrix(y_test, rf_y_pred)

    # Display results
    display_classification_report(rf_classification_report)
    display_confusion_matrix(rf_confusion_matrix, title='Random Forest Confusion Matrix')
    display_accuracy(rf_accuracy)

# Decision Tree Model Training and Evaluation
def DST():
    # Data preprocessing
    le = LabelEncoder()
    data = dataset.dropna()
    data['target'] = le.fit_transform(data['target'])
    data['thal'] = le.fit_transform(data['thal'])
    data['cp'] = le.fit_transform(data['cp'])
    x = data.drop(['target'], axis=1)
    y = data['target']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=2)

    # Train Decision Tree model
    clf_gini = DecisionTreeClassifier(criterion='entropy', random_state=2)
    clf_gini.fit(x_train, y_train)
    y_pred = clf_gini.predict(x_test)

    # Evaluate Decision Tree model
    accuracy = accuracy_score(y_test, y_pred)
    classification_report = classification_report(y_test, y_pred)
    confusion_matrix = confusion_matrix(y_test, y_pred)

    # Display results
    display_classification_report(classification_report)
    display_confusion_matrix(confusion_matrix, title='Decision Tree Confusion Matrix')
    display_accuracy(accuracy)

# Naive Bayes Model Training and Evaluation
def NB():
    # Data preprocessing
    X = dataset.drop(columns=['target'])
    y = dataset['target']
    X = pd.get_dummies(X, columns=['cp', 'restecg', 'slope', 'ca', 'thal'])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=0)

    # Train Naive Bayes model
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    # Evaluate Naive Bayes model
    accuracy = accuracy_score(y_test, y_pred)
    classification_report = classification_report(y_test, y_pred)
    confusion_matrix = confusion_matrix(y_test, y_pred)

    # Display results
    display_classification_report(classification_report)
    display_confusion_matrix(confusion_matrix, title='Naive Bayes Confusion Matrix')
    display_accuracy(accuracy)

# ANN Model Training and Evaluation
def ANN_algo():
    # Data preprocessing
    le = LabelEncoder()
    data = dataset.dropna()
    data['target'] = le.fit_transform(data['target'])
    data['thal'] = le.fit_transform(data['thal'])
    data['cp'] = le.fit_transform(data['cp'])
    x = data.drop(['target'], axis=1)
    y = data['target']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    sc = StandardScaler()
    X_train = sc.fit_transform(x_train)
    X_test = sc.transform(x_test)

    # Train ANN model
    classifier = Sequential()
    classifier.add(Dense(activation="relu", input_dim=13, units=8, kernel_initializer="uniform"))
    classifier.add(Dense(activation="relu", units=14, kernel_initializer="uniform"))
    classifier.add(Dense(activation="sigmoid", units=1, kernel_initializer="uniform"))
    classifier.add(Dropout(0.2))
    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    classifier.fit(X_train, y_train, batch_size=8, epochs=100)
    y_pred = classifier.predict(X_test)
    y_pred = (y_pred > 0.5)

    # Evaluate ANN model
    accuracy = accuracy_score(y_test, y_pred)
    classification_report = classification_report(y_test, y_pred)
    confusion_matrix = confusion_matrix(y_test, y_pred)

    # Display results
    display_classification_report(classification_report)
    display_confusion_matrix(confusion_matrix, title='ANN Confusion Matrix')
    display_accuracy(accuracy)

def call_file():
    import Check_Heart
    Check_Heart.Train()




check = tk.Frame(root, w=100)
check.place(x=700, y=100)
# Function to close the window
def window():
    root.destroy()

# # Buttons to trigger different models
# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"), text="SVM", command=Model_Training, width=15, height=2)
# button3.place(x=250, y=200)

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"), text="Desicion tree", command=DST, width=15, height=2)
# button3.place(x=450, y=200)

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"), text="Random forest", command=RF, width=15, height=2)
# button3.place(x=650, y=200)

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"), text="Naive Bayes", command=NB, width=15, height=2)
# button3.place(x=850, y=200)

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"), text="ANN", command=ANN_algo, width=15, height=2)
# button3.place(x=1050, y=200)
button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Disease Detection", command=call_file, width=15, height=2)
button4.place(x=5, y=350)

# Exit button
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, 'bold'), bg="red", fg="white")
exit.place(x=5, y=450)

root.mainloop()