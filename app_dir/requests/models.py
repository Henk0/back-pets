from django.db import models
from django.utils.timezone import now
from app_dir.user.api.serializers import User

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Request(models.Model):
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    langitute = models.FloatField(
        blank=False,
        null=False
    )
    latitude = models.FloatField(
        blank=False,
        null=False
    )
    author = models.ForeignKey(
        User, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL)
    # photo = models.ImageField(
    #     upload_to=upload_to, 
    #     blank=True, 
    #     null=True)
    created_at = models.DateTimeField(
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        default=now
    )

    class Meta:
        app_label = 'requests'

    def __str__(self):
        return self.name
