# Generated by Django 4.1.5 on 2023-02-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplyapp', '0003_delete_productmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='supplyapp/static')),
            ],
        ),
    ]
