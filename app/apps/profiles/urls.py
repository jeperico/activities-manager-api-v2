from apps.profiles import api
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"user", api.UserViewSet)
router.register(r"teacher", api.TeacherViewSet)
router.register(r"register-teacher", api.TeacherRegister, basename="register-teacher")

urlpatterns = [
  path("", include(router.urls)),
]

