from django.shortcuts import render, HttpResponse, redirect
from libapp.models import Book
from django.db.models import Q
from libapp.forms import StudentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from libapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def about(request):
    return render(request,'about.html')

@login_required
def books(request):
    userid=request.user.id
    user_name=request.user.username
    if request.method=="POST":
        bn=request.POST['bname']
        a=request.POST['author']
        p=request.POST['price']
        i=request.POST['isbn']
        d=request.POST['desc']
        up=request.POST['upload']
        bl=request.POST['book_link']
      
        b=Book.objects.create(bname=bn,author=a,price=p,isbn=i,desc=d,is_deleted="1",upload=up,book_link=bl,uid=userid,uname=user_name)
        #print(p)
        b.save()
        return redirect('/')
    else:
        return render(request,'books.html')

@login_required
def udashboard(request):
    userid=request.user.id
    user_name=request.user.username
    # rec=Book.objects.all()
    q1=Q(is_deleted=1)
    q2=Q(uid=userid)
    q3=Q(uname=user_name)
    rec=Book.objects.filter(q1 & q2 & q3)
    content={}
    content['data']=rec
    return render(request,'dashboard.html',content)

@login_required
def delete(request,rid):
    # b=Book.objects.get(id=rid)
    # b.delete()
    b=Book.objects.filter(id=rid)
    b.update(is_deleted="0")
    return redirect('/')

@login_required
def edit(request,rid):
    if request.method=="POST":
        ubname=request.POST['bname']
        uauthor=request.POST['author']
        uprice=request.POST['price']
        uisbn=request.POST['isbn']
        udesc=request.POST['desc']
        uup=request.FILES['upload']
        ubl=request.POST['book_link']

        b=Book.objects.filter(id=rid)
        b.update(bname=ubname,author=uauthor,price=uprice,isbn=uisbn,desc=udesc,upload=uup,book_link=ubl)

        return redirect('/')

    else:
        b=Book.objects.get(id=rid)
        # print(b)
        content={}
        content['data']=b
        return render(request,'edit.html',content)

def index(request):
    rec=Book.objects.filter(is_deleted=1).order_by('-dt')
    
    page = request.GET.get('page', 1)
  
    paginator = Paginator(rec, 3)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    content={
        'data':rec,
        'books':books,
    }
    res= render(request,'index.html',content)
    res.set_cookie('bname',content['data'])
    return res

def getcookies(request):
    content={}
    content['bn']=request.COOKIES['bname']
    return render(request,'getcookies.html',content)

def book_info(request):
    rec=Book.objects.filter(is_deleted=1)
    content={}
    content['data']=rec
    return render(request,'book_info.html',content)

def studentform(request):
    fm=StudentForm()
    content={}
    content['form']=fm
    return render(request,'studentform.html',content)

def user_register(request):
    if request.method=="POST":
        # fm=UserCreationForm(request.POST)
        fm=UserForm(request.POST)
        if fm.is_valid():
            fm.save()#inserting username and password in auth_user table
            return HttpResponse("User Created Successfully!!!")
        else:
            return HttpResponse("Failed to create user")
    else:
        # fm=UserCreationForm()
        fm=UserForm()
        content={}
        content['form']=fm
        return render(request,'register.html',content)

def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(data=request.POST)
        if fm.is_valid():
            user=fm.get_user()
            login(request,user)
            return redirect('/udashboard')
    else:
        fm=AuthenticationForm()
        return render(request,'login.html',{"form":fm})

def user_logout(request):
    logout(request)
    return redirect('/')
