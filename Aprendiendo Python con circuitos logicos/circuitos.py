"""
Funciones y clases para modelado y simulación de circuitos lógicos.
"""

import matplotlib.pyplot as plt

def tablas():
    """
    Muestra las tablas lógicas AND y OR de dos variables
    y la operación NOT de una variable.
    Los valores son 0 para verdadero y 1 para falso.
    """
    
    # título de la tabla
    print("a b  a and b  a or b  not a")
    
    # muestra cuatro combinaciones de ceros y unos
    # y el resultado de la operación and
    print("{} {}     {}       {}       {}".format(0, 0, 0 and 0, 0 or 0, int(not 0)))
    print("{} {}     {}       {}       {}".format(0, 1, 0 and 1, 0 or 1, int(not 0)))
    print("{} {}     {}       {}       {}".format(1, 0, 1 and 0, 1 or 0, int(not 1)))
    print("{} {}     {}       {}       {}".format(1, 1, 1 and 1, 1 or 1, int(not 1)))


class TablaLogica:
    """Clase con un método para mostrar tablas lógicas AND, OR y NOT."""
    
    def tabla(self):
        """
        Muestra las tablas lógicas AND y OR de dos variables,
        y la tabla NOT de una variable.
        Los valores son 0 para verdadero y 1 para falso.
        """
        # muestra un título
        print("a b  a and b  a or b  not a")

        # muestra las operaciones lógicas para todas las combinaciones
        # de valores de ceros y unos.
        print("{} {}     {}       {}       {}".format(0, 0, 0 and 0, 0 or 0, int(not 0)))
        print("{} {}     {}       {}       {}".format(0, 1, 0 and 1, 0 or 1, int(not 0)))
        print("{} {}     {}       {}       {}".format(1, 0, 1 and 0, 1 or 0, int(not 1)))
        print("{} {}     {}       {}       {}".format(1, 1, 1 and 1, 1 or 1, int(not 1)))


class PuertaLogica:
    """
    Clase base para puertas lógicas de dos entradas.
    """        
    def __init__(self):
        """Inicializa datos de la clase.""" 

        # llama al método entradas con
        # datos de entrada en cero
        self.entradas(0, 0)     
        
    def entradas(self, a, b):
        """Recibe datos de entrada."""
        
        # almacena los parámetros de entradas
        # a y  b en los objetos internos a y b
        self.a = a
        self.b = b
        # llama al método calcula
        self.calcula()
        
    def calcula(self):
        """Las clases derivadas definen su comportamiento."""

        # no ejecuta instrucción y retorna
        pass
    
    def salida(self):
        """Retorna la salida."""
        return self.s


class And(PuertaLogica):
    """
    Modelo de una puerta lógica AND de dos entradas.
    """

    def calcula(self):
        """
        Realiza la operación lógica AND entre las entradas
        y asigna el resultado a la salida.
        """
        self.s = self.a and self.b


class Or(PuertaLogica):
    """Modelo de una puerta lógica OR de dos entradas."""
    
    def calcula(self):
        """
        Realiza la operación lógica OR entre las entradas
        y asigna el resultado a la salida.
        """
        self.s = self.a or self.b


class Xor(PuertaLogica):
    """Modelo de una puerta lógica XOR de dos entradas."""
    
    def calcula(self):
        """
        Realiza la operación lógica OR exclusiva entre las entradas
        y asigna el resultado a la salida.
        """
        
        # compara las entradas por desigualdad,
        # convierte el resultado a entero
        # y asigna el resultado a la salida
        self.s = int(self.a != self.b)


class Not:
    """Modelo de una puerta NOT."""
    
    def __init__(self):
        """Inicializa la salida en 0."""
        self.s = 0
        
    def entrada(self, a):
        """Asigna a la salida el bit complementario de la entrada."""
        
        # aplica el operador not a la entrada, convierte el 
        # resultado a entero y lo asigna a la salida.
        self.s = int(not a)
        
    def salida(self):
        """Retorna la salida."""
        return self.s


