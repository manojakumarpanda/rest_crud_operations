from rest_framework import serializers
from django.contrib.auth.models import User
from .models import profile
from rest_framework.exceptions import ValidationError




class User_serialiser(serializers.Serializer):
    username    = serializers.CharField(max_length=100,allow_blank=False,allow_null=False)
    password    = serializers.CharField(max_length=100,allow_blank=False,allow_null=False)
    email       = serializers.EmailField(max_length=100)



class profile_serialiser(serializers.ModelSerializer):
    user=User_serialiser(many=False,read_only=True)

    def validate(self, data):
        name    =data['name']
        age     =data['age']
        gender  =data['gender']
        immage  =data['immage']
        if not name:
            raise ValidationError('The name must require')
        if not age and age>0:
            raise ValidationError('The age must require and shoud be greater then 0')
        if not gender and gender not in ('M','F','O'):
            raise ValidationError('The gender need to be selected')
        if not immage:
            raise ValidationError('The immage need to be uploaded')
        return data


    class Meta:
        model=profile
        fields=['id','user','name','age','gender','immage']

    def create(self, validated_data):
        try:
            user_data=validated_data.pop('user')
            password=user_data.pop('password')
            user=User(**user_data)
            user.set_password(raw_password=password)
            user.save()
            profile_data=profile.objects.get_or_create(user=user,**validated_data)
        except ValueError:
            raise ValueError('The data is in appropriate for this field')
        except KeyError:
            raise ValueError('You have selected a wrong key select a valid one')
        except:
            raise ValidationError('There something went wrong please try again')
        return profile_data


    def update(self, instance, validated_data):
        instance.name   =validated_data.get('name',instance.name)
        instance.age    =validated_data.get('age',instance.age)
        instance.gender =validated_data.get('gender',instance.gender)
        instance.immage   =validated_data.get('immage',instance.immage)
        instance.save()

        return instance

