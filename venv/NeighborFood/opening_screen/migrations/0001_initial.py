# Generated by Django 4.0.6 on 2022-08-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('store_name', models.CharField(max_length=225, primary_key=True, serialize=False, unique=True, verbose_name='店名')),
                ('location', models.CharField(max_length=225, verbose_name='自分の位置')),
                ('distance', models.IntegerField(max_length=10, verbose_name='距離')),
                ('price', models.IntegerField(max_length=10, verbose_name='価格')),
                ('review', models.CharField(max_length=225, verbose_name='評価')),
                ('phone_number', models.IntegerField(max_length=10, verbose_name='電話番号')),
                ('opening_flg', models.BooleanField(default=False, verbose_name='営業フラグ')),
                ('type_of_cuisine', models.CharField(max_length=225, verbose_name='料理種類')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('distance', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='距離')),
                ('price', models.IntegerField(max_length=10, verbose_name='価格')),
                ('review', models.CharField(max_length=225, verbose_name='評価')),
                ('phone_number', models.IntegerField(max_length=10, verbose_name='電話番号')),
                ('opening_flg', models.BooleanField(default=False, verbose_name='営業フラグ')),
                ('type_of_cuisine', models.CharField(max_length=225, verbose_name='料理種類')),
            ],
        ),
    ]
