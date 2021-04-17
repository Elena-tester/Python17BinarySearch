def sort_for_list(some_list, default_sort = False):
    global list_of_numbers
    if default_sort:
        some_list.sort()
    else:
        list_of_numbers = merge_sort(some_list)

#алгоритм сортировки слиянием процедура 1
def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 1 (меньше 2х),
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние

#алгоритм сортировки слиянием процедура 2
def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def binary_search(array, element, left, right):
    #global n
    #print("n = ",n)
    #print("array = ", array)
    #print("left = ", left)
    #print("right = ", right)
    #n = n + 1

    if left > right:  # если левая граница превысила правую,
        #return False  # значит элемент отсутствует
        return left # если элемент отсутствует, значит выводим большую позицию, которая требуется в задаче как большая или равная
        # (иначе при успещном поиске она будет равная найденному элементу)

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

print("Введите последовательность чисел через пробел")

sequence_of_numbers_by_string = input()
# место для повышенной сложности: проверка входных данных последовательности чисел через пробел
list_of_numbers_by_string = sequence_of_numbers_by_string.split(" ")
list_of_numbers = list(map(int, list_of_numbers_by_string))

print("Введите число для поиска")

searching_number_by_string = input()
# место для повышенной сложности: проверка входных данных введённого числа для поиска
searching_number = float(searching_number_by_string)

sort_for_list(list_of_numbers)

#n = 0 # переменная для отладки
len_by_list_of_numbers = len(list_of_numbers)
number_of_right_element = binary_search(list_of_numbers, searching_number, 0, len_by_list_of_numbers-1)
number_of_left_element = number_of_right_element - 1

if number_of_right_element == len_by_list_of_numbers:
    print(
        "Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу установить не удалось.\n",
        "Номер позиции элемента, который больше или равен этому числу больше количества элеменртов в списке и равен", number_of_right_element, "!")
elif (number_of_right_element == 0) and (number_of_left_element < 0):
    print(
        "Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу установить не удалось.\n",
        "Номер позиции элемента, который больше или равен этому числу равен 0!")
elif list_of_numbers[number_of_left_element] == searching_number:
    print(
        "Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу установить не удалось.\n",
        "Номер позиции элемента, который перед следующим числом равным искому, является ", number_of_left_element,
        " . Этот элемент = ", list_of_numbers[number_of_left_element])
    #целевое условие задачи ниже
elif list_of_numbers[number_of_left_element] < searching_number and list_of_numbers[number_of_right_element] >= searching_number:
    print("Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу, является ", number_of_left_element)
else:
    print(
        "Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу установить не удалось.\n",
        "Неустановленная ошибка, обратитесь к разрабочику.")

print("Для отсортированного списка: ", list_of_numbers)