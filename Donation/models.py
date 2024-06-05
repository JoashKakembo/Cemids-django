from django.db import models

class Donation(models.Model):
  full_name = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=20)
  email = models.EmailField(unique=True)
  amount = models.DecimalField(max_digits=100, decimal_places=2)

  def __str__(self):
    return self.full_name

