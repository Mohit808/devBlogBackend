from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import generics
from .models import devBlog,StripeDb


class devBlogSer(ModelSerializer):
    class Meta:
        model = devBlog
        fields = ["id","uniqueKeys","title","code"]

class StripeDbSerializers(ModelSerializer):
    class Meta:
        model=StripeDb
        fields=["id","email","userId","serviceName","amount"]