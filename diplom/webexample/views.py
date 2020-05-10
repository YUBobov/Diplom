#Функция для вывода информации из другого файла
from django.shortcuts import render
#Импорт модели, в которой записаны данные о кабелях
from .models import FTTx, ADSS
#Импорт модуля для разбития записей на страницы
from django.core.paginator import Paginator

#Функция вывода шаблона
def index(request):
    #Возвращаем параметр request и путь к html файлу, который необходимо вывести
    return render(request, 'webexample/homePage.html')

#Функция вывода данных о кабелях
def kabels(request):
    #Организация словаря в котором хранятся обращения к таблицам
    allTabls = {'FTTx':FTTx, 'ADSS': ADSS}
    #Проверяем какой метод используется в запросе
    #Если метод POST, то значит, что значения передуются с формы
    if request.method == 'POST':
        #Используем метод session для того, чтобы запомнить текущие значения для поиска
        request.session['types'] = request.POST["types"]
        request.session['vol'] = request.POST["vol"]
        #Обращение к таблице по выбранному типу кабеля
        #request.POST["types"] забирает значение из атрибута value в форме
        #По этому значению обращаемся к словарю с таблицами
        #Из словаря выбирается необходимая таблица
        #С помощью метода fitler выбираем необходимые нам значения, которые были заданы в таблице
        bd = allTabls.get(request.POST["types"]).objects.filter(volokno=request.POST["vol"])
        #Используем модуль paginator для разбития набора записей в bd на определённое количество
        paginator = Paginator(bd, 3)
        #Проверяем присутсвует ли в наборе параметр page
        if 'page' in request.POST:
            page_num = request.POST['page']
        #Если параметр отсутсвтует, значит клиент запрашивает первую страницу
        else:
            page_num = 1
        #Задаём страницу, которую запрашиавет клиент
        page = paginator.get_page(page_num)
    else:
    #Если используется метод GET, значит, что данные для поиска уже установлены и нужно обращаться к сессии запроса
        bd = allTabls.get(request.session['types']).objects.filter(volokno=request.session['vol'])
        #Используем модуль paginator для разбития набора записей в bd на определённое количество
        paginator = Paginator(bd, 3)
        #Проверяем присутсвует ли в наборе параметр page
        if 'page' in request.GET:
            page_num = request.GET['page']
        #Если параметр отсутсвтует, значит клиент запрашивает первую страницу
        else:
            page_num = 1
        #Задаём страницу, которую запрашиавет клиент
        page = paginator.get_page(page_num)
    context = {'page':page,'bd':page.object_list}
    #Передаём данные с переходом на страцу с их выводом    
    return render(request, 'webexample/kabels.html', context )