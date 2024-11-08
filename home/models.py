from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')
    userID = models.CharField(max_length=20, unique=True, primary_key=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups", 
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_permissions",  
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def is_admin(self):
        return self.role == 'admin'
    
    def is_user(self):
        return self.role == 'user'

class Tennis(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField()
    squared = models.FloatField()
    limit = models.IntegerField()
    court_address = models.CharField(max_length=255, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    hours = models.IntegerField()
    brief = models.CharField(max_length=100000, null=True)
    
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url