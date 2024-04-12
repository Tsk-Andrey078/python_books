from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class UserProfile(models.Model):
    column_name = models.CharField(max_length=254)

    is_visible = models.BooleanField()
    def __str__(self) -> str:
        return self.column_name

class Book(models.Model):
    id_b = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=512)
    price = models.IntegerField(validators=[MaxValueValidator(9998), MinValueValidator(0)])

    def __str__(self) -> str:
        return self.name