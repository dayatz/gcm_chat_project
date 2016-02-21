from gcm.models import Device


def send_user_message(user_id, message):
    device = Device.objects.get(dev_id=user_id)
    device.send_message({'message': message})
