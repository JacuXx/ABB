class NodoABB:
    """Clase que representa un nodo del árbol binario de búsqueda"""
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ABBConSucesor:
    """Versión del ABB que usa sucesor inorden para eliminación con 2 hijos"""
    
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor):
        """Agrega un elemento al árbol"""
        if self.raiz is None:
            self.raiz = NodoABB(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)
    
    def _agregar_recursivo(self, nodo_actual, valor):
        """Método auxiliar recursivo para agregar elementos"""
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoABB(valor)
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoABB(valor)
            else:
                self._agregar_recursivo(nodo_actual.derecho, valor)
    
    def eliminar_con_sucesor(self, valor):
        """Elimina un elemento usando sucesor inorden para nodos con 2 hijos"""
        self.raiz = self._eliminar_sucesor_recursivo(self.raiz, valor)
    
    def _eliminar_sucesor_recursivo(self, nodo_actual, valor):
        """Método auxiliar que usa sucesor inorden"""
        if nodo_actual is None:
            print(f"El valor {valor} no se encuentra en el árbol")
            return nodo_actual
        
        if valor < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar_sucesor_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar_sucesor_recursivo(nodo_actual.derecho, valor)
        else:
            print(f"Eliminando nodo: {valor}")
            
            # Caso 1: Nodo sin hijos
            if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
                print(f"  - Tipo: Nodo hoja (sin hijos)")
                return None
            
            # Caso 2: Nodo con un hijo
            elif nodo_actual.izquierdo is None:
                print(f"  - Tipo: Nodo con un hijo derecho")
                return nodo_actual.derecho
            elif nodo_actual.derecho is None:
                print(f"  - Tipo: Nodo con un hijo izquierdo")
                return nodo_actual.izquierdo
            
            # Caso 3: Nodo con dos hijos - USANDO SUCESOR
            else:
                print(f"  - Tipo: Nodo con dos hijos")
                print(f"  - Usando sucesor inorden")
                sucesor = self._encontrar_minimo(nodo_actual.derecho)
                nodo_actual.valor = sucesor.valor
                nodo_actual.derecho = self._eliminar_sucesor_recursivo(nodo_actual.derecho, sucesor.valor)
        
        return nodo_actual
    
    def _encontrar_minimo(self, nodo):
        """Encuentra el nodo con el valor mínimo en un subárbol"""
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo
    
    def recorrido_inorden(self):
        """Realiza un recorrido inorden"""
        elementos = []
        self._recorrido_inorden_recursivo(self.raiz, elementos)
        return elementos
    
    def _recorrido_inorden_recursivo(self, nodo_actual, elementos):
        """Método auxiliar recursivo para el recorrido inorden"""
        if nodo_actual is not None:
            self._recorrido_inorden_recursivo(nodo_actual.izquierdo, elementos)
            elementos.append(nodo_actual.valor)
            self._recorrido_inorden_recursivo(nodo_actual.derecho, elementos)
    
    def mostrar_arbol(self, nodo=None, nivel=0, prefijo="Raíz: "):
        """Muestra la estructura visual del árbol"""
        if nodo is None:
            nodo = self.raiz
        
        if nodo is not None:
            print(" " * (nivel * 4) + prefijo + str(nodo.valor))
            if nodo.izquierdo is not None or nodo.derecho is not None:
                if nodo.izquierdo is not None:
                    self.mostrar_arbol(nodo.izquierdo, nivel + 1, "├── I: ")
                else:
                    print(" " * ((nivel + 1) * 4) + "├── I: None")
                
                if nodo.derecho is not None:
                    self.mostrar_arbol(nodo.derecho, nivel + 1, "└── D: ")
                else:
                    print(" " * ((nivel + 1) * 4) + "└── D: None")

def demo_comparacion():
    """Demuestra la diferencia entre predecesor y sucesor"""
    print("=== COMPARACIÓN: PREDECESOR vs SUCESOR ===")
    
    # Datos del ejercicio
    datos = [51, 52, 63, 14, 18, 11, 25, 56, 40, 22, 87, 27, 12, 99]
    
    # Crear árbol con sucesor
    abb_sucesor = ABBConSucesor()
    for valor in datos:
        abb_sucesor.agregar(valor)
    
    print("\nÁrbol original:")
    abb_sucesor.mostrar_arbol()
    print(f"Inorden original: {abb_sucesor.recorrido_inorden()}")
    
    print(f"\nEliminando nodo 14 (con 2 hijos) usando SUCESOR INORDEN:")
    abb_sucesor.eliminar_con_sucesor(14)
    
    print(f"\nÁrbol después de eliminar con sucesor:")
    abb_sucesor.mostrar_arbol()
    print(f"Inorden final: {abb_sucesor.recorrido_inorden()}")

if __name__ == "__main__":
    demo_comparacion()