# Generated by Django 3.1.7 on 2021-09-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20210905_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='status',
            field=models.CharField(choices=[('online', 'On-line'), ('offline', 'Off-line')], default='offline', max_length=10),
        ),
    ]