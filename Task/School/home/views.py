from django.shortcuts import render,redirect
from home.models import user,student,teacher,Image,StudentImage,TeacherImage
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from .forms import ImageForm,StudentForm,TeacherForm

# Create your views here.
def home(request):
    return render(request, 'dashboard.html')

def admindashboard(request):
    return render(request, 'admindashboard.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if user.objects.filter(email=email).exists():
            s=user.objects.get(email=email)
            pwd=s.password
            if check_password(password,pwd):
                return redirect('/admindashboard')
            else:
                return redirect('/login')
            
        else:
            return redirect('/signup')
            
    else:
        return render(request, 'login.html')

def studentlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if student.objects.filter(email=email).exists():
            s=student.objects.get(email=email)
            pwd=s.password
            if check_password(password,pwd):
                return redirect('/studentdashboard')
            else:
                return redirect('/studentlogin')
            
        else:
            return redirect('/studentlogin')
           
    else:
        return render(request, 'studentlogin.html')
    
def teacherlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if teacher.objects.filter(email=email).exists():
            s=teacher.objects.get(email=email)
            pwd=s.password
            if check_password(password,pwd):
                return redirect('/teacherdashboard')
            else:
                return redirect('/login')
            
        else:
            return redirect('/teachersignup')
            
    else:
        return render(request, 'teacherlogin.html')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        phoneno=request.POST['number']
        password=make_password(request.POST['password'])
        if user.objects.filter(email=email).exists():
            return redirect('/signup')
        else:
            user.objects.create(username=username,email=email,phoneno=phoneno,password=password)
            return redirect('/login')
    return render(request, 'signup.html')

def studentsignup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        phoneno=request.POST['number']
        password=make_password(request.POST['password'])
        if student.objects.filter(email=email).exists():
            return redirect('/signup')
        else:
            student.objects.create(sname=username,email=email,phoneno=phoneno,password=password)
            return redirect('/studentlogin')
    return render(request, 'studentsignup.html')

def teachersignup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        phoneno=request.POST['number']
        password=make_password(request.POST['password'])
        if teacher.objects.filter(email=email).exists():
            return redirect('/signup')
        else:
            teacher.objects.create(tname=username,email=email,phoneno=phoneno,password=password)
            return redirect('/teacherlogin')
    return render(request, 'teachersignup.html')

def studentdashboard(request):
    return render(request, 'studentdashboard.html')

def teacherdashboard(request):
    return render(request, 'teacherdashboard.html')


def photo(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = ImageForm()
        img = Image.objects.all()
        stu= StudentImage.objects.all()
        tea=TeacherImage.objects.all()
        return render(request, 'admindashboard.html', {'img':img,'stu':stu,'tea':tea, 'form':form})
    else:
        form = ImageForm()
        img = Image.objects.all()
        stu= StudentImage.objects.all()
        tea=TeacherImage.objects.all()
        return render(request, 'admindashboard.html', {'img':img,'stu':stu,'tea':tea, 'form':form})

def studentphoto(request):
    if request.method == "POST":
        form= StudentForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
        form=StudentForm()
        img=StudentImage.objects.all()
        return render(request, "studentdashboard.html",{"img":img, "form":form})
    else:
        form=StudentForm()
        img=StudentImage.objects.all()
        return render(request, "studentdashboard.html",{"img":img, "form":form})
    
def teacherphoto(request):
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = TeacherForm()
        pic = TeacherImage.objects.all()
        stu= StudentImage.objects.all()
        return render(request, 'teacherdashboard.html', {'pic': pic, 'stu':stu, 'form':form})
    else:
        form = TeacherForm()
        pic = TeacherImage.objects.all()
        stu= StudentImage.objects.all()
        return render(request, 'teacherdashboard.html', {'pic': pic, 'stu':stu, 'form':form})
