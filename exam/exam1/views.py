from django.shortcuts import render, redirect
from .models import Question,UniqueCode
from .forms import QuestionForm,LoginForm,SignupForm
from django.db.models import Sum
import random,string
from django.contrib.auth import authenticate, login

def dashboard(request):
    return render(request, 'dashboard.html')
def home(request):
    return render(request,'home.html')

def enter_code(request):
    return render(request,'enter_code.html')   


def create_questions(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question_text']
            option1 = form.cleaned_data['option1']
            option2 = form.cleaned_data['option2']
            option3 = form.cleaned_data['option3']
            option4 = form.cleaned_data['option4']
            time_to_answer = form.cleaned_data['time_to_answer']
            unique_code = form.cleaned_data['unique_code'] 

            correct_option = form.cleaned_data['correct_option']
            question = Question(
                question_text=question_text,
                option1=option1,
                option2=option2,
                option3=option3,
                option4=option4,
                correct_option=correct_option,
                time_to_answer=time_to_answer,  
                unique_code=unique_code
            )
            question.save()
            return redirect('create_questions')  
    else:
        form = QuestionForm()
    return render(request, 'create_questions.html', {'form': form})

def take_exam(request):
    if request.method == 'POST':
        unique_code = request.POST.get('code')
        questions = Question.objects.filter(unique_code=unique_code)
        total_time = questions.aggregate(total_time=Sum('time_to_answer'))['total_time']
        return render(request, 'take_exam.html', {'questions': questions, 'total_time': total_time, 'unique_code': unique_code})
    else:
        return render(request, 'enter_code.html')
        

def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'view_questions.html', {'questions': questions})

def unique_code(request):
    unique_code = None
    while not unique_code:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if not UniqueCode.objects.filter(code=code).exists():
            unique_code = UniqueCode.objects.create(code=code)

    return render(request, 'unique_code.html', {'unique_code': unique_code.code})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
