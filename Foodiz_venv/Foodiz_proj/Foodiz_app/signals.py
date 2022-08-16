import profile
from django.db.models.signals import pre_save ,post_save
from django.dispatch import receiver
from django.db import models
from .models import Profile, User
from django.contrib.auth import get_user_model
from django.conf import settings

# Remove used imports

User = get_user_model()

@receiver(post_save, sender = User)
def creat_or_save_user_profile(sender, created, instance, **kwargs): # spelling issue in function name
    if created == True: # created is a bool, no need to add == True
        Profile.objects.create(user = instance)
    instance.profile.save() # there is no need for this, the create method is enough and will save it to the database