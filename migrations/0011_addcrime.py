# Generated by Django 2.1.5 on 2019-04-27 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0010_auto_20190427_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addcrime',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('no', models.CharField(max_length=100)),
                ('suspect', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('case1', models.TextField(max_length=500)),
                ('rpy', models.TextField(max_length=500)),
            ],
        ),
    ]
