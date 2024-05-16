from django.db import models
class User(models.Model):
    bio=models.CharField(max_length=200)
    skillset=models.CharField(max_length=200)
    contact_details=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.bio)

class Portfolio(models.Model):
    project_showcase=models.CharField(max_length=200)
    education=models.CharField(max_length=200)
    work_experience=models.IntegerField()
    experience=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.project_showcase)