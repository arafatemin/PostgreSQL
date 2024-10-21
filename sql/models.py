import uuid

from django.db import models



class Staff(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Car(models.Model):
    car_uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'car'
        managed = False

    def __str__(self):
        return self.make


class Person(models.Model):
    person_uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(max_length=255)
    date_of_brith = models.DateField()
    country_of_brith = models.CharField(max_length=255)
    car_uid = models.ForeignKey(Car, on_delete=models.SET_NULL, db_column='car_uid', blank=True, null=True)

    class Meta:
        db_table = 'person'
        managed = False

    def __str__(self):
        return self.first_name


