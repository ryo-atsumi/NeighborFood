# Generated by Django 4.0.6 on 2022-08-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opening_screen', '0003_alter_result_opening_flg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='price',
            field=models.CharField(max_length=255, verbose_name='価格'),
        ),
    ]
