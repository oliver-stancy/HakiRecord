from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Statement(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    ID_Number = models.IntegerField()
    DOB = models.DateField()
    Address = models.TextField()
    Phone_Number = models.IntegerField()
    INCIDENT_TYPES = [
        ('theft', 'Theft'),
        ('murder', 'Murder'),
        ('child abuse', 'Child Abuse'),
        ('accident', 'Accident'),
    ]
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)

    # Text input for location
    incident_location = models.CharField(max_length=255)

    # Date field
    incident_date = models.DateField(default=timezone.now)

    # Dropdown for time of incident
    INCIDENT_TIMES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
        ('night', 'Night'),
    ]
    incident_time = models.CharField(max_length=20, choices=INCIDENT_TIMES)

    # Textarea for suspect description
    suspect_description = models.TextField(blank=True, null=True)
    incident_evidence=models.FileField(upload_to='evidence/')

    # Textarea for brief explanation
    incident_description = models.TextField(blank=True,null = True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    Service_No = models.ForeignKey(User, on_delete=models.CASCADE)
    ob_number = models.CharField(max_length=30, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.ob_number:
            today = timezone.localtime().date()
            # Count how many entries are recorded today
            count_today = Statement.objects.filter(
                recorded_at__date=today
            ).count() + 1
            # Generate OB number, e.g., "OB 1/14/10/2025"
            self.ob_number = f"OB {count_today}/{today.day}/{today.month}/{today.year}"
        super().save(*args,** kwargs)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"

class Contact(models.Model):
    contact_name=models.CharField(max_length=100)
    contact_email=models.CharField(max_length=100)
    contact_message=models.TextField()

    def __str__(self):
        return f"{self.contact_name} {self.contact_email}"






