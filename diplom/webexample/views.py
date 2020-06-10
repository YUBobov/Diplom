#Функция для вывода информации из другого файла
from django.shortcuts import render
#Импорт модели, в которой записаны данные о кабелях
from .models import FTTx, ADSS, Tip8, Vkanal, Vgrunt, Raspredelitelnyj, Ognestojkij, Universalnyj

#Функция для заполнения полей формы
def polya():
    allTabls = {'FTTx':FTTx, 'ADSS': ADSS, 'Tip8':Tip8, 'Vkanal':Vkanal, 'Vgrunt':Vgrunt, 'Raspred':Raspredelitelnyj, 'Ognest':Ognestojkij, 'Univers':Universalnyj }
    #Массивы данных для количества волокон и кН
    allKn = []
    allVol = []
    #Обходим все таблицы с кабелями по ключу
    for i in allTabls:
        #Используя имя ключа извлекаем модель с кабелями
        bd = allTabls.get(i)
        #Извлечение значений из заданных полей
        for oneEl in bd.objects.values('volokno','kN'):
            #Добавляем уникальные значения в массивы
            #Делаемя замену запятой на точку для преобразования к числу с плавающей точкой
            if float(oneEl['kN'].replace(',','.')) not in allKn:
                allKn.append(float(oneEl['kN'].replace(',','.')))
            if oneEl['volokno'] not in allVol:
                allVol.append(oneEl['volokno'])
    allKn.sort()
    allVol.sort()
    #Составляем словарь для передачи на клиент
    #Возвращаем словарь
    return {'allKn':allKn, 'allVol':allVol}

#Функция вывода шаблона
def index(request):
    #Возвращаем параметр request и путь к html файлу, который необходимо вывести
    return render(request, 'webexample/homePage.html', polya())

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
        #Производится проверка параметров для филтьтрации
        #Если в количестве волокон и кН указан параметр "Не выбрано"
        if (request.POST["vol"] == "None") and (request.POST["kn"] == "None"):
            #С помощью метода filter выбираем необходимые нам значения, которые были заданы в таблице
            #Модификатор __gte выбирает знчение в поле больше или равное заданному
            context = {'bd':bd.objects.all()}
        #Иначе происходит проверка по параметрам в отдельности
        elif request.POST["vol"] == "None":
            context = {'bd':bd.objects.filter(volokno=request.POST["kn"])}
        elif request.POST["kn"] == "None":
            context = {'bd':bd.objects.filter(volokno=request.POST["vol"])}
        else:     
            context = {'bd':bd.objects.filter(volokno=request.POST["vol"], kN=request.POST["kn"])}
        #Обхединяем словарь с данными о кабелях и словарь полей
        context.update(polya())
    #Если такой таблицы нет, то передаём пустое значение
    else:
        #Выводим словарь для заполнения полей формы
        context = polya()
        #Передаём данные с переходоим на страцу с их выводом
    return render(request, 'webexample/kabels.html', context)