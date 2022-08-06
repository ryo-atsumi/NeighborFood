from django.db import models

class Setting(models.Model):
    distance = models.IntegerField("距離",primary_key=True, unique=True)
    price = models.IntegerField("価格",max_length=10)
    review = models.CharField("評価",max_length=225)
    phone_number = models.IntegerField("電話番号",max_length=10)
    opening_flg = models.BooleanField("営業フラグ",default=False)
    type_of_cuisine = models.CharField("料理種類",max_length=225)
    
    def __str__(self):
        return self.distance


class Result(models.Model):
    store_name = models.CharField("店名",primary_key=True, unique=True,max_length=225)
    location = models.CharField("自分の位置",max_length=225)
    distance = models.IntegerField("距離",max_length=10)
    price = models.IntegerField("価格",max_length=10)
    review = models.CharField("評価",max_length=225)
    phone_number = models.IntegerField("電話番号",max_length=10)
    opening_flg = models.BooleanField("営業フラグ",default=False)
    type_of_cuisine = models.CharField("料理種類",max_length=225)
    
    def __str__(self):
        return self.store_name