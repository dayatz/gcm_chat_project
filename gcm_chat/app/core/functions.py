from gcm.models import Device
from gcm.api import GCMMessage


def send_user_message(user_id, message):
    device = Device.objects.get(dev_id=user_id)
    device.send_message({'message': message})


def send_multiuser_message(user_ids, message):
    reg_ids = Device.objects.filter(
        dev_id__in=user_ids).values_list('reg_id', flat=True)
    GCMMessage.send({'message': message}, registration_ids=reg_ids)
