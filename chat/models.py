from django.db import models
from user.models import User
from encrypted_fields import fields


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="msg_sender")

    recipient = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='msg_recipient')

    content = fields.EncryptedTextField(blank=False,
                                        verbose_name='Message\'s content')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """class for additional info"""
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["created_at"]
