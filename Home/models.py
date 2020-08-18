from django.db import models

class categorieslink (models.Model):
    name = models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.name

class Homelink (models.Model):
    name = models.CharField(max_length=250,unique=True)
    path = models.CharField(max_length=250,unique=True)
    categorie = models.ForeignKey(categorieslink, on_delete=models.CASCADE)
    crated_dt = models.DateField(auto_now=True)

    def __str__(self):
        return self.name