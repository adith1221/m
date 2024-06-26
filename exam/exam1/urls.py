# urls.py
from django.urls import path
from .views import create_questions,take_exam,dashboard,enter_code,home,unique_code,view_questions,signup,user_login

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create/', create_questions, name='create_questions'),
    path('take_exam/', take_exam, name='take_exam'),
    path('enter_code/', enter_code, name='enter_code'),
    path('home/',home,name='home'),
    path('unique_code/',unique_code,name='unique_code'),
    path('view_questions/',view_questions,name='view_questions'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),


   
]
