class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        # CREAR (inicializa lista vacía)
        self.cabeza = None


    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    # RECORRER
    def recorrer(self):
        elementos = []

        if self.cabeza is None:
            return elementos

        actual = self.cabeza
        while True:
            elementos.append(actual.dato)
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        return elementos

    # BUSCAR
    def buscar(self, dato):
        if self.cabeza is None:
            return False

        actual = self.cabeza
        while True:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        return False

    # ELIMINAR
    def eliminar(self, dato):
        if self.cabeza is None:
            return False

        actual = self.cabeza
        anterior = None

        # Caso especial: eliminar la cabeza
        if actual.dato == dato:
            if actual.siguiente == self.cabeza:
                # Solo un nodo
                self.cabeza = None
                return True
            else:
                # Más de un nodo
                ultimo = self.cabeza
                while ultimo.siguiente != self.cabeza:
                    ultimo = ultimo.siguiente
                self.cabeza = actual.siguiente
                ultimo.siguiente = self.cabeza
                return True

    
        anterior = actual
        actual = actual.siguiente

        while actual != self.cabeza:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente

        return False


if __name__ == "__main__":
    lista = ListaCircular()

    # Crear y agregar elementos
    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)

    print("Lista:", lista.recorrer())

    # Buscar
    print("¿Existe 20?", lista.buscar(20))

    # Eliminar
    lista.eliminar(20)

    print("Lista después de eliminar 20:", lista.recorrer())
