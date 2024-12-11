from django.contrib import admin
from .models import User, Teacher

class UserAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'email']
  search_fields = ['name', 'email']
  readonly_fields = ['created_at', 'updated_at']

admin.site.register(User, UserAdmin)
  
class TeacherAdmin(admin.ModelAdmin):
  list_display = ['id', 'user', 'school']
  search_fields = ['user']
  readonly_fields = ['created_at', 'updated_at']

admin.site.register(Teacher, TeacherAdmin)
