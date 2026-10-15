from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save,sender=User)
def User_saved(sender,instance,created,**kwargs):
    if created:
        print("New User Created: ",instance.name)
    else:
        print("Student Updated: ",instance.name)
    