from django.db import models
from django.utils import timezone
#from django.db.models import Model

class UserModel(models.Model):
    username = models.CharField(max_length=16)
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=12, null=True)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    address = models.TextField(max_length=200 )
    email_id = models.EmailField(max_length=200)
    secret_code = models.IntegerField()
    #file will be uploaded to MEDIA_ROOT / upload_img
    #avatar = models.ImageField(upload_to = 'upload_img/', heigth_field = None, width_field = None,max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


