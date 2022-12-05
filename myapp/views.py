
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import devBlog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .serializer import devBlogSer

@api_view(['POST'])
def devBlogFunc(request):
    data=request.data
    title=request.data['title']
    count=request.data['count']
    uniqueKeys=request.data['uniqueKeys']

    row=devBlog(uniqueKeys=uniqueKeys,title=title,code='ThisCode')
    row.save()
    list=[]
    for x in range(int(count)):
        code=request.data[str(x)]
        list.append(code)
        row=devBlog(uniqueKeys=uniqueKeys,title='',code=code)
        row.save()
    return JsonResponse({'hello':data})

def getDevBlogTitleData(Request):
    rows=devBlog.objects.filter(code="ThisCode")
    list=[]
    for row in rows:
        list.append({'uniqueKeys':row.uniqueKeys,"title":row.title,"code":row.code})
    return JsonResponse({"data":list})


@api_view(['GET'])
def getDevBlogSinglePostData(request,pk):
    queryset=devBlog.objects.filter(uniqueKeys=pk)
    print(queryset)
    serializer= devBlogSer(queryset,many=True)
    return Response(serializer.data)


class getDevBlogData(ListCreateAPIView):
    queryset=devBlog.objects.filter(code="ThisCode")
    serializer_class=devBlogSer

