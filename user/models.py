from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from encrypted_fields import fields


class User(AbstractUser):
    QUESTIONS = [("PET", "What's your pet name?"),
                 ("PN", "What's your phone number"),
                 ("BF", "What's your best friend name")
                 ]

    username = models.CharField(unique=True, max_length=64)

    first_name = models.CharField(blank=False,null=True, max_length=64)

    last_name = models.CharField(blank=False,null=True, max_length=64)

    registration_date = models.DateTimeField(blank=False,
                                             auto_now_add=True)

    secret_question = fields.EncryptedTextField(blank=False,null=True, choices=QUESTIONS)

    secret_answer = fields.EncryptedCharField(max_length=256, blank=False, null=True)


    class Meta:
        """class for additional info"""
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["id"]

    def get_absolute_url(self):
        reverse('user', kwargs={'pk': self.id})

    def __str__(self):
        return self.username

    def __unicode__(self):
        return u'{0}'.format(self.secret_question)