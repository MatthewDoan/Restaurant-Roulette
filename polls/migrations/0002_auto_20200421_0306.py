# Generated by Django 3.0.5 on 2020-04-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]