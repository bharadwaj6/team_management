# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Member(models.Model):
    """Team member object."""

    ROLES = (
        (1, 'admin'),
        (2, 'regular'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=100)
    role = models.IntegerField(choices=ROLES)
