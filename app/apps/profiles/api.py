# from .models import User, Teacher
# from .serializers import {
#   UserReadOnlySerializer,
#   UserCompleteReadOnlySerializer,
#   UserRegisterSerializer,
#   TeacherReadOnlySerializer,
#   TeacherRegisterSerializer,
# }
# from rest_framework import (
#   generics,
#   mixins,
#   permissions,
#   response,
#   status,
#   views,
#   viewsets,
# )
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from rest_framework import filters


# class UserViewSet(
#   mixins.RetrieveModelMixin,
#   mixins.UpdateModelMixin,
#   mixins.DestroyModelMixin,
#   mixins.LisModelMixin,
#   viewsets.GenericViewSet
# ):
#   serializer_class = UserCompleteReadOnlySerializer
#   queryset = User.objects.all()
#   filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#   search_fields = ["name"]
  
#   def get_serializer_class()
