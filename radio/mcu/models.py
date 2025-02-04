import os

from django.db import models


class TipMcu(models.Model):
    objects = None
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class TipKorpusMcu(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name


class DatasheetMcu(models.Model):
    objects = None
    discription = models.CharField(max_length=200, blank=True, default='DataSheet')
    url = models.FileField(upload_to='datasheets/mcus/', null=True, blank=True)

    def __str__(self):
        return f"{os.path.basename(str(self.url))}"


class Mcu(models.Model):
    objects = None
    name = models.CharField(max_length=200, verbose_name="наименование")
    mark = models.CharField(max_length=200, blank=True, null=True, verbose_name="маркировка")
    tip_mcu = models.ForeignKey(TipMcu, on_delete=models.CASCADE, verbose_name="семейство МК")
    tip_korpusa = models.ForeignKey(TipKorpusMcu, on_delete=models.CASCADE, verbose_name="корпус")
    amount = models.IntegerField(default=0, verbose_name="количество, шт.")
    datasheet = models.ManyToManyField(DatasheetMcu, blank=True, verbose_name="данные")
    primech = models.TextField(blank=True, null=True, verbose_name="примечание")

    def __str__(self):
        return self.name