class Registro:
    """Modela una memoria o registro de un bit."""
    
    def __init__(self):
        """Crea e inicializa los objetos de la clase."""
        self.d = 0
        self.reloj = 0
        self.habilitador = 0
        self.q = 0
        
    def entradas(self, reloj, habilitador, d):
        """Recibe las entradas y evalúa si actualizar la salida."""
        
        # si el reloj interno es 0 y el reloj externo 1 y el habilitador interno 1
        if self.reloj == 0 and reloj == 1 and self.habilitador == 1:
            # asigna la entrada interna al dato de salida
            self.q = self.d

        # actualiza los objetos internos
        self.d = d                      # dato de entrada
        self.reloj = reloj              # entrada para ingreso de dato
        self.habilitador = habilitador  # entrada de habilitación
        
    def salida(self):
        """Retorna el bit almacenado."""
        return self.q 


class SumadorCompleto:
    """
    Suma tres bits de entrada en dos bits de salida.
    """        
    def __init__(self):
        """Crea las puertas lógicas e inicializa las entradas y salidas a cero."""
        
        # puertas lógicas para el sumador completo
        self.and1 = And()       # and1 es un objeto de clase And
        self.and2 = And()       # and2 es un objeto de clase And
        self.and3 = And()       # and3 es un objeto de clase And
        self.or1 = Or()         #  or1 es un objeto de clase Or
        self.or2 = Or()         #  or2 es un objeto de clase Or
        self.xor1 = Xor()       # xor1 es un objeto de clase Xor
        self.xor2 = Xor()       # xor2 es un objeto de clase Xor

        # ejecuta el método entradas con argumentos en cero
        self.entradas(0, 0, 0)
        
    def entradas(self, a, b, ci):
        """Recibe las entradas del sumador completo y calcula las salidas."""
        # toma las entradas
        self.a = a      # la entrada a  se asigna al objeto interno a
        self.b = b      # la entrada b  se asigna al objeto interno b
        self.ci = ci    # la entrada ci se asigna al objeto interno ci
        
        # ejecuta el método circuito
        self.circuito() # 

    def circuito(self):
        """Modelo estructural de un sumador completo."""

        # bit de acarreo de salida
        # ----------------------------------------------
        # bloque de ands
        self.and1.entradas(self.a, self.b)  # a y b  son entradas de and1
        self.and2.entradas(self.a, self.ci) # a y ci son entradas de and2
        self.and3.entradas(self.b, self.ci) # b y ci son entradas de and3
        nodo1 = self.and1.salida()          # nodo1 es salida de and1
        nodo2 = self.and2.salida()          # nodo2 es salida de and2
        nodo3 = self.and3.salida()          # nodo3 es salida de and3
        # bloque de ors
        self.or1.entradas(nodo1, nodo2)     # nodo1 y nodo2 son entradas de or1
        nodo4 = self.or1.salida()           # nodo4 es salida de or1
        self.or2.entradas(nodo4, nodo3)     # nodo4 y nodo3 son entradas de or2
        self.co = self.or2.salida()         # co es salida de or2
        
        # bit de suma
        # ----------------------------------------------
        # bloque de xors
        self.xor1.entradas(self.a, self.b)  # a y b son entradas de xor1
        nodo5 = self.xor1.salida()          # nodo5 es salida de xor1
        self.xor2.entradas(nodo5, self.ci)  # nodo5 y ci son entradas de xor2
        self.s = self.xor2.salida()         # s es salida de xor2

    def salidas(self):
        """Retorna el acarreo y la suma."""
        # retorna la salida como una tupla de dos elementos
        return self.co, self.s


def tiempos(T, dt):
    """
    Recibe el número de periodos y el tiempo de cambio de nivel lógico.
    Retorna una lista de tiempos desde 0 hasta T con tiempos de cambio 
    agregados después de cada entero entre 1 y T - 1.
    """
    
    t = [0]                 # inicializa una lista con el tiempo 0
    for i in range(1, T):   # para cada valor entre 1 y T - 1
        t.append(i)             # agrega a la lista el tiempo i
        t.append(i + dt)        # agrega a la lista el tiempo i incrementado en dt

    t.append(T)             # agrega el tiempo T
    return t                # retorna la lista de tiempos


def duplica(lista):
    """
    Recibe una lista y retorna otra lista con los elementos duplicados.
    """
    doble = [0]*2*len(lista)        # doble es una lista de ceros, de doble tamaño que lista
    
    for i in range(len(lista)):     # para cada índice de lista
        doble[2*i]     = lista[i]       # el elemento en la posición i de lista se asigna a la posición 2i      de doble
        doble[2*i + 1] = lista[i]       # el elemento en la posición i de lista se asigna a la posición 2i  + 1 de doble
    
    return doble                    # retorna la lista con elementos duplicados


