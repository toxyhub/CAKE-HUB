from django.db import models

class CakePro(models.Model): #inheritance
    name=models.CharField(max_length=200) #creating field system
    price=models.IntegerField()
    image=models.ImageField(upload_to='pic') #creating a folder and will put 
    quanty=models.FloatField()
    discount=models.IntegerField(default=0)
    descript=models.TextField()
    date=models.DateTimeField(auto_now_add=True) #takes the correct date
    