#Функция для вывода информации из другого файла
from django.shortcuts import render
#Функция вывода шаблона
def index(request):
    #Возвращаем параметр request и путь к html файлу, который необходимо вывести
    return render(request, 'webexample/homePage.html')
