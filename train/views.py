from django.shortcuts import render
from .forms import DetailsForm
import pickle
import numpy as np


model=pickle.load(open('tmodel.pkl','rb'));

def form(request):
    boolean,output=False,0
    if request.method=='POST':
        form=DetailsForm(request.POST)
        if form.is_valid():
            test=[form.cleaned_data["pregnancies"],
            form.cleaned_data["glucose"],
            form.cleaned_data["bloodpressure"],
            form.cleaned_data["skinthickness"],
            form.cleaned_data["insulin"],
            form.cleaned_data["bmi"],
            form.cleaned_data["diabetespedgreefunction"],
            form.cleaned_data["age"],]
            final=[np.array(test)]
            prediction=model.predict_proba(final)
            output=float('{0:.{1}f}'.format(prediction[0][1], 2))*100
            boolean=True
            form=DetailsForm()
            return render(request,'form.html',{'form':form,'output':output,'boolean':boolean})
    else:
        form=DetailsForm()
        return render(request,'form.html',{'form':form,'output':output,'boolean':boolean})
