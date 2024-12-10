from .models import User, Teacher
from .serializers import {
  UserReadOnlySerializer,
  UserCompleteReadOnlySerializer,
  UserRegisterSerializer,
  TeacherReadOnlySerializer,
  TeacherRegisterSerializer,
}
from rest_framework import (
  generics,
  mixins,
  permissions,
  response,
  status,
  views,
  viewsets,
)
