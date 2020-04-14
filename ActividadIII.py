import math
import multiprocessing as mp  # Para trabajar en paralelo

import numpy as np


def Orden(X):
    n_cores = mp.cpu_count()
    print(n_cores)
    dimension = len(X)  # Obtengo num de elementos en el array
    seccion = math.ceil(dimension / n_cores)
    print(seccion)
    MC = mp.RawArray('i', dimension)  # Array MC de memoria compartida donde se almacenaran
    cores = []  # Array para guardar los cores y su trabajo
    for core in range(n_cores):  # Asigno a cada core el trabajo que le toca, ver excel adjunto
        i_MC = min(core * seccion,
                   dimension)  # Calculo i para marcar inicio del trabajo del core en relacion a las filas
        f_MC = min((core + 1) * seccion, dimension)  # Calculo f para marcar fin del trabajo del core, ver excel
        cores.append(mp.Process(target=par_core, args=(X, MC, i_MC, f_MC)))  # Añado al Array los cores y su trabajo
    for core in cores:
        core.start()  # Arranco y ejecuto el trabajo para c/ uno de los cores que tenga mi equipo, ver excel
    for core in cores:
        core.join()  # Bloqueo cualquier llamada hasta que terminen su trabajo todos los cores
    Y = [[0] * dimension for i in range(dimension)]  # Convierto el array unidimensional MC en una matrix 2D (C_2D)
    for i in range(dimension):  # i para iterar sobre las filas de A
        Y[i] = MC[i]  # Guardo el C_2D los datos del array MC
    return Y


def par_core(X, MC, i_MC, f_MC):  # La tarea que hacen todos los cores
    temp = [len(X)]
    for i in range(i_MC, f_MC):  # Size representado en colores en el excel que itera sobre las filas en A
        temp.append(X[i])
    temp.sort()
    MC.append(temp)


if __name__ == '__main__':
    n = 24
    X = np.random.randint(1, 5, n)  # Genero A[21535220][6]con num. aleatorios del 0 al 215, ver excel
    print('\n\nEl Array original es asi\n\n', X)
    print('\n\nEl Array ordenado ha quedado asi\n\n', Orden(X))
