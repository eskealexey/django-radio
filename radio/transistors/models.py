from django.db import models

class TipTrans(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TipKorpus(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class DatasheetTransistor(models.Model):
    discription = models.CharField(max_length=200, default='-')
    url = models.FileField(upload_to='datasheets/transistors', null=True, blank=True)

    def __str__(self):
        return f"{self.discription} {str(self.url)}"

class Transistor(models.Model):
    name = models.CharField(max_length=200)
    mark = models.CharField(max_length=200)
    tip_trans = models.ForeignKey(TipTrans, on_delete=models.CASCADE)
    tip_korpusa = models.ForeignKey(TipKorpus, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.IntegerField()
    datasheet = models.ForeignKey(DatasheetTransistor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
