from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from django.utils.deconstruct import deconstructible

# Create your models here.

@deconstructible
class RenameKoreanFileName:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        _, ext = os.path.splitext(filename)
        new_filename = instance.username.replace(' ', '_') + ext
        return os.path.join(self.path, new_filename)

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_img = models.ImageField(upload_to=RenameKoreanFileName('profile/'), blank=True)

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
