# Generated by Django 4.2.2 on 2024-06-26 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_usermodel_campus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='campus',
        ),
    ]
