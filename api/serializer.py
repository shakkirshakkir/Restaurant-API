from rest_framework import serializers
from .models import Menu,Review
from django.contrib.auth.models import User

class MenuSerializer(serializers.Serializer):
    dish=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()
    category=serializers.CharField()

class MenuModelSer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields="__all__"
    def validate(self,attrs):
        pr=attrs.get("price")
        if pr<0:
            raise serializers.ValidationError("Price should be a non-negative value")
        return attrs

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)   

class DishNameSer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=['dish']
class UsernameSer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['user_name']

class ReviewSer(serializers.ModelSerializer):
    dish=DishNameSer(many=False,read_only=True)
    user=UsernameSer(many=False,read_only=True)
    class Meta:
        model=Review
        fields=['review','rating','dish','user']
    def create(self,validated_data):
        user=self.context.get("user")
        dish=self.context.get("dish")
        return Review.objects.create(user=user,dish=dish,**validated_data)   

