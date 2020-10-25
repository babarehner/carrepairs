from django.db import models

class Vehicles(models.Model):

    class Meta:
        ordering = [ 'year']

    id = models.AutoField(
        primary_key = True
    )

    year_min = 1900
    year_max = 2100
    year = models.IntegerField(
        'Year',
    )

    man_max_len = 50
    manufacturer = models.CharField(
        'Manufacturer',
        max_length = man_max_len,
    )

    model_max_len = 100
    model = models.CharField(
        'model',
        max_length = model_max_len
    )

    sn_max_len = 15
    serial_no = models.CharField(
        'Serial Number',
        unique = True,
        max_length = sn_max_len
    )