def dibuja(canales, dt, dy):
    """
    Recibe una lista de canales, el tiempo de cambio de nivel lógico y la separación entre canales.
    Muestra las señales comenzando con el primer canal en la parte superior.
    Coloca marcas en los ejes coordenados.
    """

    N = len(canales)        # N toma el número de listas en canales
    T = len(canales[0])     # T toma el número de periodos de la primera lista en canales
    t = tiempos(T, dt)      # t contiene la lista de tiempos
    delta = N               # delta copia a N, el número de listas

    for lista in canales:               # para cada lista en canales
        canal = lista[:]                    # una copia se asigna a canal
        delta = delta - 1                   # delta disminuye en 1
        for i in range(len(canal)):             # para cada índice de la lista canal
            if canal[i] == 1:                       # si el elemento indizado es 1
                canal[i] = canal[i] - dy                # se le disminuye en dy
            canal[i] = canal[i] + delta             # agrega delta al elemento indizado 

        plt.plot(t, duplica(canal))         # grafica los datos duplicados de canal versus t
        
    # marcas en el eje y
    y = [0]*(2*N)                   # y es una lista del doble número de canales en cero
    for i in range(N):              # para cada índice i desde 0 hasta N - 1
        y[2*i] = i                      # el elemento de y indizado por 2i     recibe el valor i, donde irá una marca 0
        y[2*i + 1] = i + 1 - dy         # el elemento de y indizado por 2i + 1 recibe el valor i + 1 - dy, donde irá una marca 1
    
    # marcas en el eje x
    plt.yticks(y, [0, 1]*N)         # en las posiciones definidas por y se colocan marcas 0 y 1 alternadamente sobre el eje y
    plt.xticks(range(0, T + 1))     # las posiciones desde 0 hasta T se marcan con los números desde 0 hasta T sobre el eje x
    
    plt.grid()      # muestra una grilla
    plt.show()      # muestra todos los gráficos


def cronograma(titulo, canales, leyendas, colores, dt = 0.2, dy = 0.2, escala = 1):
    """
    Muestra señales digitales como cronogramas, comenzando con la primera
    señal en la parte superior.
    Recibe un título, la lista de canales, la lista de etiquetas,
    el retardo de cambio, la separación entre canales, y el
    factor de escala para la altura de la ventana de visualización. 
    """

    N = len(canales)        # N toma el número de listas en canales
    T = len(canales[0])     # T toma el número de periodos de la primera lista en canales
    t = tiempos(T, dt)      # t contiene la lista de tiempos

    delta = N               # delta copia a N, el número de listas,
                            # y se utiliza para desplazar las señales en el eje y

    # crea una figura para la gráfica con tamaño
    # proporcional al número de datos por canal (anchura)
    # y número de canales (altura) con el factor de escala
    plt.figure(figsize=(T, N*escala))


    for lista in canales:               # para cada lista en canales
        canal = lista[:]                    # una copia se asigna a canal
        delta = delta - 1                   # delta disminuye en 1
        for i in range(len(canal)):             # para cada índice de la lista canal
            if canal[i] == 1:                       # si el elemento indizado es 1
                canal[i] = canal[i] - dy                # se le disminuye en dy
            canal[i] = canal[i] + delta             # agrega delta al elemento indizado 

        # grafica los datos duplicados de canal versus t
        # con sus respectivos colores, desde 0 hasta N -1
        plt.plot(t, duplica(canal), colores[N - delta - 1])         
        
       
    # marcas en el eje y
    y = [0]*(2*N)                   # y es una lista del doble número de canales en cero
    for i in range(N):              # para cada índice i desde 0 hasta N - 1
        y[2*i] = i                      # el elemento de y indizado por 2i     recibe el valor i, donde irá una marca 0
        y[2*i + 1] = i + 1 - dy         # el elemento de y indizado por 2i + 1 recibe el valor i + 1 - dy, donde irá una marca 1

    # marcas en el eje x
    plt.yticks(y, [0, 1]*N)         # en las posiciones definidas por y se colocan marcas 0 y 1 alternadamente sobre el eje y
    plt.xticks(range(0, T + 1))     # las posiciones desde 0 hasta T se marcan con los números desde 0 hasta T sobre el eje x
    
    plt.legend(leyendas, loc='best')    # etiquetas de las señales
    plt.title(titulo)                   # título de la figura
    plt.xlabel('tiempo')                # etiqueta del eje x
    plt.ylabel('señales')               # etiqueta del eje y

    plt.xlim([0, T])    # límites de los valores del eje x, entre 0 y T
    plt.ylim([-dy, N])  # límites de los valores del eje y, entre -dy y N
    
    plt.grid()      # muestra una grilla
    plt.show()      # muestra todos los gráficos


