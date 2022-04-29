from django.shortcuts import render
from testapp.models import Employee
def displayview(request):
    emp=Employee.objects.all()
    dict={'emp':emp}
    return render(request,'testapp/first.html',dict)
