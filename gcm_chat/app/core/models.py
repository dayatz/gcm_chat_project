from django.db import models
from django.contrib.auth.models import AbstractUser
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
