# Generated by Django 2.2 on 2020-05-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200513_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email_id',
            field=models.EmailField(max_length=200),
        ),
    ]
