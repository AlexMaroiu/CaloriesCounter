from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Articol(MyModel):
    class Meta:
        db_table = 'articole'

    nume = models.CharField(max_length=255, null=False)
    firma = models.CharField(max_length=255, null=False)
    calorii = models.IntegerField(null=False)


class Mancat(models.Model):
    class Meta:
        db_table = 'mancat'

    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    articole_mancate = models.ForeignKey('Articol', on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=3, default=0)
    calorii = models.DecimalField(max_digits=9, decimal_places=3, default=0)
    data = models.DateField(null=True)

    def get_articol_nume(self):
        return self.articole_mancate.nume
    get_articol_nume.short_description = "Nume produs"
    get_articol_nume.admin_order_field = "articole_mancate__nume"

    def __str__(self):
        return f'{type(self)} - {self.id}'


class Profil(models.Model):
    class Meta:
        db_table = 'profile'

    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    calorii = models.DecimalField(max_digits=9, decimal_places=3, default=0)
    zi = models.DateField(null=True)