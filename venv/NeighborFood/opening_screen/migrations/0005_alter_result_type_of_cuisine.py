# Generated by Django 4.0.6 on 2022-08-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opening_screen', '0004_alter_result_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='type_of_cuisine',
            field=models.CharField(max_length=255, verbose_name='料理種類'),
        ),
    ]
