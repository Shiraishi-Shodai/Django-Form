from django.db import models

# Create your models here.
class Device(models.Model): #モデル名は大文字で始める,１つのモデルが１つのテーブルに該当する
    # フィールドのオプションで何も指定しなければNOT NULL制約がかかる
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    
class OneText(models.Model):
    japanese = models.CharField(max_length=100)