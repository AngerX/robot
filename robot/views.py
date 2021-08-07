from django.core.checks import messages
from django.forms.widgets import PasswordInput
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *
from django import forms
from robot import models, forms
from django.shortcuts import redirect
from .models import *
from django.contrib import messages
from .forms import SignupForm
from django.core.files.storage import FileSystemStorage

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()

#from django import forms


def index(request, name, password):
    individual = Userdata.objects.get(name = name, password = password)
    n = 0
    return render(request, 'index.html', locals())

def login(request):
    userdatas = Userdata.objects.all()
    return render(request, 'Login.html', locals())

def logout(request):
    return redirect('/')

def signup(request):
    if request.method == 'POST': #如果收到表單提交
        signup_form = forms.SignupForm(request.POST, request.FILES)
        if signup_form.is_valid():#如果每個內容都有填入的話
            signup_name = request.POST['username'].strip() #.strip()代表去掉左右的空白(space)，怕使用者打密碼時案到空白建
            signup_year = request.POST['year']
            signup_month = request.POST['month']
            signup_day = request.POST['day']
            signup_gender = request.POST['gender']
            signup_image = request.FILES['Photos'] #取得表單(forms)中的內容
            print(signup_image.name) #於終端機輸出圖片名稱
            print(signup_image.size) #於終端機輸出圖片大小(bytes)
            print(signup_image)
            #fs = FileSystemStorage()
            #sfs.save(signup_image.name, signup_image) 這兩行會直接將圖片存在media底下
            try:
                user = models.Userdata.objects.get(name = signup_name, year = signup_year, month = signup_month, day = signup_day, gender = signup_gender)
                message = '帳號已存在'
            except:
                signup_password = str(signup_year) + str(signup_month) + str(signup_day)
                user = Userdata.objects.create(name = signup_name, year = signup_year, month = signup_month, day = signup_day, gender = signup_gender, password = signup_password, image = signup_image)
                user.save()
                return redirect('/')
                #messages.add_message(request, messages.WARNING, '無此帳號')
        else:
            message = '請檢查欄位'
            #messages.add_message(request, messages.INFO, '請檢查欄位')
    else:
        signup_form = forms.SignupForm() #若表單還沒提交，用signup_form存forms的SignupForm內容後交給html顯示
    return render(request, 'SignUp.html', locals())

def testpage(request, n, name, password):
    name = name
    password = password
    
    n += 1
    if n == 6:
        return redirect('/index/'+name+'/'+password+'/')
    return render(request, 'testpage.html',locals())

def introduction(request, name, password):
    userdatas = Userdata.objects.all()
    individual = Userdata.objects.get(name = name, password = password)
    n = 0
    return render(request, 'introduction.html', locals())

# Create your views here.




