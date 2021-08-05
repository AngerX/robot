from django.db import models
from django.db.models.base import Model
from django.utils import timezone

class Userdata(models.Model):
    name = models.CharField(max_length=200) 
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    gender = models.CharField(max_length=200) 
    password = models.CharField(max_length=200)
    #將儲存圖片位置定義在設定放靜態檔(在setting中設定的media資料夾)，底下的image資料夾下
    #http://127.0.0.1:8000/media/image/~~~~~.jpg 可直接在網頁上顯示該資料夾底下的圖片
    image = models.ImageField(upload_to='headshot/', blank=False, null=False) 
    def __str__(self):
        return self.name

class Sort_term_memory(models.Model):
    image = models.ImageField(upload_to='stm_picture/', blank=False, null=False) 

# Create your models here.