def simular_sumador_completo():
    """Muestra la tabla y el cronograma de un sumador completo."""

    sumador = SumadorCompleto() # sumador es un objeto de tipo SumadorCompleto
    a = [0]*4 + [1]*4           # a  : [0, 0, 0, 0, 1, 1, 1, 1]
    b = ([0]*2 + [1]*2)*2       # b  : [0, 0, 1, 1, 0, 0, 1, 1]
    ci = [0, 1]*4               # ci : [0, 1, 0, 1, 0, 1, 0, 1]

    # recipientes para las salidas
    co = [0]*8      # co : [0, 0, 0, 0, 0, 0, 0, 0]
    s  = [0]*8      #  s : [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(8):                      # para cada valor de i desde 0 hasta 7
        sumador.entradas(a[i], b[i], ci[i])     # las entradas del sumador son los elementos de a, b y ci indizados por i
        co[i], s[i] = sumador.salidas()         # las salidas se almacenan en los elementos de co y s indizados por i

    # muestra las señales en el cronograma
    cronograma("Sumador completo",                              # título del gráfico 
               [a, b, ci, co, s],                               # lista de señales
               ['a', 'b', 'cin', 'cout', 's'],                  # lista de nombres
               ['blue', 'blue', 'green', 'orangered', 'orange'])  # lista de colores


def binario(entero, bits = 4):
    """
    Recibe un número entero y retorna una lista
    de bits representando al número binario equivalente.
    binario(4)    -> [0, 1, 0, 0]
    binario(4, 5) -> [0, 0, 1, 0, 0]
    binario(4, 2) -> [1, 0, 0]
    """
    
    # esta función procesa números enteros
    if type(entero) != int:
        print("El argumento debe ser un entero.")
        return      # retorna sin ejecutar más instrucciones

    s = "{:b}".format(entero)       # convierte un número a dígitos binarios como texto
    s = s.zfill(bits)               # agrega ceros desde la izquierda hasta completar el número de bits solicitados

    b = []                          # lista de bits, inicialmente vacía
    for i in s:                     # para cada caracter en s
        b.append(int(i))                # convierte el caracter a entero y lo agrega a la lista de bits        

    # retorna la lista
    return b



def numero(lista):
    """
    Convierte una lista de bits a número entero.
    numero([0, 1, 0, 1])    -> 5
    numero([1, 1, 1, 1, 0]) -> 30
    """

    # esta función procesa listas
    if type(lista) != list:
        print("El argumento debe ser una lista.")
        return      # termina la ejecución de la función

    n = lista[0]        # número acumulador, inicializado con el bit más significativo, el primero de la lista

    for i in lista[1:]: # para cada elemento de la lista desde el segundo hasta el final
        n = 2*n + i         # al doble del acumulador agrega el elemento de la lista y asigna el resultado al acumulador
    
    # retorna el número
    return n


