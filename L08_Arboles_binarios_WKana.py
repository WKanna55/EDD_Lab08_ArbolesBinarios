"""
Ejercicio 01: Implementacio de un arbol binario de busqueda(inicio)
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.derecha = None
        self.izquierda = None

class BusquedaArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato, raiz):
        if raiz is None:
            return Nodo(dato)
        else:
            if dato > raiz.dato:
                raiz.derecha = self.insertar(dato, raiz.derecha)
            else:
                raiz.izquierda = self.insertar(dato, raiz.izquierda)
        return raiz

    def eliminar(self):
        pass

    def buscar(self, dato, raiz):
        if raiz is None:
            return False
        else:
            if dato == raiz.dato:
                return True
            if dato > raiz.dato:
                return self.buscar(dato, raiz.derecha)
            else:
                return self.buscar(dato, raiz.izquierda)


    def in_order(self, raiz):
        if raiz != None:
            self.in_order(raiz.izquierda)
            print(raiz.dato)
            self.in_order(raiz.derecha)

    def pre_order(self, raiz):
        if raiz != None:
            print(raiz.dato)
            self.pre_order(raiz.izquierda)
            self.pre_order(raiz.derecha)

    def post_order(self, raiz):
        if raiz != None:
            self.post_order(raiz.izquierda)
            self.post_order(raiz.derecha)
            print(raiz.dato)

    def in_order_niveles(self, raiz, nivel = 0):
        if raiz != None:
            self.in_order_niveles(raiz.izquierda, nivel +1)
            print((nivel * 4 * "-") + str(raiz.dato))
            self.in_order_niveles(raiz.derecha, nivel +1)

    """
    Ejercicio 01: Implementacio de un arbol binario de busqueda(fin)
    """

    """
    Ejercicio 02: Hallar la profundidad(inicio)
    """
    def depth(self, raiz):
        if raiz is None:
            return -1
        return max(self.altura(raiz.izquierda), self.altura(raiz.derecha)) + 1
    """
    Ejercicio 02: Hallar la profundidad(fin)
    """

    """
    Ejercicio 03: Hallar la altura(inicio)
    """
    def altura(self, raiz):
        if raiz is None:
            return -1
        return max(self.altura(raiz.izquierda), self.altura(raiz.derecha)) + 1

    """
    Ejercicio 03: Hallar la altura(fin)
    """

    """
    Ejercicio 04: Identificar maximo y minimo(inicio)
    """
    def min(self, raiz):
        if raiz.izquierda == None:
            return raiz.dato
        return self.min(raiz.izquierda)

    def max(self, raiz):
        if raiz.derecha == None:
            return raiz.dato
        return self.max(raiz.derecha)
    """
    Ejercicio 04: Identificar maximo y minimo(fin)
    """

    """
    Ejercicio 05: Numero de Nodos Hoja(inicio)
    """
    def num_hojas(self, raiz):
        if raiz != None:
            if raiz.derecha == None and raiz.izquierda == None:
                return 1
            else:
                return sum([self.num_hojas(raiz.derecha), self.num_hojas(raiz.izquierda)])
        else:
            return 0

    """
    Ejercicio 05: Numero de Nodos Hoja(fin)
    """

    """
    Ejercicio 06: Nodos Hermanos(inicio)
    """
    def hermanos(self, dato1, dato2, raiz):
        if raiz != None and raiz.izquierda != None and raiz.derecha != None:
            if dato1 == raiz.derecha.dato and dato2 == raiz.izquierda.dato or dato1 == raiz.izquierda.dato and dato2 == raiz.derecha.dato:
                print("hermanos")
                return True
            else:
                return bool(sum([self.hermanos(dato1, dato2, raiz.izquierda), self.hermanos(dato1, dato2, raiz.derecha)]))
        return False

    """
    Ejercicio 06: Nodos Hermanos(fin)
    """

    """
    Ejercicio 07: Tamaño del arbol(inicio)
    """
    def total_nodos(self, raiz):
        if raiz != None:
            return 1 + self.total_nodos(raiz.izquierda) + self.total_nodos(raiz.derecha)
        else:
            return 0

    """
    Ejercicio 07: Tamaño del arbol(fin)
    """

    """
    Ejercicio 08: Obtener ancestros(inicio)
    """
    def obtener_ancestro(self, dato, raiz):
        if raiz is None:
            return False
        else:
            if raiz.izquierda != None and dato == raiz.izquierda.dato:
                return raiz.dato
            if raiz.derecha != None and dato == raiz.derecha.dato:
                return raiz.dato
            if dato > raiz.dato:
                return self.obtener_ancestro(dato, raiz.derecha)
            else:
                return self.obtener_ancestro(dato, raiz.izquierda)

    """
    Ejercicio 08: Obtener Ancestros(fin)
    """

    """
    Ejercicio 09: Verificar si es Arbol de busqueda(inicio)
    """
    def verificar_bst(self, raiz):
        if raiz != None:
            if raiz.izquierda != None and raiz.izquierda.dato > raiz.dato:
                return False
            if raiz.derecha != None and raiz.derecha.dato < raiz.dato:
                return False
            if raiz.izquierda != None and raiz.izquierda.dato < raiz.dato:
                return True
            if raiz.derecha != None and raiz.derecha.dato > raiz.dato:
                return True
            if raiz.izquierda != None:
                return self.verificar_bst(raiz.izquierda)
            if raiz.derecha != None:
                return self.verificar_bst(raiz.derecha)
        else:
            return
    """
    Ejercicio 09: Verificar si es Arbol de busqueda(fin)
    """

    """
    Ejercicio 10: Nodos a K distancia(inicio)
    """
    def nodo_k_distancia(self, nodo, distancia, raiz):

        def dist_subarbol(subraiz):
            if subraiz == None:
                return -1
            return max(dist_subarbol(subraiz.izquierda), dist_subarbol(subraiz.derecha)) +1

        def buscar_nodos(dist, subraiz):
            if subraiz != None:
                if dist == 0:
                    return subraiz.dato
                else:
                    return [buscar_nodos(dist-1, subraiz.izquierda), buscar_nodos(dist-1, subraiz.derecha)]
            else:
                return


        if raiz != None:
            if raiz.dato == nodo:
                print("inicio nodo: " + str(nodo))
                if distancia > dist_subarbol(raiz):
                    raise Exception("sin nodos, fuera del arbol")
                else:
                    print("distancia restante: " + str(dist_subarbol(raiz)))
                    print("distancia a recorrer: " + str(distancia))
                    print("Nodos:")
                    return buscar_nodos(distancia, raiz)
            if nodo > raiz.dato:
                return self.nodo_k_distancia(nodo, distancia, raiz.derecha)
            else:
                return self.nodo_k_distancia(nodo, distancia, raiz.izquierda)
        else:
            return

    """
    Ejercicio 10: Nodos a K distancia(fin)
    """

"""
Pruebas para el arbol binario
"""

bst = BusquedaArbolBinario()
bst.raiz = Nodo(8)
bst.insertar(4, bst.raiz)
bst.insertar(15, bst.raiz)
bst.insertar(1, bst.raiz)
bst.insertar(6, bst.raiz)
bst.insertar(13, bst.raiz)
bst.insertar(18, bst.raiz)
bst.insertar(14, bst.raiz)
"""
                8
        4               15
    1       6       13      18
   .  .   .   .    .  14   .   .
"""

#bst.in_order_niveles(bst.raiz)
#print(bst.buscar(14, bst.raiz))
#print(bst.altura(bst.raiz))
#print(bst.min(bst.raiz))
#print(bst.max(bst.raiz))
#print(bst.num_hojas(bst.raiz))
#print(bst.hermanos(13,18,bst.raiz))
#print(bst.total_nodos(bst.raiz))
#print(bst.obtener_ancestro(14, bst.raiz))
#print(bst.verificar_bst(bst.raiz))
print(bst.nodo_k_distancia(8,2,bst.raiz))
