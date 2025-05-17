from django import forms

class HeartDiseaseForm(forms.Form):
    age = forms.FloatField(label='Age (years)', min_value=0, max_value=120, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}), help_text='Enter age in years (e.g., 50).')
    sex = forms.ChoiceField(label='Sex', choices=[(0, 'Female'), (1, 'Male')], widget=forms.Select(attrs={'class': 'form-control'}), help_text='Select biological sex.')
    cp = forms.ChoiceField(label='Chest Pain Type (CP)', choices=[(0, 'Typical angina'), (1, 'Atypical angina'), (2, 'Non-anginal pain'), (3, 'Asymptomatic')], widget=forms.Select(attrs={'class': 'form-control'}), help_text='Select type of chest pain.')
    trestbps = forms.FloatField(label='Resting Blood Pressure (TRESTBPS, mm Hg)', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}), help_text='Enter resting blood pressure (e.g., 120).')
    chol = forms.FloatField(label='Serum Cholesterol (CHOL, mg/dl)', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}), help_text='Enter cholesterol level (e.g., 200).')
    fbs = forms.ChoiceField(label='Fasting Blood Sugar (FBS)', choices=[(0, '≤ 120 mg/dl'), (1, '> 120 mg/dl')], widget=forms.Select(attrs={'class': 'form-control'}), help_text='Fasting blood sugar > 120 mg/dl?')
    restecg = forms.ChoiceField(label='Resting ECG Results (RESTECG)', choices=[(0, 'Normal'), (1, 'ST-T wave abnormality'), (2, 'Left ventricular hypertrophy')], widget=forms.Select(attrs={'class': 'form-control'}), help_text='Select ECG result.')
    thalach = forms.FloatField(label='Maximum Heart Rate (THALACH, bpm)', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}), help_text='Enter max heart rate (e.g., 150).')
    exang = forms.ChoiceField(label='Exercise-Induced Angina (EXANG)', choices=[(0, 'No'), (1, 'Yes')], widget=forms.Select(attrs={'class': 'form-control'}), help_text='Angina during exercise?')
    oldpeak = forms.FloatField(label='ST Depression (OLDPEAK, mm)', min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}), help_text='Enter ST depression (e.g., 1.0).')
    slope = forms.ChoiceField(label='ST Segment Slope (SLOPE)', choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')], widget=forms.Select(attrs={'class': 'form-control'}), help_text='Select ST segment slope.')
    ca = forms.FloatField(label='Major Vessels Colored (CA)', min_value=0, max_value=4, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}), help_text='Number of vessels (0-4).')
    thal = forms.ChoiceField(label='Thalassemia (THAL)', choices=[(0, 'Normal'), (1, 'Fixed defect'), (2, 'Reversible defect')], widget=forms.Select(attrs={'class': 'form-control'}), help_text='Select thalassemia type.')