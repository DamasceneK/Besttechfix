from django.db import models

class ServiceRequest(models.Model):
    DEVICE_CHOICES = [
        ('computer', 'Computer'),
        ('phone', 'Phone'),
        ('printer', 'Printer'),
        ('wifi', 'Wi-Fi / Network'),
        ('email', 'Email / Account'),
        ('smart_device', 'Smart TV / Camera / Device'),
        ('business_it', 'Small Business IT'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=150)
    device_type = models.CharField(max_length=50, choices=DEVICE_CHOICES)
    issue_description = models.TextField()
    best_time_to_contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.device_type}"