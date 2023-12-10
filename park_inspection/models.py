from django.db import models

# In your models.py file


class Inspection(models.Model):
    park_name = models.CharField(max_length=255)
    park_location = models.CharField(max_length=255)
    park_description = models.TextField()
    
    inspector_name = models.CharField(max_length=255)
    inspector_email = models.EmailField()

    date_inspected = models.DateField()
    inspection_notes = models.TextField()
    is_passed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.park_name} Inspection - {self.date_inspected}"
    
# In your models.py file

from django.db import models

class Park(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()

    # Add other fields as needed



     
    