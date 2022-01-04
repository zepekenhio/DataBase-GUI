from django.db import models
from django.db.models.deletion import SET_DEFAULT
from .utils import create_new_ref_number
from django.contrib.auth.models import User

# Create your models here.

class Father(models.Model):
    full_name = models.CharField('full_name', max_length=120)
    occupation = models.CharField('occupation', max_length=120)
    marital_status = models.CharField('email', max_length=20)
    nni = models.CharField('nni', unique='True', max_length=10, editable=False, default=create_new_ref_number)
    
    def __str__(self):
        return f'{self.full_name} : {self.nni}'
    

class Mother(models.Model):
    full_name = models.CharField('full_name', max_length=120)
    occupation = models.CharField('occupation', max_length=120)
    marital_status = models.CharField('email', max_length=20)
    nni = models.CharField('nni', unique='True', max_length=10, editable=False, default=create_new_ref_number)
    
    def __str__(self):
        return f'{self.full_name} : {self.nni}'
    

class Child(models.Model):
    first_name = models.CharField('full_name', max_length=120)
    last_name = models.CharField('full_name', max_length=120)
    birth_time = models.TimeField('birth_time', )
    birth_date = models.DateField('birth_date', )
    birth_place = models.CharField('birth_place', blank=False, max_length=120)
    gender = models.CharField('gender', blank=False, max_length=120)
    nni = models.CharField('nni', unique='True', max_length=10, editable=False, default=create_new_ref_number)
    father = models.ForeignKey(Father, blank=False, null=False, on_delete=models.CASCADE)
    mother = models.ForeignKey(Mother, blank=False, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=SET_DEFAULT, default=None, null=True)
    def __str__(self):
        return self.fist_name