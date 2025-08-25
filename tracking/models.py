from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    tracking_id = models.CharField(max_length=20, unique=True)  # Unique tracking number
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight = models.FloatField()  # In kg
    status = models.CharField(max_length=50, choices=[
        ('PENDING', 'Pending'),
        ('IN TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional: Link to customer

    def __str__(self):
        return self.tracking_id

class StatusUpdate(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='updates')
    location = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.package.tracking_id} at {self.location}"