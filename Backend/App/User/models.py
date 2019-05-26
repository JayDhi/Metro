# App/User/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CATEGORY_TYPE = (
        (0, 'Normal'),
        (1, 'Admin'),
        (2, 'SysAdmin')
    )
    category = models.IntegerField(default=0, choices=CATEGORY_TYPE)
    class Meta:
        permissions = (
                       ('can_view_profile', 'Can View Profile'),
                       ('can_edit_profile', 'Can Edit Profile'),
        )
    
    def __str__(self):
        return self.username