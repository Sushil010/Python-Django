from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    # image=models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

