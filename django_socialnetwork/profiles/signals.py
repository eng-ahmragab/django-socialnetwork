from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile




# signal (post_save): gets fired after an object gets saved
# signal sender (User Model): Fires up the signal when an event occurs
# signal receiver: Listens for the signal and performs a task


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(f"[*] post_save signal: create_profile(sender={sender}, instance={instance})")
    #Create a new Profile object
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print(f"[*] post_save signal: save_profile(sender={sender}, instance={instance})")
    # set the profile of field of the user instance
    instance.profile.save()








