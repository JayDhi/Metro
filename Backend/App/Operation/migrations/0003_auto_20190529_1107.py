# Generated by Django 2.2.1 on 2019-05-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operation', '0002_auto_20190529_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='name',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]