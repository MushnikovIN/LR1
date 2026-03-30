#Problem 1
f = () #создание кортежа

for i in range(1, 11, 1):
    f += (i,) #перезапись кортежа новым с еще одним элементом

print("Задача 1\nВывод: кортеж", f)



#Problem 2
l = [] #создание списка
s = set(f) #создание множества

for i in s:
    if i % 3 == 0:
        l.append(i*4)
    else:
        l.append(i+6)

print(f"\nЗадача 2\nВвод: множество {s}\nВывод: список {l}")


#Problem 3
d = {} #создание словаря

for i, j in zip(s, l): #for loop by two variables
    d[i] = j

print(f"\nЗадача 3\nВвод:\nмножество {s}\nсписок {l}\nВывод: словарь {d}")


#Problem 4
from random import randint
s = {randint(0, 50) for i in range(10)} #creating set with random ints

print("\nЗадача 4\nВвод: множество", s, "\nВывод:\nмаксимум:", max(s), "\nминимум:", min(s))  


#Problem 5

def func5(start, stop, step):
    l = [] #создание списка по заданным параметрам
    for i in range(start, stop, step):
        l.append(i)
    l.append(stop)

    h = len(list(filter(lambda x : x % 7 == 0, l))) #вычисление количества элементов кратных 7

    sorted_list = sorted(l) #копирование и сортировка списка
    
    if len(sorted_list) % 2 == 0: #если число элементов в списке четное, то медиана вычисляется как среднее между двумя числами со средними индексами в списке
        median = (sorted_list[len(sorted_list)//2] + sorted_list[len(sorted_list)//2 - 1])/2
    else: #если число элементов нечетное, то просто берется медиана 
        median = sorted_list[len(sorted_list)//2]


    if h - median < 0: #если разность между h и медианой меньше нуля, исходный список зеркально отображается
        l.reverse()
        return(l)
    elif h - median > 0: #если больше нуля, список копируется и в начало вставляется полученная разность
        new_list = l.copy()
        new_list.insert(0, h - median)
    else: #если разность равна нулю, функция выдает ошибку
        raise AssertionError("Разность между количеством чисел кратных 7 и медианой всех чисел списка равна нулю")

    return(new_list)

start5 = -50
stop5 = 67
step5 = 2

print(f"\nЗадача 5\nВвод: start = {start5}, stop = {stop5}, step = {step5}\nВывод: {func5(-50, 67, 2)}")


#Problem 6
from numpy import pi
from functools import reduce
from operator import mul


def func6(len_list, width_list):
    S_circles = ()
    for l, w in zip(len_list, width_list):
        S_circles += ((pi*((l/2)**2 + (w/2)**2)),) #перезапись кортежа с добавлением площади очередного круга

    medium = sum(S_circles)/len(S_circles) #вычисление среднего
    S_circles_list = list(filter(lambda x : x < 1.1*medium, S_circles)) #фильтрация только тех площадей, что меньше 110% средней         
    mult = reduce(mul, S_circles_list)/len(len_list) #произведение площадей и деление на число элементов исходных массивов
                
    return mult

#создание входных данных о длинах и ширинах прямоугольников
len_list = [randint(1, 10) for i in range(10)]
width_list = [randint(1, 10) for i in range(10)]

print(f"\nЗадача 6\nВвод:\nдлины = {len_list},\nширины = {width_list}\nВывод: {func6(len_list, width_list)}")



#Problem 7
from time import sleep
print("\nЗадача 7")
def kosti(count_players, name_list):
    res = []
    for i in range(count_players): #цикл бросания костей каждым игроком
        print(f"\n{name_list[i]} бросает кости...")
        for j in range(10):
            sleep(0.2)
            print(f"\r{randint(1,6)}", end="")
        res.append(randint(1,6))

        print(f"\r{name_list[i]} выбросил {res[i]}.", end="")

    if res.count(max(res)) > 1: #если победителей больше одного, выводится результат - ничья
        winner_inds = [i for i in range(count_players) if res[i] == max(res)]
        
        print("\n\nНичья между игроками: ", end = "")
        for i in winner_inds:
            print(name_list[i], end = " ")
    else: #иначе выводится имя победителя
        print("\n\nПобедитель", name_list[res.index(max(res))])


kosti(6, ["Алексей","Сергей","Владимир","Андрей", "Ярослав", "Мария"])

input()








