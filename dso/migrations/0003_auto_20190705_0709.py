# Generated by Django 2.2.1 on 2019-07-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dso', '0002_auto_20190702_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relations',
            name='relation_english',
            field=models.CharField(max_length=100),
        ),
    ]
