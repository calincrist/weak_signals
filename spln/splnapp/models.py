from django.db import models

class FileModel(models.Model):
     file_id = models.AutoField(primary_key=True)
     name = models.CharField(max_length = 100, default='')
     contents = models.CharField(max_length = 1000, default='')
     path = models.CharField(max_length = 1000, default='')
