from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField(default='Good')
    contact_number=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name