class Sumador3bits:
    """Modelo de un sumador de números de tres bits."""

    def __init__(self, modelo = "estructural"):
        """Inicializa todos los valores en cero."""
        self.modelo = modelo

        if self.modelo == "estructural":
            # crea tres objetos de tipo SumadorComleto
            self.sc1 = SumadorCompleto()
            self.sc2 = SumadorCompleto()
            self.sc3 = SumadorCompleto()

        # llama al método entradas con todos los bits en cero.
        self.entradas([[0, 0, 0], [0, 0, 0], 0])
        
    def entradas(self, lista):
        """Recibe las entradas y determina las salidas."""
        # asigna las entradas a los objetos internos
        self.a = lista[0]
        self.b = lista[1]
        self.ci = lista[2]
        
        # selecciona el método para calcular las salidas
        # de acuerdo al valor del modelo
        if self.modelo == "estructural":
            self.circuito()
        else:
            self.funcion()
        
    def funcion(self):
        """Calcula las salidas sumando y separando números."""
        
        suma = numero(self.a) + numero(self.b) + self.ci    # suma los números
        self.co = suma // 8                                 # extrae el cociente
        self.s = binario(suma % 8, 3)                       # extrae la suma de tres bits

    def circuito(self):
        """Modela un circuito estructuralmente."""

        self.sc1.entradas(self.a[2], self.b[2], self.ci)    # entradas del sumador de menor peso
        co1, s1 = self.sc1.salidas()                        # con salidas asignadas a co1 y s1 

        self.sc2.entradas(self.a[1], self.b[1], co1)        # entradas del segundo sumador
        co2, s2 = self.sc2.salidas()                        # con salidas asignadas a co21 y s2 
        
        self.sc3.entradas(self.a[0], self.b[0], co2)        # entradas del sumador de mayor peso
        self.co, s3 = self.sc3.salidas()                    # con salidas asignadas a self.co y s3 
        
        self.s = [s3, s2, s1]       # la salida self.s se forma con tres bits

    def salidas(self):
        return self.co, self.s


def verificar_sumador3bits():
    """Verifica que los modelos del sumador provean las mismas respuestas."""
    
    z1 = Sumador3bits("estructural")
    z2 = Sumador3bits("funcional")

    errores = 0

    for n in range(128):
        bits = binario(n, 7)        # convierte el número n en lista de 7 bits
        a = bits[0:3]               # a toma los tres primeros,   0 1 2
        b = bits[3:6]               # b toma los tres siguientes, 3 4 5
        ci = bits[6]                # c toma el séptimo bit           6

        # ambos modelos reciben las mismas entradas
        z1.entradas([a, b, ci])
        z2.entradas([a, b, ci])
        
        # cada salida se almacena en objetos diferentes
        s1 = z1.salidas()
        s2 = z2.salidas()
        
        # compara los acarreos y las salidas
        if s1 != s2:
            errores += 1
            if errores == 1:
                print("### Depurar casos: ------------------------------")
                print("                           estructural      funcional")
                print("    a         b     ci    co     s        co     s")
            print("{} {} {}    {}  {}".format(bits[0:3], bits[3:6], bits[6], s1, s2))

    if errores == 0:
        print("Éxito, todos los casos coincidieron.")


class Registro3bits:
    """Modelo de un registro de 3 bits."""

    def __init__(self, modelo = "estructural"):
        """Recibe un modelo e inicializa sus tres entradas y su salida."""
        
        self.modelo = modelo
        self.q = [0]*3
        
        if self.modelo == "estructural":
            # crea una lista de registros
            self.registro = [Registro(), Registro(), Registro()]
        else:
            self.d = [0]*3
            self.reloj = 0
            self.habilitador = 0

        self.entradas(0, 0, [0]*3)

    def entradas(self, reloj, habilitador, d):
        """Recibe las entradas y utiliza el modelo seleccionado."""
        
        if self.modelo == "estructural":
            self.circuito(reloj, habilitador, d)
        else:
            self.funcion(reloj, habilitador, d)

    def funcion(self, reloj, habilitador, d):
        """Procesa datos algorítmicamente."""
        
        if self.reloj == 0 and reloj == 1 and self.habilitador == 1:
            self.q = self.d
        
        self.d = d
        self.reloj = reloj
        self.habilitador = habilitador

    def circuito(self, reloj, habilitador, d):
        """Procesa datos estructuralmente."""
        
        # maneja los registros individuales en paralelo.
        for i in range(3):
            self.registro[i].entradas(reloj, habilitador, d[i])
            self.q[i] = self.registro[i].salida()
        # self.q[0] = 0     # provoca diferencias con el modelo funcional

    def salidas(self):
        """Retorna la salida."""
        return self.q
    
    
