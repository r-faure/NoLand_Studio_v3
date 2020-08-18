from django.db import models

# Create your models here.

class Resume(models.Model):
    path = models.CharField(max_length=250,unique=True)
    name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    web = models.CharField(max_length=250)
    driver_license = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    
    def __str__(self):
        return self.path

class Course(models.Model):
    #id = models.IntegerField(unique=True)
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.id

class Experience(models.Model):
    #id = models.IntegerField(unique=True)
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desciption = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.id

class Asset(models.Model):
    #id = models.IntegerField(unique=True)
    resume = models.ManyToManyField(Resume, related_name="resumes")
    name = models.CharField(max_length=250)
    #lvl_0_10 = models.IntegerChoices

    def __str__(self):
        return self.id
