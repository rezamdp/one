# Generated by Django 5.0.4 on 2024-04-15 15:01

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_courier', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name_courier', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('phone_number_courier', models.CharField(max_length=100, verbose_name='تلفن همراه')),
            ],
            options={
                'verbose_name': 'راکب',
                'verbose_name_plural': 'راکب ها',
            },
        ),
        migrations.CreateModel(
            name='ReasonBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='عنوان برگشت')),
            ],
            options={
                'verbose_name': 'دلیل برگشت',
                'verbose_name_plural': 'دلایل برگشت',
            },
        ),
        migrations.CreateModel(
            name='ReportCuorier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_customer', models.CharField(max_length=100, verbose_name='نام مشتری')),
                ('target_number', models.CharField(choices=[('1', 'یک مقصد'), ('2', 'دو مقصد')], default='1', max_length=3, verbose_name='تعداد مقصد')),
                ('target1', models.CharField(max_length=100, verbose_name='مقصد')),
                ('target2', models.CharField(blank=True, max_length=100, null=True, verbose_name='مقصد فرعی')),
                ('duty_to_pay1', models.CharField(choices=[('GB', 'ماه رویان'), ('CUSTOMER', 'مشتری')], default='GB', max_length=15, verbose_name='وظیفه پرداخت')),
                ('duty_to_pay2', models.CharField(blank=True, choices=[('GB', 'ماه رویان'), ('CUSTOMER', 'مشتری')], default='GB', max_length=15, null=True, verbose_name='وظیفه پرداخت فرعی')),
                ('back_courier1', models.BooleanField(default=False, verbose_name='برگشت پیک')),
                ('back_courier2', models.BooleanField(default=False, verbose_name='برگشت پیک فرعی')),
                ('cost_courier1', models.DecimalField(blank=True, decimal_places=2, max_digits=25, null=True, verbose_name='هزینه پیک')),
                ('cost_courier2', models.DecimalField(blank=True, decimal_places=2, max_digits=25, null=True, verbose_name='هزینه پیک فرعی')),
                ('number_bigak1', models.CharField(blank=True, max_length=100, null=True, verbose_name='شماره بیجک')),
                ('number_bigak2', models.CharField(blank=True, max_length=100, null=True, verbose_name='شماره بیجک فرعی')),
                ('create_report', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('update_report', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reportcouriers', to='reportcourier.courier', verbose_name='راکب')),
                ('reason_back', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reportcouriers', to='reportcourier.reasonback', verbose_name='علت برگشت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reportcouriers', to=settings.AUTH_USER_MODEL, verbose_name='کارشناس فروش')),
            ],
            options={
                'verbose_name': 'گزارش',
                'verbose_name_plural': 'گزارشات',
            },
        ),
    ]