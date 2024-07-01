from django.contrib import admin
from django.urls import path
from .views import index, relative, other

#templates tagging
app_name = 'basic_app'


urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('relative/', relative, name='relative'),
    path('other/', other, name='other'),

]