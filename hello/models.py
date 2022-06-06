import re
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,ProhibitNullCharactersValidator
from django.core.validators import ValidationError

def number_only( value ):
    if ( re.match( r'^[0-9]*$' , value )==None):
        raise ValidationError('%(value)s is not Number!',params={'value':value})

# Create your models here.
class Friend( models.Model ):
    name = models.CharField(max_length=100,validators=[number_only])
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(150)])
    birthday = models.DateField()

    