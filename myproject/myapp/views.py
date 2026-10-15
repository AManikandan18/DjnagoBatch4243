from django.shortcuts import render
from .models import Student,Students,Course,User # . means current Folder/App

# Create your views here.
def home(request):
    return render(request, "home.html")

# student = Student(
#     name="Raju",
#     age=23,
#     email="Raju@gmail.com",
#     course="Python",
#     mark=85
# )
# student.save()

# Student.objects.create(
#     name="Mani",
#     age=23,
#     email="mani@gmail.com",
#     course="Python",
#     mark=85
# )

# Without Select Related:
# student = Students.objects.all() #1
# # print(student)  #QuerySet

# for std in student:
#     print(std.name,std.course.name) #3  = n+1
    
# With Select Related:
# student = Students.objects.select_related("course") #1
# print(student)
# for std in student:
#     print(std.name,std.course.name) #1

#without Prefetch_related():
# courses = Course.objects.all()

# for course in courses:
#     for student in course.students.all():
#         print(course.name,student.name)
        
# For every course, course.students.all() may trigger another query.

# If there are 20 courses, this could mean approximately 21 queries.

# courses = Course.objects.prefetch_related("students")

# for course in courses:
#     for student in course.students.all():
#         print(course.name, student.name)


# User.objects.create(name = "Raj",age = 23)
# User.objects.filter(id = 1).update(name = "Kavin Kumar")
# user_date = User.objects.create(
#     name = "Naveen",
#     age = 20
# )

# user_date.name = "Naveen Kumar"
# user_date.save()