def simular_registros3bits():
    """
    Muestra un cronograma para los modelos del registro de tres bits.
    """
    
    # crea los dos modelos de registro
    estructural = Registro3bits()
    funcional = Registro3bits("funcional")

    # patrones o vectores de entrada
    N = 8
    d2, d1, d0 = [0]*N, [0]*N, [0]*N
    for i in range(N):
        bits = binario(i, 3)
        d2[i] = bits[0]
        d1[i] = bits[1]
        d0[i] = bits[2]

    reloj = [0, 1]*N        # cambia a [1, 0]*N y nota la diferencia en la captura de datos.

    # duplica los valores para mostrar el mismo dato en cada ciclo de reloj
    d2 = duplica(d2)
    d1 = duplica(d1)
    d0 = duplica(d0)

    hab   = [1]*2*N

    # recipientes para las salidas
    e2, e1, e0 = [0]*2*N, [0]*2*N, [0]*2*N
    f2, f1, f0 = [0]*2*N, [0]*2*N, [0]*2*N

    # rango de simulación
    for i in range(2*N):
        # entradas de los circuitos
        d = [d2[i], d1[i], d0[i]]       # tres bits de entrada
        estructural.entradas(reloj[i], hab[i], d)
        funcional.entradas(reloj[i], hab[i], d)
        # salidas
        e2[i], e1[i], e0[i] = estructural.salidas()
        f2[i], f1[i], f0[i] = funcional.salidas()

    # visualización
    cronograma("Registro de tres bits", 
               [hab, d2, d1, d0, reloj, e2, e1, e0, f2, f1, f0],
               ['hab', 'd2', 'd1', 'd0', 'reloj', 
                'e2', 'e1', 'e0', 'f2', 'f1', 'f0'],
               ['red', 'blue', 'blue', 'blue', 'orangered', 
                'green', 'green', 'green', 'orange', 'orange', 'orange'],
              escala = 0.6)    
    
    
    
class Contador3bits:
    """Modelo de un contador de tres bits."""

    def __init__(self, modelo = "estructural"):
        """Recibe un modelo e inicializa los valores de los objetos en cero."""
        self.q = [0]*3

        self.modelo = modelo
        if self.modelo == "estructural":
            self.registro = Registro3bits()
            self.sumador = Sumador3bits()
        else:
            self.reloj = 0
            self.habilitador = 0
        
        self.entradas([0, 0])
        
    def entradas(self, lista):
        """
        Recibe una lista de entradas y selecciona el método 
        de procesamiento de acuerdo al modelo.
        """
        if self.modelo == "estructural":
            self.circuito(lista)
        else:
            self.funcion(lista)

    def funcion(self, lista):
        """Procesa las señales algorítmicamente."""
        
        reloj = lista[0]
        habilitador = lista[1]

        if self.reloj == 0 and reloj == 1 and self.habilitador == 1:
            n = numero(self.q)      # n es q convertido a entero
            if n == 7:              # si n es 7
                n = 0                   # pasa a ser 0
            else:                   # sino
                n = n + 1               # incrementa en uno
                
            self.q = binario(n, 3)  # actualiza la salida con n convertido a binario de tres bits
            
            #if n == 7:           # quitar comentarios para provocar errores
            #    self.q[0] = 0
        
        self.reloj = reloj
        self.habilitador = habilitador

    def circuito(self, lista):
        """Define un circuito con un registro y un sumador de tres bits."""
        
        reloj = lista[0]
        habilitador = lista[1]

        self.sumador.entradas([self.q, [0, 0, 1], 0])   # sumador con entradas q, 1 y 0
        c, d = self.sumador.salidas()                   # acarreo para c, suma para d
        self.registro.entradas(reloj, habilitador, d)   # registro con entrada de datos d
        self.q = self.registro.salidas()                # salida para q

    def salidas(self):
        """Retorna la cuenta q."""
        return self.q    
    
    
