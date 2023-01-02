from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from  .models import Category
from  .models import Blog
from .serializers import  CategorySerializer,BlogSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer

# Create your views here.
class BlogView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =BlogSerializer