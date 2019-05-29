# App/User/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE = (
        (0, u'User'),
        (1, u'Staff'),
        (2, u'Dev'),
        (3, u'Admin'),
    )
    ROLE_CATEGORY = (
        (0, u'Category1'),
        (1, u'Category2'),
        (2, u'Category3'),
        (3, u'Category4'),
        (4, u'Category5'),
    )
    role = models.IntegerField(default=0, choices=ROLE)
    role_category = models.IntegerField(default=0, choices=ROLE_CATEGORY)
    class Meta:
        permissions = (
                       ('can_view_profile', 'Can View Profile'),
                       ('can_edit_profile', 'Can Edit Profile'),
        )
    
    def __str__(self):
        return self.username