from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import generics
from .models import devBlog,StripeDb,StripeServiceDb


class devBlogSer(ModelSerializer):
    class Meta:
        model = devBlog
        fields = ["id","uniqueKeys","title","code"]

class StripeDbSerializers(ModelSerializer):
    class Meta:
        model=StripeDb
        fields=["id","email","accountId"]

class StripeServiceSerializers(ModelSerializer):
    class Meta:
        model=StripeServiceDb
        fields=["id","email","accountId","serviceName","amount"]