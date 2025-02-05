import os

from django.db import models


class TipModul(models.Model):
    objects = None
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class DatasheetModul(models.Model):
    objects = None
    discription = models.CharField(max_length=200, blank=True, default='DataSheet')
    url = models.FileField(upload_to='datasheets/moduls/', null=True, blank=True)

    def __str__(self):
        return f"{os.path.basename(str(self.url))}"

class NaznachenieModul(models.Model):
    objects = None
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Modul(models.Model):
    objects = None
    name = models.CharField(max_length=200, verbose_name="наименование")
    mark = models.CharField(max_length=200, blank=True, null=True, verbose_name="маркировка")
    tip_modul = models.ForeignKey(TipModul, on_delete=models.CASCADE, verbose_name="тип модуля")
    naznachenie = models.ForeignKey(NaznachenieModul, on_delete=models.CASCADE, verbose_name="назначение")
    amount = models.IntegerField(default=0, verbose_name="количество, шт.")
    datasheet = models.ManyToManyField(DatasheetModul, blank=True, verbose_name="данные")
    primech = models.TextField(blank=True, null=True, verbose_name="примечание")

    def __str__(self):
        return self.name
