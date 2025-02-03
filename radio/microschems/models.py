import os

from django.db import models


class TipMicroschema(models.Model):
    objects = None
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class TipKorpusMicroschema(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class NaznachenieMicroschema(models.Model):
    objects = None
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class DatasheetMicroschema(models.Model):
    objects = None
    discription = models.CharField(max_length=200, blank=True)
    url = models.FileField(upload_to='datasheets/microschems/', null=True, blank=True)

    def __str__(self):
        return f"{os.path.basename(str(self.url))}"


class Microschema(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    mark = models.CharField(max_length=200, blank=True, null=True)
    tip_micro = models.ForeignKey(TipMicroschema, on_delete=models.CASCADE)
    tip_korpusa = models.ForeignKey(TipKorpusMicroschema, on_delete=models.CASCADE)
    naznachenie = models.ForeignKey(NaznachenieMicroschema, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    datasheet = models.ManyToManyField(DatasheetMicroschema, blank=True)
    primech = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