def verificar(modelo1, modelo2, vectores):
    """
    Recibe dos circuitos, modelo1 y modelo2, y compara sus salidas
    utilizando las entradas provistas como listas en el objeto vectores.
    Los circuitos deben tener métodos entradas que recibre una lista
    de entradas y métodos salidas que retornan las respuestas de
    los circuitos."""
    
    
    # convierte los N vectores de E elementos a una lista de tamaño E de listas de tamaño N
    # ------------------------------------------------
    # [a, b, c], [A, B, C] -> [[a, A], [b, B], [c, C]]           vectores -> casos
    #
    # a b c         a A
    # A B C     ->  b B
    #               c C
    # ------------------------------------------------
    N = len(vectores)       # N es el número de listas en vectores
    E = len(vectores[0])    # E es el número de datos por cada lista en vectores
    casos = []
    # agrega E listas con N elementos en 0
    for i in range(E):          
        casos.append([0]*N)

    # copia los elementos de las listas de vectores
    # en las listas de casos, intercambiando índices
    for i in range(N):                      
        for j in range(E):
            casos[j][i] = vectores[i][j]

    errores = 0

    print("caso - modelo 1 - modelo 2)")
    for i in casos:
        modelo1.entradas(i)
        modelo2.entradas(i)
        
        # compara las salidas del modelo con las salidas esperadas
        print("{} {} {}".format(i, modelo1.salidas(), modelo2.salidas()), end = "")
        if modelo1.salidas() != modelo2.salidas():
            errores += 1
            print(" depurar ")
        else:
            print()
            
            
def simular_contador3bits(contador, ciclos):
    """
    Muestra el cronograma de un contador.
    Recibe el contador y el número de ciclos de reloj.
    """

    # patrones o vectores de entrada
    reloj = [0, 1]*ciclos
    N = 2*ciclos
    habilitador = [1]*N
    
    errores = 0    # para llevar la cuenta de resultados diferentes

    # listas recipientes para las salidas
    q2, q1, q0 = [0]*N, [0]*N, [0]*N  # del contador estructural

    # N periodos de simulación
    for i in range(N):

        # las posiciones i de las listas reloj y habilitador
        # son las entraddas de reloj y habilitador de los contadores
        clock = reloj[i]
        enable = habilitador[i]
        contador.entradas([clock, enable])

        # las salidas de cada contador se almacenan en
        # las posiciones indizadas de las listas recipientes
        q2[i], q1[i], q0[i] = contador.salidas()

    cronograma("Contador de tres bits",                     # título de la gráfica
               [reloj, q2, q1, q0],                         # lista de canales
               ['reloj', 'q2', 'q1', 'q0'],                 # etiquetas de los canales
               ['orangered', 'green', 'green', 'green'],    # colores de las señales
               dt = 0.1)         # tiempo de cambio de nivel lógico
    

    
