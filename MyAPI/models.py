from django.db import models

class approval(models.Model):
    GENDER_CHOICES =(
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    MARRIED_CHOICES =(
        ('Yes','Yes'),
        ('No','No')
    )
    GRADUATED_CHOICES =(
        ('Graduate','Graduated'),
        ('Not_Graduate','Not_Graduated')
    )
    SELFEMPLOYED_CHOICES =(
        ('Yes','Yes'),
        ('No','No')
    )
    PROPERTY_CHOICES =(
        ('Rural','Rural'),
        ('Semiurban','Semiurban'),
        ('Urban','Urban')
    )

    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    dependants = models.IntegerField(default=0)
    applicantIncome=models.IntegerField(default=0)
    coapplicantIncome=models.IntegerField(default=0)
    loanAmount=models.IntegerField(default=0)
    loanTerm=models.IntegerField(default=0)
    creditHistory=models.IntegerField(default=0)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    graduatedEducation = models.CharField(max_length=15, choices=GRADUATED_CHOICES)
    selfEmployed = models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES)
    area = models.CharField(max_length=15, choices= PROPERTY_CHOICES)

    def __str__(self):
        return self.firstName, self.lastName