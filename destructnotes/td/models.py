from django.db import models

# Create your models here.
class Notes(models.Model):
    id=models.AutoField(primary_key=True)
    text=models.CharField()
    created_at=models.DateTimeField(auto_now=True)
