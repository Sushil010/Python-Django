from django.db import models
import uuid

# Create your models here.
class Notes(models.Model):
    note_id= models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    viewed=models.BooleanField(default=False)

    def __str__(self):
        return str(self.note_id)