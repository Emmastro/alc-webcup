# Generated by Django 3.2.3 on 2021-05-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0002_auto_20210529_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='miningfarm',
            name='farm_name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
