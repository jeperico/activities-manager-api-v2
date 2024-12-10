from django.db import models

class User(models.Model):
  name = models.CharField(
    max_length=100, help_text='Name of the user', verbose_name='Name'
  )
  password = models.CharField(
    max_length=100, help_text='Password of the user', verbose_name='Password'
  )
  created_at = models.DateTimeField(
    auto_now_add=True, verbose_name='Created At', help_text='Created At'
  )
  updated_at = models.DateTimeField(
    auto_now=True, verbose_name='Updated At', help_text='Updated At'
  )

    def __str__(self):
      return 
    self.name
