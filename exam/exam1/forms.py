# forms.py
from django import forms
from .models import User

class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200)
    option1 = forms.CharField(max_length=100)
    option2 = forms.CharField(max_length=100)
    option3 = forms.CharField(max_length=100)
    option4 = forms.CharField(max_length=100)
    correct_option = forms.ChoiceField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3'), ('option4', 'Option 4')])
    time_to_answer = forms.IntegerField(initial=60)
    unique_code = forms.CharField(max_length=20)  # Initial time to answer is 60 seconds

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
