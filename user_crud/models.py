from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail



# Create your models he

class profile(models.Model):
    gender_choice  = (
        ('M','Male'),
        ('F','Female'),
        ('O','Others'),

               )
    user        = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name        = models.CharField(max_length=100,blank=False,null=False)
    age         = models.IntegerField()
    gender      = models.CharField(max_length=5,blank=False,null=False,choices=gender_choice)
    immage      = models.ImageField(upload_to='immage/%m')
    created_at  = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_at  = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.name


@receiver(post_save,sender=profile)
def After_save(sender,instance,*args,**kwargs):
    send_mail('Success mail', 'Your profile is created successfully ', 'kumarpandamanoja@gmail.com',[instance.user.email])



