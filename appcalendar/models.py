from django.db import models

# Create your models here.


class BookRoom(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    arrive_date = models.DateField()
    departure_date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.full_name
