#this file is needed to create a profile for each new user isntaed of 
#manually creating it from admin panel

# from django.db.models.signals import post_save
# #this is a signal that get fired after an object is saved

# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile


# #the idea is to create a new profile(reciever model) for each new created user(sender model)


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)



# #then another signal to save profile in database
# @receiver(post_save, sender=User)
# def save_profile(sender, instance,created, **kwargs):
#     instance.profile.save()

#remember signal are added in app.py