from django.shortcuts import render
from . forms import ApprovalForm
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from . models import approval
from . serializers import approvalsSerializers
from keras import backend as K
import pickle
import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict,Counter
from django.contrib import messages
class ApprovalsView(viewsets.ModelViewSet):
    queryset = approval.objects.all()
    serializer_class = approvalsSerializers

def ohevalue(df):
    ohe_col=joblib.load("/Users/Hp User/Documents/Python/Django/BankLoanApprovalML/MyAPI/allcol.pkl")
    cat_columns=['Gender', 'Married', 'Education','Self_Employed','Property_Area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict={}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i]=df_processed[i].values
        else:
            newdict[i]=0
    newdf = pd.DataFrame(newdict)
    return newdf

#@api_view(["POST"])
def approvereject(unit):
    try:
        mdl = joblib.load("/Users/Hp User/Documents/Python/Django/BankLoanApprovalML/MyAPI/loan_model.pkl")
        scalers = joblib.load("/Users/Hp User/Documents/Python/Django/BankLoanApprovalML/MyAPI/scalers.pkl")
        X=scalers.transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred > 0.58)
        newdf=pd.DataFrame(y_pred, columns = ['Status'])
        newdf = newdf.replace({True: 'Approved', False:'Rejected'})
       
        return (newdf.values[0][0])
    except ValueError as e:
        return Response(e.args[0])

def cxcontact(request):

    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            Firstname = form.cleaned_data['First_Name']
            Lastname = form.cleaned_data['Last_Name']
            Dependants = form.cleaned_data['Dependants']
            ApplicantIncome = form.cleaned_data['Applicant_Income']
            CoapplicantIncome = form.cleaned_data['Coapplicant_Income']
            Loan_Amount = form.cleaned_data['Loan_Amount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            answer = approvereject(ohevalue(df))
            Xscalers = approvereject(ohevalue(df))
            if int(df['Loan_Amount'])<25000:
                messages.success(request,'Application Status: {}'.format(answer))
            else:
                messages.success(request,'Your Loan Request Exceeds $25,000 Limit')

    form= ApprovalForm() 

    return render(request, 'myform/cxform.html', {'form':form})

def cxcontact2(request):

    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            Firstname = form.cleaned_data['firstname']
            Lastname = form.cleaned_data['lastname']
            Dependants = form.cleaned_data['Dependants']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
            Loan_Amount = form.cleaned_data['Loan_Amount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            answer = approvereject(ohevalue(df))
            messages.success(request,'Application Status: {}'.format(answer))
            

            


    form= ApprovalForm() 

    return render(request, 'myform/cxform.html', {'form':form})