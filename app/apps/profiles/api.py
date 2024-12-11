from .models import User, Teacher
from .serializers import (
  UserReadOnlySerializer,
  UserRegisterSerializer,
  TeacherReadOnlySerializer,
  TeacherRegisterSerializer,
)
from rest_framework import (
  generics,
  mixins,
  permissions,
  response,
  status,
  views,
  viewsets,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import filters



class UserViewSet(
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  mixins.ListModelMixin,
  viewsets.GenericViewSet,
):
  queryset = User.objects.all()
  serializer_class = UserReadOnlySerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  search_fields = ['name', 'email']

  def get_serializer_class(self):
    return self.serializer_class

  def get_queryset(self):
    if self.request.user.is_superuser:
      return self.queryset
    return self.queryset.filter(id=self.request.user.id)

  def retrieve(self, request, *args, **kwargs):
    instance = User.objects.get(id=request.user.id)
    serializer = UserReadOnlySerializer(instance)
    return Response(serializer.data)

  def update(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


class UserRegister(
  mixins.CreateModelMixin,
  viewsets.GenericViewSet,
):
  queryset = User.objects.all()
  serializer_class = UserRegisterSerializer
  permission_classes = [permissions.AllowAny]
  
  def perform_create(self, serializer):
    res = super().perform_create(serializer)
    return res


class TeacherViewSet(viewsets.ModelViewSet):
  queryset = Teacher.objects.all()
  serializer_class = TeacherReadOnlySerializer
  filter_backends = [DjangoFilterBackend, SearchFilter]
  search_fields = ['user__name', 'user__email']


class TeacherRegister(
  mixins.CreateModelMixin,
  viewsets.GenericViewSet,
):
  queryset = Teacher.objects.all()
  serializer_class = TeacherRegisterSerializer
  permission_classes = [permissions.AllowAny]
  
  def perform_create(self, serializer):
    res = super().perform_create(serializer)
    return res
