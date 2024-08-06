from django.db import models
from django.contrib.auth import get_user_model

class Car(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    model = models.CharField(max_length=100, blank=False, null=False)
    brand = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, Owner: {self.owner.username}"
