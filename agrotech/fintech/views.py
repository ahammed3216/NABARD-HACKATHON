from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm,Announcemnts
from django.contrib.auth import authenticate, login
from .models import *
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    orders=Announcement.objects.all()
    return render(request,'admin.html',{'orders':orders})


def customer(request):
    announcements=Announcement.objects.all()
    return render(request,'customer.html',{'orders':announcements})


def employee(request):
    return render(request,'employee.html')


def anno_form(request):
    form=Announcemnts(request.POST or None)
    order=Announcement()
   
    if form.is_valid():
        print (form.cleaned_data)
        title=form.cleaned_data.get('title')
        description=form.cleaned_data.get('description')
        start_date=form.cleaned_data.get('start_date')
        end_date=form.cleaned_data.get('end_date')
        amount=form.cleaned_data.get('amount')

        print('end date',end_date)

        def change_format(date):
            print(date)
            date_new=date.split('/')
            date=date_new[::-1]
            ret_date=''
            for i in date:
                ret_date=ret_date+i
                ret_date=ret_date+'-'
            ret_date=ret_date[:-1]
            return ret_date

        
        date1=change_format(start_date)
        date2=change_format(end_date)
        order.amount=amount
        order.start_date=date1
        order.end_date=date2
        order.description=description
        order.title=title

        order.save()
        return redirect('/')

    print("hello")
    return render(request,'ann_form.html')


def application(request):
    return render(request,"application.html")