# models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)
    time_to_answer = models.IntegerField(default=60)
    unique_code = models.CharField(max_length=8)  # New field for storing unique code, adjust max_length as needed

    def __str__(self):
        return self.question_text

class UniqueCode(models.Model):
    code = models.CharField(max_length=20, unique=True)



class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
