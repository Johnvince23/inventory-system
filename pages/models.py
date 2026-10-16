from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date_added = models.DateField(auto_now_add=True)

    def total_value(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.name} - {self.quantity} in stock"    
