from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)
    # currency_code = models.CharField(max_length=3)
    # dialing_code = models.IntegerField()
    # continent = models.CharField(max_length=10)
    # country_name = models.CharField(max_length=50, default=' ')
    # timezone = models.CharField(max_length = 15, default=' ')
    # alt_name = models.CharField(max_length=100, default=' ')
    # country_code = models.CharField(max_length=3, default=" ")
    # temperature = models.CharField(max_length=6, default=" ")
    # pressure = models.CharField(max_length=10, default=" ")
    # humidity = models.CharField(max_length=10, default=" ")
    # icon = models.CharField(max_length=5, default="")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Cities'