class Semaforo:
    """
    Modela un semáforo de cuatro estados con periodos
    3T, T, 3T y T. Las salidas son dos grupos de 
    tres luces de colores rojo, ámbar y verde.
    """

    def __init__(self, modelo = "estructural"):
        """Recibe un modeo e inicializa los valores de los objetos en cero."""
        self.a = [1, 0, 0]
        self.b = [0, 0, 1]
        self.modelo = modelo
        if self.modelo == "estructural":
            # contador de tres bits
            self.contador = Contador3bits()
            # dos puertas Not
            self.not1, self.not2 = Not(), Not()
            # cinco puertas And
            self.and1, self.and2 = And(), And()
            self.and3, self.and4 = And(), And()
            self.and5 = And()
        else:
            self.reloj = 0
            self.q = [0, 0, 0]

        self.entradas([0])
        
    def entradas(self, lista):
        """Selecciona el modelo para procesar las señales."""
        if self.modelo == "estructural":
            self.circuito(lista)
        else:
            self.funcion(lista)
        
    def funcion(self, lista):
        """Procesa las señales algorítmicamente."""
        
        reloj = lista[0]
        if self.reloj == 0 and reloj == 1:
            n = numero(self.q) + 1      # n es la lista de tres bits convertida a entero incrementado en 1
            if n == 8:                  # si n es 8
                n = 0                       # se vuelve 0
            self.q = binario(n, 3)      # la cuenta convierte n en lista de tres bits

        # asegura que n sea el valor actual de q
        n = numero(self.q)
        # Si n es 0, 1 o 2, los tiempos del primer estado de luces
        if n < 3:                                   #   A      B
            # activa el Rojo de A y el Verde de B
            self.a, self.b = [1, 0, 0], [0, 0, 1]   # ROJO   VERDE
        # Si n es 3, segundo estado
        elif n == 3:
            self.a, self.b = [1, 0, 0], [0, 1, 0]   # ROJO   AMBAR
        # Si n es 4, 5 o 6, tercer estado
        elif n < 7:
            self.a, self.b = [0, 0, 1], [1, 0, 0]   # VERDE  ROJO
        # Si n es 7, cuarto estado
        else:
            self.a, self.b = [0, 1, 0], [1, 0, 0]   # AMBAR  ROJO
            
        self.reloj = reloj

    def circuito(self, lista):
        """Utiliza un modelo de circuito para procesar las señales."""
        ROJO, AMBAR, VERDE = 0, 1, 2                # índices para las luces

        reloj = lista[0]
        
        self.contador.entradas([reloj, 1])            # contador con entradas reloj y 1 (habilitado)
        q = self.contador.salidas()                  # q es una lista de tres bits, q[0], q[1], q[2]

        self.not1.entrada(q[0])                     # not1 tiene entrada q[0]
        self.a[ROJO] = self.not1.salida()           # la salida de not1 controla la luz roja de A
        
        self.b[ROJO] = q[0]                         # El bit q[0] maneja la luz roja de B

        self.and1.entradas(q[1], q[2])              # las entradas de and1 son q[1] y q[2]
        nodo1 = self.and1.salida()                  # nodo1 recibe la salida de and1
        
        self.not2.entrada(nodo1)                    # not2 tiene a nodo1 de entrada
        nodo2 = self.not2.salida()                  # y su salida va a nodo2
        
        self.and2.entradas(q[0], nodo2)             # and2 tiene entradas q[0] y nodo2
        self.a[VERDE] = self.and2.salida()          # y su salida controla la luz verde de A
        
        self.and3.entradas(self.a[ROJO], nodo2)     # and3 tiene de entradas a la luz roja de A y a nodo2
        self.b[VERDE] = self.and3.salida()          # y su salida maneja la luz verde de B
        
        self.and4.entradas(self.a[ROJO], nodo1)     # and4 toma como entradas la luz roja de A y el nodo2
        self.b[AMBAR] = self.and4.salida()          # y su salida maneja la luz ámbar de B
        
        self.and5.entradas(q[0], nodo1)             # and5 tiene entradas q[0] y nodo1

        self.and5.entradas(q[0], 0)  # quitar el comentario para provocar error en la depuración
        
        self.a[AMBAR] = self.and5.salida()          # y su salida controla la luz ámbar de A
    
    def salidas(self):
        """Retornas dos listas representando el estado de las luces."""
        return self.a, self.b
    

def simular_semaforo(semaforo, N):
    """Simulación del semáforo para visualización de las señales en un cronograma.
    Recibe el número de periodos de simulación."""
    
    # listas de datos, con N elementos en cero,
    # para el reloj y las seis luces
    temporizador = [0]*N
    rojoA, ambarA, verdeA = [0]*N, [0]*N, [0]*N
    rojoB, ambarB, verdeB = [0]*N, [0]*N, [0]*N

    reloj = 0       # señal de reloj

    for i in range(N):
        # entradas y salidas del semáforo
        semaforo.entradas([reloj])
        p, q = semaforo.salidas()

        # registra los datos para el cronograma
        temporizador[i] = reloj
        rojoA[i], ambarA[i], verdeA[i] = p[0], p[1], p[2]
        rojoB[i], ambarB[i], verdeB[i] = q[0], q[1], q[2]

        # cambia el estado del reloj
        reloj = 1 - reloj

    # muestra las señales
    cronograma("Semáforo", 
               [temporizador, rojoA, ambarA, verdeA, rojoB, ambarB, verdeB],
               ['reloj', 'Rojo A', 'Ambar A', 'Verde A', 'Rojo B', 'Ambar B', 'Verde B'],
               ['blue', 'red', 'orange', 'green', 'red', 'orangered', 'green'], escala = 1)    
    
    
def simulacion_textual():
    """Muestra los nombres de las luces encendidas en cada estado."""

    semaforo = Semaforo()
    reloj = 0
    luz = ['ROJO', 'AMBAR', 'VERDE']
    print('ciclo   A       B   reloj')
    for t in range(20):
        
        semaforo.entradas([reloj])
        
        a, b = semaforo.salidas()

        for i in range(3):
            if a[i] == 1:
                indice1 = i
                break               # si se encontró un 1 no es necesario seguir iterando la lista

        for i in range(3):
            if b[i] == 1:
                indice2 = i
                break

        print("{:3}   {:5} - {:5}   {}".format(t//2 + 1, luz[indice1], luz[indice2], reloj))
        
        reloj = int(not reloj)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




