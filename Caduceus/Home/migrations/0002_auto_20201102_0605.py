# Generated by Django 3.1.2 on 2020-11-02 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=120)),
                ('LastName', models.CharField(max_length=120)),
                ('Email', models.CharField(max_length=120)),
                ('Password', models.CharField(max_length=16)),
                ('Address', models.CharField(max_length=120)),
                ('PhoneNumber', models.CharField(max_length=12)),
                ('City', models.CharField(max_length=120)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
