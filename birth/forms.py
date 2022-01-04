from django import forms
from django.forms import ModelForm
from .models import Father, Mother, Child


class FatherForm(ModelForm):
    class Meta:
        model = Father
        fields= ('full_name', 'occupation', 'marital_status', )

        labels = {
            'full_name': '',  
            'occupation': '',
            'marital_status': '', 
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom et prenom',}),  
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation',}),
            'marial_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status Matrimonial',}), 
            'marial_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status Matrimonial',}), 
        }
        

class MotherForm(ModelForm):
    class Meta:
        model = Mother
        fields= ('full_name', 'occupation', 'marital_status', )

        labels = {
            'full_name': '',  
            'occupation': '',
            'marital_status': '', 
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom et prenom',}),  
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation',}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation',}),
        }



class ChildForm(ModelForm):
    class Meta:
        model = Child
        fields = ( 'first_name', 'last_name', 'birth_time', 'birth_date', 'birth_place', 'gender', 'father', 'mother', 'user',  )

        labels = {
            'first_name': '',
            'last_name': '',
            'birth_time': '',
            'birth_date': '', 
            'birth_place': '',  
            'gender': '',    
            'father': 'Selectionner le père', 
            'mother': 'Selectionner la mere', 
            'user': '', 
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom',}),
            'birth_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Heur de naissance',}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date de naissance',}),
            'birth_place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu de naissance',}),  
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre',}), 
            'father': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choisir le Père',}), 
            'mother': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choisir la Mère',}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User ID',}), 
        }

