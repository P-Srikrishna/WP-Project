# Generated by Django 3.1.2 on 2020-11-02 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20201102_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration1',
            name='City',
            field=models.CharField(max_length=120, verbose_name='City'),
        ),
    ]
