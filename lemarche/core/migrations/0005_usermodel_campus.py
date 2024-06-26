# Generated by Django 4.2.2 on 2024-06-26 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_usermodel_campus'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='campus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.campus'),
        ),
    ]
