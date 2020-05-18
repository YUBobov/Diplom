#Функция для вывода информации из другого файла
from django.shortcuts import render
#Импорт модели, в которой записаны данные о кабелях
from .models import FTTx, ADSS, Tip8, Vkanal, Vgrunt, Raspredelitelnyj, Ognestojkij, Universalnyj

#Функция вывода шаблона
def index(request):
    #Возвращаем параметр request и путь к html файлу, который необходимо вывести
    return render(request, 'webexample/homePage.html')

#Функция вывода данных о кабелях
def kabels(request):
    #Организация словаря в котором хранятся обращения к таблицам
    allTabls = {'FTTx':FTTx, 'ADSS': ADSS, 'Tip8':Tip8, 'Vkanal':Vkanal, 'Vgrunt':Vgrunt, 'Raspred':Raspredelitelnyj, 'Ognest':Ognestojkij, 'Univers':Universalnyj }
    #Обращение к таблице по выбранному типу кабеля
    #request.POST["types"] забирает значение из атрибута value в форме
    #Проеверяем есть ли запрашиваемый тип кабеля в словаре таблиц
    if request.POST["types"] in allTabls:
        #По этому значению обращаемся к словарю с таблицами
        #Из словаря выбирается необходимая таблица
        bd = allTabls.get(request.POST["types"])
        #Передаём данные с переходоим на страцу с их выводом     
        #С помощью метода filter выбираем необходимые нам значения, которые были заданы в таблице
        #Модификатор gte выбирает знчение в поле больше или равное заданному
        context = {'bd':bd.objects.filter(volokno__gte=request.POST["vol"], kN__gte=request.POST["kn"])}
    #Если такой таблицы нет, то передаём пустое значение
    else:
        context = None
    return render(request, 'webexample/kabels.html', context)