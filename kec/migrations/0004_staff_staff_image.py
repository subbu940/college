# Generated by Django 2.2.6 on 2019-11-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kec', '0003_auto_20191114_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
