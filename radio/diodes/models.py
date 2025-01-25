import os

from django.db import models


class TipDiode(models.Model):
    objects = None
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class TipKorpusDiode(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class DatasheetDiode(models.Model):
    objects = None
    discription = models.CharField(max_length=200, blank=True)
    url = models.FileField(upload_to='datasheets/diodes/', null=True, blank=True)

    def __str__(self):
        return f"{os.path.basename(str(self.url))}"


class Diode(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    mark = models.CharField(max_length=200, blank=True, null=True)
    tip_diode = models.ForeignKey(TipDiode, on_delete=models.CASCADE)
    tip_korpusa = models.ForeignKey(TipKorpusDiode, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    datasheet = models.ManyToManyField(DatasheetDiode, blank=True)
    primech = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
