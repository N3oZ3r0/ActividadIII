import math
import multiprocessing as mp
import numpy as np
import time

#Funcion merge que ordena el array en su totalidad
def merge(*args):
    izq, der = args[0] if len(args) == 1 else args
    izq_length, der_length = len(izq), len(der)
    izq_index, der_index = 0, 0
    merged = []
    while izq_index < izq_length and der_index < der_length:
        if izq[izq_index] <= der[der_index]:
            merged.append(izq[izq_index])
            izq_index += 1
        else:
            merged.append(der[der_index])
            der_index += 1
    if izq_index == izq_length:
        merged.extend(der[der_index:])
    else:
        merged.extend(izq[izq_index:])
    return merged

#Funcion merge que ordena cada trozo del array
def merge_sort(X):
    tam = len(X)

    if tam <= 1:
        return X

    middle = tam // 2
    izq = merge_sort(X[:middle])
    der = merge_sort(X[middle:])

    return merge(izq, der)

def Orden(X):
    cores = mp.cpu_count()
    print("Cores", cores)
    seccion = math.ceil(len(X) / cores)
    print("Size", seccion)
    pool = mp.Pool(processes=cores)
    pool
    print (X)

    X = [X[i * seccion:(i + 1) * seccion] for i in range(cores)]
    X = pool.map(merge_sort, X)

    while len(X) > 1:
        extra = X.pop() if len(X) % 2 == 1 else None
        X = [(X[i], X[i + 1]) for i in range(0, len(X), 2)]
        X = pool.map(merge, X) + ([extra] if extra else [])

    return X[0]


if __name__ == '__main__':
    n = 30
    
    X = np.random.randint(1, 256, n)  # Genero un array de tamaño n con valores aleatorios del 1 al 256

    print('\n\nEl Array original es asi\n\n', X)
    parallel_time = 0
    start = time.perf_counter()
    print('\n\nEl Array ordenado ha quedado asi\n\n', Orden(X))
    parallel_time += time.perf_counter() - start
    print('Average Parallel Time: {:.2f} ms'.format(parallel_time*1000))


