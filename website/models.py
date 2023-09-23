from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ph_name = models.CharField(max_length=100)  # Adjust this if "ph_name" stands for something specific
    cellphone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
