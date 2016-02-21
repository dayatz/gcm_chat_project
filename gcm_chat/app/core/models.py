from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from gcm.models import Device


class User(AbstractUser):
    def device_gcm(self, reg_id):
        device = self.get_user_device()
        if not device:
            device = Device(dev_id=self.pk, name=self.username)
        device.reg_id = reg_id
        device.save()

    def get_user_device(self):
        try:
            return Device.objects.get(dev_id=self.pk)
        except:
            return None


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
