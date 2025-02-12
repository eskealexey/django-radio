import os

from django.db import models


class TipTrans(models.Model):
    objects = None
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class TipKorpus(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class DatasheetTransistor(models.Model):
    objects = None
    discription = models.CharField(max_length=200, blank=True, default='DataSheet')
    url = models.FileField(upload_to='datasheets/transistors/', blank=True, null=True)

    def __str__(self):
        return f"{os.path.basename(str(self.url))}"


class Transistor(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    mark = models.CharField(max_length=200, blank=True, null=True)
    tip_trans = models.ForeignKey(TipTrans, on_delete=models.CASCADE)
    tip_korpusa = models.ForeignKey(TipKorpus, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    datasheet = models.ManyToManyField(DatasheetTransistor, blank=True)
    primech = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
