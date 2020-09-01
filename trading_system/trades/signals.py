from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
