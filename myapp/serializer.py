from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import generics
from .models import devBlog


class devBlogSer(ModelSerializer):
    class Meta:
        model = devBlog
        fields = ["id","uniqueKeys","title","code"]