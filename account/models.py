#===============================================> Imports <===============================================
# ----> genrel  <----


from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, PermissionsMixin 
from django.utils.html import format_html
from django_jalali.db import models as jmodels
from django.utils import timezone
# ----> extrenal  <----


#===============================================> User Model <===============================================

class User(AbstractUser, PermissionsMixin):
    last_login = jmodels.jDateTimeField(default=timezone.now)
    is_verified = models.BooleanField(
        default=True ,
        verbose_name="وضعیت تایید بودن کارشناس")

    phone_number = models.CharField(
        max_length=100 ,
        null= False ,
        blank= False ,
        verbose_name= 'تلفن همراه'
        )
    images_user = models.ImageField(
        upload_to='media/',
        null=True,
        blank=True ,
        verbose_name='تصویر کارشناس',
        default= 'static/dist/img/credit/icons.png'
    )


    def imgs_tag(self):
        return format_html("<img class=\'img-fluid rounded\' width=100 src='{}'>".format(self.images_user.url))

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('reportcourier:dashboard_home')

    class  Meta :
        verbose_name = 'کارشناس'
        verbose_name_plural = 'کارشناسان'