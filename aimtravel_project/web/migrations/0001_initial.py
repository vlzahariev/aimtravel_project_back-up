# Generated by Django 4.1.3 on 2022-12-05 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(blank=True, max_length=30, null=True)),
                ('service_description', models.TextField(blank=True, null=True)),
                ('service_price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_position', models.CharField(blank=True, max_length=30, null=True, verbose_name='Позиция')),
                ('employer', models.CharField(blank=True, max_length=30, null=True, verbose_name='Работодател')),
                ('wage', models.FloatField(blank=True, null=True, verbose_name='Заплащане')),
                ('city', models.CharField(blank=True, max_length=20, null=True, verbose_name='Град')),
                ('state', models.CharField(blank=True, max_length=20, null=True, verbose_name='Щат')),
                ('sponsor', models.CharField(blank=True, max_length=15, null=True, verbose_name='Спонсор')),
                ('offer_pic', models.URLField(blank=True, null=True, verbose_name='Снимка-URL')),
                ('job_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricing_type', models.CharField(blank=True, choices=[('Self Arranged', 'Self Arranged'), ('Full Placement Standard', 'Full Placement Standard'), ('Premium Full Placement', 'Premium Full Placement')], default='Full Placement Standard', max_length=25, null=True)),
                ('price', models.FloatField()),
                ('price_description', models.TextField(blank=True, help_text='Please enter description', null=True)),
            ],
        ),
    ]