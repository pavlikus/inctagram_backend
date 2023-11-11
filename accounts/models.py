from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField

from inctagram.services import get_image_upload_path
from inctagram.storage import OverwriteStorage


class User(AbstractUser):
    email = models.EmailField(
        _("Email address"), blank=False, max_length=254, unique=True
    )
    birthday = models.DateField(_("Birthday"), blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    bio = models.CharField(_("About Me"), blank=True, max_length=2048)
    city = models.CharField(_("Location"), blank=True, max_length=512)

    avatar = ImageField(
        default="images/placeholder/avatar.png",
        storage=OverwriteStorage(),
        upload_to=get_image_upload_path,
    )
