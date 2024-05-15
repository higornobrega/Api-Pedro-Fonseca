from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class Profile(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    cpf = models.CharField(max_length=50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []