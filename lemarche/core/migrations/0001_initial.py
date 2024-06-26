# Generated by Django 4.2.2 on 2024-06-26 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusName', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=50)),
                ('imgUrl', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('pic', models.TextField(blank=True, max_length=200, null=True)),
                ('contactNo', models.IntegerField()),
                ('location', models.TextField(blank=True, max_length=200, null=True)),
                ('address', models.JSONField(blank=True, null=True)),
                ('campus', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.campus')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('price', models.IntegerField()),
                ('datePosted', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('imgUrl', models.TextField(blank=True, max_length=200, null=True)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('liked_by', models.ManyToManyField(blank=True, related_name='liked_by', to='core.usermodel')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usermodel')),
            ],
        ),
    ]
