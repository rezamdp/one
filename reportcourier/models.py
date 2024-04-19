#===============================================> Imports <===============================================
# ----> genrel  <----
from django.db import models
from django.urls import reverse


# ----> extrenal  <----
from django_jalali.db import models as jmodels
from account.models import User



#===============================================> ReasonBack Model <===============================================
class ReasonBack (models.Model):
    title = models.CharField(
        max_length=100 ,
        null=False ,
        blank=True ,
        verbose_name= 'عنوان برگشت'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reportcourier:add_reasonback')
    class Meta :
        verbose_name = "دلیل برگشت"
        verbose_name_plural = "دلایل برگشت"


#=================================================> Courier Model <================================================
class Courier (models.Model):
    first_name_courier = models.CharField(
        max_length=100 ,
        null= False ,
        blank= False ,
        verbose_name= 'نام'
        )

    last_name_courier = models.CharField(
        max_length=100 ,
        null= False ,
        blank= False ,
        verbose_name= 'نام خانوادگی'
        )

    phone_number_courier = models.CharField(
        max_length=100 ,
        null= False ,
        blank= False ,
        verbose_name= 'تلفن همراه'
        )

    def __str__(self):
        return self.last_name_courier

    def get_absolute_url(self):
        return reverse('reportcourier:add_courier')

    class Meta :
        verbose_name = "راکب"
        verbose_name_plural = "راکب ها"



#blank = true ---> field not *
#===============================================> ReportCuorier Model <===============================================

class ReportCuorier (models.Model):
    duty_to_pay_choice = (
        ('GB', 'ماه رویان'),
        ('CUSTOMER', 'مشتری')
    )
    two_target = (
        ('1', 'یک مقصد'),
        ('2', 'دو مقصد')
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        verbose_name='کارشناس فروش',
        related_name="reportcouriers"
    )

    reason_back = models.ForeignKey(
        to=ReasonBack,
        verbose_name='علت برگشت',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="reportcouriers"
    )

    courier = models.ForeignKey(
        to=Courier,
        on_delete=models.PROTECT,
        verbose_name='راکب',
        related_name="reportcouriers"
    )

    name_customer = models.CharField(
        max_length=100,
        null=False,
        verbose_name='نام مشتری'
    )
#==========================================> targer <======================================================
    target_number = models.CharField(
        choices= two_target,
        max_length=3,
        default='1' ,
        verbose_name= 'تعداد مقصد'
    )

    target1 = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='مقصد'
    )

    target2 = models.CharField(
        max_length=100,
        null=True,
        blank= True ,
        verbose_name='مقصد فرعی'
    )



    duty_to_pay1 = models.CharField(
        choices=duty_to_pay_choice,
        max_length=15,
        default='GB',
        verbose_name='وظیفه پرداخت'
    )
    duty_to_pay2 = models.CharField(
        choices=duty_to_pay_choice,
        max_length=15,
        default='GB',
        null=True ,
        blank=True,
        verbose_name='وظیفه پرداخت فرعی'
    )


    back_courier1 = models.BooleanField(
        default=False,
        null=False,
        verbose_name='برگشت پیک'
    )

    back_courier2 = models.BooleanField(
        default=False,
        null=False,
        verbose_name='برگشت پیک فرعی'
    )

    cost_courier1 = models.DecimalField(
        max_digits=25,
        decimal_places= 2 ,
        null=True,
        blank=True,
        verbose_name='هزینه پیک'
    )

    cost_courier2 = models.DecimalField(
        max_digits=25,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='هزینه پیک فرعی'
    )

    number_bigak1 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='شماره بیجک'
    )
    number_bigak2 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='شماره بیجک فرعی'
    )

    create_report = jmodels.jDateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت" , )

    update_report = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')


    class Meta:
        verbose_name = "گزارش"
        verbose_name_plural = 'گزارشات'
        ordering = ('-create_report',)


    def __str__(self):
        return f'{self.user} - {self.name_customer}'

    def get_absolute_url(self):
        return reverse('reportcourier:reportcourier-detail', args=[str(self.id)])