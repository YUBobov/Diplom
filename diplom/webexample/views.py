#Функция для вывода информации из другого файла
from django.shortcuts import render
#Импорт модели, в которой записаны данные о кабелях
from .models import FTTx, ADSS

#Функция вывода шаблона
def index(request):
    #Возвращаем параметр request и путь к html файлу, который необходимо вывести
    return render(request, 'webexample/homePage.html')

#Функция вывода данных о кабелях
def kabels(request):
    #Организация словаря в котором хранятся обращения к таблицам
    allTabls = {'FTTx':FTTx, 'ADSS': ADSS}
    #Обращение к таблице по выбранному типу кабеля
    #request.POST["types"] забирает значение из атрибута value в форме
    #По этому значению обращаемся к словарю с таблицами
    #Из словаря выбирается необходимая таблица
    bd = allTabls.get(request.POST["types"])
    #Передаём данные с переходоим на страцу с их выводом     
    #С помощью метода fitler выбираем необходимые нам значения, которые были заданы в таблице
    return render(request, 'webexample/kabels.html', {'bd':bd.objects.filter(volokno=request.POST["vol"])})