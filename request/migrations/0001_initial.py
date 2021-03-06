# Generated by Django 3.2.6 on 2021-12-06 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myuploadfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=255)),
                ('myfiles', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PricingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PartNumber', models.CharField(max_length=50)),
                ('Nomenclature', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField()),
                ('myfiles', models.FileField(upload_to='excel/')),
            ],
        ),
    ]
