# Generated by Django 3.2.8 on 2022-03-29 09:30

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=core.models.upload_image_path)),
                ('feel', models.CharField(blank=True, max_length=50, null=True)),
                ('store_id', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=core.models.upload_image_path)),
                ('happy', models.PositiveIntegerField(default=0)),
                ('satisfied', models.PositiveIntegerField(default=0)),
                ('neutral', models.PositiveIntegerField(default=0)),
                ('sad', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ManyToManyField(blank=True, to='core.Customer')),
            ],
        ),
    ]