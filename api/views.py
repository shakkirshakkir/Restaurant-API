from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import MenuSerializer,MenuModelSer,UserSerializer,ReviewSer
from .models import Menu,Review
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action
# Create your views here.


# class DishList(APIView):
    # def get(self,request,*args,**kwargs):
    #     if 'category' in request.query_params:
    #         cat=request.query_params.get('category')
    #         items=[i for i in menu_items if ['category']==cat]
    #         return Response(data=items)
    #     if 'limit' in request.query_params:
           
    #         lmt=int(request.query_params.get('limit'))
    #         items=menu_items[0:lmt]
    #         return Response(data=items)
# class DishList(APIView):   
#     def get(self,request,*args,**kwargs):
#         allitems=menu_items
#         if 'category' in request.query_params:
#             cat=request.query_params.get('category')
#             allitems=[i for i in allitems if i['category']==cat]
            
#         if 'limit' in request.query_params:
           
#             lmt=int(request.query_params.get('limit'))
#             allitems=allitems[0:lmt]
#         return Response(data=allitems)
          

        
#         # return Response(data=lmt)
      

#         return Response(data=menu_items)
        

#     def post(self,request,*args,**kwargs):
#         item=request.data
#         menu_items.append(item)
#         return Response(data=menu_items)

# class DishItem(APIView):

#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         dishes=[i for i in menu_items if i['id']==id].pop()
#         return Response(data=dishes)
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         item=request.data
#         dishes=[i for i in menu_items if i['id']==id].pop()
#         dishes.update(item)
#         return Response(data=menu_items)
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         dishes=[i for i in menu_items if i['id']==id].pop()
#         dishlist=menu_items.remove(dishes)
#         return Response(data=menu_items)

# class DishList(APIView):
#     def get(self,request,*args,**kwargs):
#         dishes=Menu.objects.all()
#         ser=MenuSerializer(dishes,many=True)
#         return Response(data=ser.data)
#     def post(self,request,*args,**kwargs):
#         ser=MenuSerializer(data=request.data)
#         if ser.is_valid():
#             dish=ser.validated_data.get("dish")
#             price=ser.validated_data.get("price")
#             rating=ser.validated_data.get("rating")
#             category=ser.validated_data.get("category")
#             Menu.objects.create(dish=dish,price=price,rating=rating,category=category)
#             return Response({"msg":"OK"})
#         return Response({"msg":"FAILED"})
        
      
        
        
#         return Response(data=ser.data)

# class DishList(APIView):
#     def get(self,request,*args,**kwargs):
#         dishes=Menu.objects.all()
#         dser=MenuModelSer(dishes,many=True)
#         return Response(data=dser.data)
#     def post(self,request,*args,**kwargs):
#         ser=MenuModelSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response({"msg":"Added"})
#         else:
#             return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)

# class DishItem(APIView):

#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         dish=Menu.objects.get(id=id)
#         ser=MenuSerializer(dish)
#         return Response(data=ser.data)
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         item=Menu.objects.get(id=id)
#         ser=MenuSerializer(data=request.data)
#         if ser.is_valid():
#             dish=ser.validated_data.get("dish")
#             price=ser.validated_data.get("price")
#             rating=ser.validated_data.get("rating")
#             category=ser.validated_data.get("category")
#             item.dish=dish
#             item.price=price
#             item.rating=rating
#             item.category=category
#             item.save()
#             return Response({"msg":"OK"})
#         return Response({"msg":"FAILED"})
        
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         item=Menu.objects.get(id=id)
#         item.delete()
#         return Response({"msg":"OK"})


class DishItem(APIView):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("mid")
        item=Menu.objects.get(id=id)
        dser=MenuModelSer(item)
        return Response(data=dser.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        item=Menu.objects.get(id=id)
        ser=MenuModelSer(data=request.data,instance=item)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Updated"})
        else:
            return Response({"msg":"ser.errors"},status=status.HTTP_404_NOT_FOUND)

class UserView(APIView):
    def post(self,request,*args,**kwargs):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Registered"})
        else:
            return Response({"msg":"ser.errors"},status=status.HTTP_404_NOT_FOUND)

class MenuView(ViewSet):
    def list(self,request,*args,**kwargs):
        item=Menu.objects.all()
        dser=MenuModelSer(item,many=True)
        return Response(data=dser.data)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=Menu.objects.get(id=id)
        dser=MenuModelSer(item)
        return Response(data=dser.data)
    def create(self,request,*args,**kwargs):
        ser=MenuModelSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Added"})
        else:
            return Response({"msg":"ser.errors"},status=status.HTTP_404_NOT_FOUND)
   
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=Menu.objects.get(id=id)
        ser=MenuModelSer(data=request.data,instance=item)
        
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Updated"})
        else:
            return Response({"msg":"ser.errors"},status=status.HTTP_404_NOT_FOUND)

    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        item=Menu.objects.get(id=id)
        item.delete()
        return Response({"msg":"Deleted"})
    
class MenuModelView(ModelViewSet):
     serializer_class=MenuModelSer
     model=Menu
     queryset=Menu.objects.all()
#     authentication_classes=[authentication.BasicAuthentication]
#     permission_classes=[permission.IsAuthenticated]
authentication_classes=[authentication.TokenAuthentication]
permission_classes=[permissions.IsAuthenticated]
        

@action(detail=True,methods=['get'])
def get_reviews(self,request,*args,**kwargs):
    id=kwargs.get('pk')
    item=Menu.objects.get(id=id)
    reviews=Review.objects.filter(dish=item)
    ser=ReviewSer(reviews,many=True)
    return Response(data=ser.data)       
@action(detail=True,methods=['post'])
def add_review(self,request,*args,**kwargs):
    id=kwargs.get("pk")
    item=Menu.objects.get(id-id)
    user=request.user
    ser=ReviewSer(data=request.data,context={"user":user,"dish":item})
    if ser.is_valid():
        ser.save()
        return Response({"msg":"OK"})
    else:
        return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)
       


        
        
    
        
    
          




        