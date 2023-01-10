"""devBlogBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('getDevBlogTitleData/', views.getDevBlogTitleData),
    path('devBlogFunc/', views.devBlogFunc),
    path('getDevBlogData/', views.getDevBlogData.as_view()),
    path('getDevBlogSinglePostData/<str:pk>',views.getDevBlogSinglePostData),
    path('search/<str:pk>',views.search),
    path('getStripeData/',views.getStripeData.as_view()),
    path('getStripeServiceData/',views.getStripeServiceData.as_view())
    # path('usersNearData',views.usersNearData.as_view())
    # path('call_method/',views.call_method)
]
