from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from gcm.models import Device


class User(AbstractUser):
    device = models.OneToOneField(Device, null=True)

    def device_gcm(self, reg_id):
        d = self.device
        if not d:
            d = Device(dev_id=self.pk, name=self.username)
        d.reg_id = reg_id
        d.save()

    def send_message(self, message):
        self.device.send_message({'message': message})


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
