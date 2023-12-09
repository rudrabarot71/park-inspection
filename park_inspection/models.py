from django.db import models

class pi_public(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    rating = models.DecimalField(
        max_digits=1, 
        decimal_places=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    size = models.DecimalField(max_digits=4,)


     
    