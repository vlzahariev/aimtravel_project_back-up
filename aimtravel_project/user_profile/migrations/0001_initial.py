# Generated by Django 4.1.3 on 2022-12-05 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('employee_first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('employee_last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('employee_role', models.CharField(blank=True, max_length=20, null=True)),
                ('employee_pic', models.URLField(blank=True, null=True)),
                ('employee_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('employee_email', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='First name')),
                ('middle_name', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Middle name')),
                ('last_name', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='Last name')),
                ('date_of_birth', models.DateField(blank=True, help_text='dd-mm-yyyy', null=True, verbose_name='Date of birth')),
                ('place_of_birth', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('province', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('street', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('bg_personal_number', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='EGN')),
                ('nationality', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('country_of_birth', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('id_passport_number', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('passport_date_of_issue', models.DateField(blank=True, null=True)),
                ('is_received_visa', models.BooleanField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('university', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('year_of_education', models.PositiveIntegerField(blank=True, help_text='Semester', null=True)),
                ('foreign_university', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('is_fulltime_student', models.BooleanField(blank=True, null=True)),
                ('search_job_pref', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('how_to_reach', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('visa_photo', models.URLField(blank=True, null=True)),
            ],
        ),
    ]