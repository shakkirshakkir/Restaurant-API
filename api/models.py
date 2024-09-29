from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# menu_items=[
#     {'id':1,'dish':'CB','price':120,'rating':4.0,'category':'non-veg'},
#     {'id':2,'dish':'BB','price':110,'rating':5.0,'category':'non-veg'},
#     {'id':3,'dish':'FB','price':150,'rating':6.0,'category':'non-veg'},
#     {'id':4,'dish':'Fried-rice','price':60,'rating':4.0,'category':'veg'},
#     {'id':5,'dish':'Meal','price':50,'rating':5.0,'category':'veg'},
    

# ]

class Menu(models.Model):
    dish=models.CharField(max_length=100)
    price=models.IntegerField()
    rating=models.FloatField()
    category=models.CharField(max_length=100)

class Review(models.Model):
    review=models.CharField(max_length=100)
    rating=models.FloatField()
    dish=models.ForeignKey(Menu,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Meta:
    unique_together=('user','dish')