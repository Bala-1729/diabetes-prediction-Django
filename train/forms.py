from django import forms

class DetailsForm(forms.Form):
    pregnancies=forms.IntegerField(label='Pregnancies')
    glucose=forms.IntegerField(label='Glucose Level')
    bloodpressure=forms.IntegerField(label='Blood Pressure')
    skinthickness=forms.IntegerField(label='Skin Thickness')
    insulin=forms.IntegerField(label='Insulin Level')
    bmi=forms.FloatField(label='BMI Value')
    diabetespedgreefunction=forms.FloatField(label='Diabetes Pedigree Function')
    age=forms.IntegerField(label='Age')
