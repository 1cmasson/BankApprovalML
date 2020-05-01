from django import forms

class ApprovalForm(forms.Form):
        First_Name=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
        Last_Name=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))
        Dependants=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Number of Dependents'}))
        Applicant_Income=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Monthly Gross Income'}))
        Coapplicant_Income=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Co-Applicant Monthly Gross Income'}))
        Loan_Amount=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Requested Loan Amount'}))
        Loan_Amount_Term=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Loan Term in Months'}))
        Credit_History=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Last Credit Rating'}))
        Credit_History=forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3', 3)])
        Gender=forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')])
        Married=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
        Education=forms.ChoiceField(choices=[('Graduate', 'Graduate'),('Not_Graduate', 'Not_Graduate')])
        Self_Employed=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
        Property_Area=forms.ChoiceField(choices=[('Rural', 'Rural'),('Semiurban', 'Semiurban'),('Urban', 'Urban')])
        
