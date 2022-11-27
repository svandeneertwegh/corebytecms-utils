from django.contrib import admin

from .models import TeamEmployee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'function', 'description']


admin.site.register(TeamEmployee, EmployeeAdmin)
