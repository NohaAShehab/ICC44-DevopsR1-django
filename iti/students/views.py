from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

from students.models import  Student
""" function works when it receives http request"""
def helloworld(request):
    """ function must retrurn with http response"""
    return HttpResponse("<h1> Hello Devops <3 <3 <3 </h1>")


def index(request):
    ## get all objects from the database
    # models provide queryset apis --> get data from db --> through class ?
    stds = Student.objects.all()
    # select * from students
    # # object is table record

    print(stds)
    # you can send data to the template
    return render(request, 'index.html',context={"students":stds} )
