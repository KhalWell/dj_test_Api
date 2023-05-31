from django.contrib import admin
from .models import Department, Job, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'father_name', 'pay', 'old'
    )
    list_display_links = (
         'first_name', 'last_name', 'father_name',
    )
    list_editable = (
        'pay',
    )
    list_filter = (
        'first_name', 'last_name', 'father_name',
    )
    search_fields = ('first_name', 'last_name', 'father_name',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title'
    )
    list_display_links = (
        'pk',
    )
    list_editable = (
        'title',
    )
    search_fields = ('title',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title'
    )
    list_display_links = (
        'pk',
    )
    list_editable = (
        'title',
    )
    search_fields = ('title',)