from django.db import models
from utils.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid



class User(AbstractBaseUser, BaseModel):
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False,
  )
  name = models.CharField(
    max_length=100,
    help_text='User name',
    verbose_name='Name',
  )
  email = models.EmailField(
    max_length=100,
    help_text='User email',
    verbose_name='Email',
    unique=True,
  )

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def __str__(self):
    return f"[{self.email}]: {self.name}."


class Teacher(BaseModel):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='teacher',
    verbose_name='User',
  )
  school = models.CharField(
    max_length=100,
    help_text='Teacher school',
    verbose_name='School',
  )

  def __str__(self):
    return f"{self.school} ==> [{self.user.email}]: {self.user.name}."
