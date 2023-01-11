# Generated by Django 2.1.5 on 2019-04-27 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0008_addcmp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addcomplaint',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_no', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('no', models.CharField(max_length=100)),
                ('type1', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('case1', models.TextField(max_length=500)),
                ('rpy', models.TextField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Addcmp',
        ),
    ]
