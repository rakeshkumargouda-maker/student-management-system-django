from django.shortcuts import redirect, render

from .models import Student

def home(request):
    return render(request, 'students/index.html')

def dashboard(request):
    return render(request, 'students/dashboard.html')

def addstudent(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        age = request.POST.get("age")
        course = request.POST.get("course")
        email = request.POST.get("email")

        student = Student(name=name, roll=roll, age=age, course=course, email=email)
        student.save()
        return redirect("viewstudents")

    return render(request, 'students/addstudent.html')
       
def viewstudents(request):
    students = Student.objects.all()
    return render(request, 'students/viewstudents.html', {"students": students})