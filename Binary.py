import streamlit as st
import pandas as pd
import numpy as np
import math
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score



@st.cache(persist=True)
def getData(file_path,names,):
    data = pd.read_table(file_path,sep=',',names=names)
    data.drop(columns="ID")
    data['Class'] = (data['Class'] == 4).astype(int)
    #data.loc[data['Class'] == 4, 'Class'] = 1
    #for i in range(data.shape[0]):
        #if data[i,-1] ==4:
            #data[i,-1] = 1
        #else:
            #data[i,-1] = 0
    return data

@st.cache(persist=True) #deperator: makes performace faster
def load_data():
    data = pd.read_csv()
    label = LabelEncoder()
    for col in data.columns:
        data[col] = label.fit_transform(data[col])
    return data


def main():
    st.title("Binary Classification Web App")
    st.sidebar.title("Binary Classification Web App")
    st.markdown("Is this sample cancerous?")
    st.sidebar.markdown("Is this sample cancerous?")

    @st.cache(persist=True)
    def split(df):
        y=data.iloc[ :, -1:]
        x=data.drop(columns=["Class"])
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=0)
        return x_train, x_test, y_train, y_test

    def plot_metrics(metrics_list):
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            plot_confusion_matrix(model, x_test, y_test, display_labels=claass_names)
            st.pyplot()

        if 'ROC Curve' in metrics_list:
            st.subheader("Confusion Matrix")
            plot_roc_curve(model, x_test, y_test)
            st.pyplot()

        if 'Precision-Recall Curve' in metrics_list:
            st.subheader("Precision Recall Curve")
            plot_precision_recall_curve(model,x_test,y_test)
            st.pyplot()

    names = ("ID", "Clump Thickness","Uniformity of Cell Size","Uniformity of Cell Shape",
    "Marginal Adhesion","Single Epithelial Cell Size","Bare Nuclei","Bland Chromatin","Normal Nucleoli",
    "Mitoses","Class")
    data = getData("breast-cancer-wisconsin.data",names)
    x_train, x_test, y_train, y_test = split(data)
    st.write(data)


#let user choose which classifier to use
    st.sidebar.subheader("Choose Classifier")
    #select box is the streamlit equivalent of a drop down list. the options should be entered in douple
    classifier = st.sidebar.selectbox("Classifier", ("Support Vector Machine (SVM)", "Logisitic Regression", "Random Forest"))
    if classifier == "Support Vector Machine (SVM)":
        st.sidebar.subheader("Model Hyperparameters")
        C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0,step=0.01,key="C")
        Kernel = st.sidebar.radio("Kernel",("rbf","linear"),key="kernel")
        Gamma = st.sidebar.radio("Gamma (Kernel coefficient)",("Scale","Auto"),key="Gamma")
        #if you want to add more parameters to the app. read the sklearn document
        





if __name__ == '__main__':
    main()
