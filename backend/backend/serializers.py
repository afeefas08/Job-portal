from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Job

class RegisterSerializer(serializers.ModelSerializer): # User model serializing.
    email = serializers.EmailField(required=True)  #making required.  

    class Meta: # which model, and what are the fields
        model = User
        fields = ['username','email','password'] #api access for particular fields only

class JobsSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField() #user data

    class Meta:
        model = Job
        fields = "__all__"
