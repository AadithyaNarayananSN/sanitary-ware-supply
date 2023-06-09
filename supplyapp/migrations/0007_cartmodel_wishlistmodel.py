# Generated by Django 4.1.5 on 2023-02-08 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplyapp', '0006_productmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='supplyapp/static')),
            ],
        ),
        migrations.CreateModel(
            name='wishlistmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='supplyapp/static')),
            ],
        ),
    ]
