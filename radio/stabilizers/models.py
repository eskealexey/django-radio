import os

from django.db import models


class TipStabilizer(models.Model):
    objects = None
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class TipKorpusStabilizer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class DatasheetStabilizer(models.Model):
    objects = None
    discription = models.CharField(max_length=200, blank=True)
    url = models.FileField(upload_to='datasheets/stabilizers/', null=True, blank=True)

    def __str__(self):
        return f"{os.path.basename(str(self.url))}"


class Stabilizer(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    mark = models.CharField(max_length=200, blank=True, null=True)
    volt = models.CharField(max_length=20, blank=True, null=True)
    tip_stab = models.ForeignKey(TipStabilizer, on_delete=models.CASCADE)
    tip_korpusa = models.ForeignKey(TipKorpusStabilizer, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    datasheet = models.ManyToManyField(DatasheetStabilizer, blank=True)
    primech = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
