from django.contrib import admin
from myapp.models import devBlog,StripeDb,StripeServiceDb
# Register your models here.
admin.site.register(devBlog)
admin.site.register(StripeDb)
admin.site.register(StripeServiceDb)
