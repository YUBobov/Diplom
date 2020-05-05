#Библиотека для работы с получением ссылок в адресной строке
from django.urls import path
#Из локального приложение импортируем файл views
from . import views
urlpatterns = [
    #Откртие метода из файла views 
    path('', views.index, name='index'),
]