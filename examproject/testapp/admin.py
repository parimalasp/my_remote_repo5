from django.contrib import admin

from testapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empno','ename','sal','addr']
admin.site.register(Employee,EmployeeAdmin)
