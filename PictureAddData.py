import pathlib
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()
from robot.models import Sort_term_memory

path = str(pathlib.Path(__file__).parent.absolute()) + '\media\stm_picture' #取得現在這個py檔的絕對路徑之後再加上放圖片的位置
dirlist = os.listdir(path) #取得path路徑下的所有檔案 
pictruesdb = Sort_term_memory.objects.all()
pictruesdb.delete()

for i in dirlist:  
    pictrue_link = 'stm_picture/' + str(i)
    print(pictrue_link)
    pictruesdb = Sort_term_memory.objects.create(image = pictrue_link)
    pictruesdb.save()