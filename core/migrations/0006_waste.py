# Generated by Django 2.2 on 2020-01-18 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200119_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_waste', models.CharField(max_length=400)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
