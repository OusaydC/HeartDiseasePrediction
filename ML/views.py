from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from . models import Features
from . forms import HeartDiseaseCheckerForm
import joblib
import pickle
import pandas as pd
import os
import numpy as np
CURRENT_DIR = os.path.dirname(__file__)
knn_model = os.path.join(CURRENT_DIR, 'models/knn.pkl')
knn = joblib.load(knn_model)

ann_model = os.path.join(CURRENT_DIR, 'models/knn.pkl')
ann = joblib.load(ann_model)

lstm_model = os.path.join(CURRENT_DIR, 'models/svm.pkl')
lstm = joblib.load(lstm_model)

lr_model = os.path.join(CURRENT_DIR, 'models/lr.pkl')
lr = joblib.load(lr_model)

svm_model = os.path.join(CURRENT_DIR, 'models/svm.pkl')
svm = joblib.load(svm_model)

dt_model = os.path.join(CURRENT_DIR, 'models/dt.pkl')
dt = joblib.load(dt_model)

rf_model = os.path.join(CURRENT_DIR, 'models/rf.pkl')
rf = joblib.load(rf_model)


# Create your views here.

def home(request):
    return render(request,'home.html')
def MachineLearning(request):
    return render(request,'index.html')
def ANN(request):
    return render(request,'indexAnn.html')
def LSTM(request):
    return render(request,'indexLSTM.html')

def result(request):
    data = []
    age = request.POST['age']
    sex = request.POST['sex']
    cp = request.POST['cp']
    trestbps = request.POST['trestbps']
    chol = request.POST['chol']
    fbs = request.POST['fbs']
    restecg = request.POST['restecg']
    thalach = request.POST['thalach']
    exang = request.POST['exang']
    oldpeak = request.POST['oldpeak']
    slope = request.POST['slope']
    ca = request.POST['ca']
    thal = request.POST['thal']
    data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    knn_result = knn.predict(data)
    lr_result = lr.predict(data)
    svm_result = svm.predict(data)
    dt_result = dt.predict(data)
    rf_result = rf.predict(data)

    # df = pd.DataFrame(data)
    # xgb_result = xgb.predict(df)
    # if (checker == 1):
    #    messages.warning(request, 'Unhealthy....!')
    #if (checker == 0):
        #   messages.success(request, 'Healthy')
    return render(request,'result.html',{"lr":lr_result,'knn':knn_result,"svm":svm_result,"dt":dt_result,"rf":rf_result})

def resultAnn(request):
    data = []
    age = request.POST['age']
    sex = request.POST['sex']
    cp = request.POST['cp']
    trestbps = request.POST['trestbps']
    chol = request.POST['chol']
    fbs = request.POST['fbs']
    restecg = request.POST['restecg']
    thalach = request.POST['thalach']
    exang = request.POST['exang']
    oldpeak = request.POST['oldpeak']
    slope = request.POST['slope']
    ca = request.POST['ca']
    thal = request.POST['thal']
    data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

    ann_result = ann.predict(data)
    return render(request,'indexAnn.html',{"ann":ann_result})


def resultLSTM(request):
    data = []
    age = request.POST['age']
    sex = request.POST['sex']
    cp = request.POST['cp']
    trestbps = request.POST['trestbps']
    chol = request.POST['chol']
    fbs = request.POST['fbs']
    restecg = request.POST['restecg']
    thalach = request.POST['thalach']
    exang = request.POST['exang']
    oldpeak = request.POST['oldpeak']
    slope = request.POST['slope']
    ca = request.POST['ca']
    thal = request.POST['thal']
    data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

    lstm_result = lstm.predict(data)
    return render(request,'resultLSTM.html',{"lstm":lstm_result})