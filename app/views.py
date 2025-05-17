from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from .forms import HeartDiseaseForm
import os
from django.conf import settings

# Load and train model once
try:
    csv_path = os.path.join(settings.STATICFILES_DIRS[0], 'Heart_train.csv')
    if not os.path.exists(csv_path):
        csv_path = os.path.join(settings.STATIC_ROOT, 'Heart_train.csv')
    df = pd.read_csv(csv_path)
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1].ravel()
    rf = RandomForestClassifier(n_estimators=16, criterion='entropy', max_depth=9)
    rf.fit(np.nan_to_num(X), Y)
except FileNotFoundError:
    rf = None

def heart(request):
    value = ''
    form = HeartDiseaseForm()

    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            if rf is None:
                value = 'Error: Model not available'
            else:
                user_data = np.array([
                    form.cleaned_data['age'],
                    form.cleaned_data['sex'],
                    form.cleaned_data['cp'],
                    form.cleaned_data['trestbps'],
                    form.cleaned_data['chol'],
                    form.cleaned_data['fbs'],
                    form.cleaned_data['restecg'],
                    form.cleaned_data['thalach'],
                    form.cleaned_data['exang'],
                    form.cleaned_data['oldpeak'],
                    form.cleaned_data['slope'],
                    form.cleaned_data['ca'],
                    form.cleaned_data['thal'],
                ]).reshape(1, 13)

                predictions = rf.predict(user_data)
                value = 'have' if predictions[0] == 1 else "don't have"

    return render(request, 'heart.html', {
        'context': value,
        'title': 'Heart Disease Prediction',
        'form': form,
    })

def home(request):
    return render(request, 'home.html')