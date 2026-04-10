# Algoritmos de búsqueda

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

#Algoritmos de ordenamiento

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

def selection_sort(lista): 
    n = len(lista) 
    for i in range(n): 
        min_idx = i 
        for j in range(i+1, n): 
            if lista[j] < lista[min_idx]: 
                min_idx = j 
        lista[i], lista[min_idx] = lista[min_idx], lista[i] 
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    right = [x for x in lista if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    left_half = merge_sort(lista[:mid])
    right_half = merge_sort(lista[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def counting_sort(lista):
    if not lista:
        return lista
    max_val = max(lista)
    count = [0] * (max_val + 1)
    for num in lista:
        count[num] += 1
    sorted_list = []
    for i, c in enumerate(count):
        sorted_list.extend([i] * c)
    return sorted_list

def radix_sort(lista):
    if not lista:
        return lista
    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        counting_sort_exp(lista, exp)
        exp *= 10
    return lista
