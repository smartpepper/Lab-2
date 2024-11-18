import csv
import xml.dom.minidom
from random import randint

def task1():
    with open('books.csv', newline = '') as File:  
        reader = csv.reader(File)
        count = 0
        for row in reader:
            row = str(row)
            if str(row.split(';')[0]) != 'ID':
                nazv = row.split(';')[1]
                if len(nazv) > 30:
                    count += 1
    print(count)

def task2():
    while True:
        text = '---Не найдено---'
        print('Введите автора или напишите "далее"')
        avtor = input()
        if avtor == 'далее':
            break
        with open('books.csv', newline = '') as File:  
            reader = csv.reader(File)
            for row in reader:
                row = str(row)
                if str(row.split(';')[0]) != 'ID':
                    #if (row.split(';')[3] == avtor):  # проверка по автору
                        #print(row.split(';')[1],row.split(';')[6])   # выводит название и дату для проверки
                    if (row.split(';')[3] == avtor) and (int(str(row.split(';')[6])[6:10]) >= 2018):
                        print(row.split(';')[1])
                        text = "---Конец списка---"
        print(text)


                
def task3():
    with open('books.csv', newline = '') as File:
        reader = list(csv.DictReader(File, delimiter = ';'))
        result = open('result.txt', 'w')
        for i in range(20):    
            number = randint(1, 9400)
            result.write(f"{i + 1} {reader[number]['Автор']} - {reader[number]['Название']} - {int(str(reader[number]['Дата поступления'])[6:10])} \n")
            
def task4():
    file = open('currency.xml', 'r')
    data = file.read()
    dom = xml.dom.minidom.parseString(data)
    dom.normalize()   
    elements = dom.getElementsByTagName('Valute')
    valute_disk = {}
    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Name':
                    if child.firstChild.nodeType == 3:
                        Name = child.firstChild.data
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        Code = child.firstChild.data
        valute_disk[Name] = Code
    for key in valute_disk.keys():
        print(key,'-', valute_disk[key])
    file.close()
print('задание 1')
task1()
print('задание 2')
task2()
task3()
print('задание 3')
print('файл создан')
print('задание 4')
task4()
