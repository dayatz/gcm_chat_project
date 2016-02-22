from django.db import models
from django.template.defaultfilters import slugify
from app.core.models import User
from gcm.api import GCMMessage


class ChatRoom(models.Model):
    user = models.ForeignKey(User, related_name='created_rooms')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ChatRoom, self).save(*args, **kwargs)

    def send_message(self, message):
        GCMMessage().send({'message': message}, to='/topics/%s' % self.slug)

    def __str__(self):
        return self.title


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages')
    user = models.ForeignKey(User, related_name='sent_messages')
    message = models.TextField()

    def __str__(self):
        return '%s: %s' % (self.user.username, self.message)
