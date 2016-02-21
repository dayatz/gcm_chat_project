from django.db import models
from django.contrib.auth.models import AbstractUser
from gcm.models import Device


class User(AbstractUser):
    device = models.OneToOneField(Device)

    def send_message(self, message):
        self.device.send_message({'message': message})
