# Generated by Django 3.2.10 on 2022-01-29 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_has_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author_status',
        ),
    ]
