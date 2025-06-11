# models.py
from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject


class BloodRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    blood_type = models.CharField(max_length=5)
    quantity = models.DecimalField(max_digits=4, decimal_places=1)  # For example, 1.5 liters
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Blood Request from {self.name} for {self.blood_type} ({self.quantity}L)"

class BecomeDonor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    blood_type = models.CharField(max_length=5)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth=models.DateField()
    preferred_donation_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Become a Donor from {self.name} for {self.blood_type} (Donation Date: {self.preferred_donation_date})"
