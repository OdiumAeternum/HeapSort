import numpy as np
import timeit
import matplotlib.pyplot as plt

def heapify(nums, heap_size, root_index):  
    #Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    #Проверяем существует ли левый дочерний элемент больший, чем корень
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    #То же самое и для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    #Заменяем корневой элемент, если нужно
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):  
    n = len(nums)

    #Строим дерево 
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    #Перемещаем корень в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums

#Проверяем равенство отсортированных массив написанным алгоритмом и встроенной функции Python        
def compare(array1, array2):
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True

#Находим соотношение значений при удвоении
#размера входных данных
def find_relation(t2n, tn):
    relations = []
    for i in range(len(t2n)):
        relations.append({'size': t2n[i]['size'], 'relation': t2n[i]['time']/tn[i]['time']})
    return relations

#Тестирование алгоритма 
def test(n):
    sizes = [10000*n*i for i in range(2,10)] 
    tests = [{'size': size} for size in sizes]
    for i in range(len(sizes)): 
        time = 0
        for j in range(20):
            list_of_nums = [x for x in np.random.randint(0, 100, sizes[i])]
            start = timeit.default_timer()
            list_of_nums_hs = heap_sort(list_of_nums)
            end = timeit.default_timer()
            time += end - start
        list_of_nums_py = sorted(list_of_nums)
        tests[i]['equal'] = compare(list_of_nums_hs, list_of_nums_py)
        tests[i]['time'] = time / 20
    return tests

#Построение графика зависимости времени выполнения алгоритма от
#числа элементов массива
def graph(tn):
    plt.figure(figsize=(9,9))
    plt.title('Зависимость времени выполнения алгоритма от числа элементов')
    plt.xlabel('Число элементов массива')
    plt.ylabel('Время выполнения')
    plt.grid()

    x = []
    y = []
    for exp in tn:
        x.append(exp['size'])
        y.append(exp['time'])

    plt.plot(x, y)
    plt.show()

tn = test(1)
t2n = test(2)

print(tn)
print(t2n)
print(find_relation(t2n,tn))

graph(tn)
