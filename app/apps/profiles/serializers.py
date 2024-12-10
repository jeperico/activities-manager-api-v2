from .models import User, Teacher
from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.password_validation import validate_password

class UserReadOnlySerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "last_name", "first_name", "email", "created_at", "updated_at"]


class UserCompleteReadOnlySerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "name", "email", "created_at", "updated_at"]


class UserRegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only=True,
    required=True,
    validators=[validate_password],
  )

  class Meta:
    model = User
    fields = ["id", "last_name", "first_name", "email", "password", "created_at", "updated_at"]
    extra_kwargs = {
      "password": {"write_only": True},
      "id": {"read_only": True},
    }

  def create(self, validated_data):
    with transaction.atomic():
      first_name = validated_data.get(
        "first_name", ""
      )
      last_name = validated_data.get(
        "last_name", ""
      )
      password = validated_data.pop("password")
      user = User.objects.create(**validated_data)
      user.set_password(password)
      user.name = (
        f"{first_name} {last_name}".strip()
      )
      user.save()

      return user


class TeacherReadOnlySerializer(serializers.ModelSerializer):
  user = UserRegisterSerializer(required=True)

  class Meta:
    model = Teacher
    fields = ["id", "user", "school", "created_at", "updated_at"]


class TeacherRegisterSerializer(serializers.ModelSerializer):
  user = UserRegisterSerilizer(required=True)

  class Meta:
    model = Teacher
    fields = '__all__'
    extra_kwargs = {
      "id": {"read_only":True}
    }
  
  def create(self, validated_data):
    user_data = validated_data.pop("user")

    user_serializer = UserRegisterSerializer(data=user_data)

    if user_serializer.is_valid():
      user = user_serializer.save()

      teacher = Teacher.objects.create(user=user, **validated_data)
      
      return admin
    else:
      raise serializers.ValidationError(user_serializer.errors)
