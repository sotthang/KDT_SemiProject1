from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os


# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_img = models.ImageField(upload_to='profile/', blank=True)

    def delete(self, *args, **kargs):
        if self.profile_img:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.profile_img.path))
        super(User, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_user = User.objects.get(id=self.id)
            if self.profile_img != old_user.profile_img:
                if old_user.profile_img:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_user.profile_img.path))
        super(User, self).save(*args, **kwargs)
