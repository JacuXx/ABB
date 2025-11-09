class Nodo:
    """Clase que representa un nodo del árbol binario de búsqueda"""
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    """Clase que implementa un Árbol Binario de Búsqueda (ABB)"""
    
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor):
        """Agrega un elemento al árbol"""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)
    
    def _agregar_recursivo(self, nodo_actual, valor):
        """Método auxiliar recursivo para agregar elementos"""
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(nodo_actual.derecho, valor)
        # Si el valor ya existe, no lo agregamos (evitamos duplicados)
    
    def buscar(self, valor):
        """Busca un elemento en el árbol"""
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo_actual, valor):
        """Método auxiliar recursivo para buscar elementos"""
        if nodo_actual is None:
            return False
        
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, valor)
    
    def eliminar(self, valor):
        """Elimina un elemento del árbol"""
        self.raiz = self._eliminar_recursivo(self.raiz, valor)
    
    def _eliminar_recursivo(self, nodo_actual, valor):
        """Método auxiliar recursivo para eliminar elementos"""
        # Caso base: el nodo no existe
        if nodo_actual is None:
            print(f"El valor {valor} no se encuentra en el árbol")
            return nodo_actual
        
        # Navegar hacia el nodo a eliminar
        if valor < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar_recursivo(nodo_actual.derecho, valor)
        else:
            # Nodo encontrado, proceder con la eliminación
            print(f"Eliminando nodo: {valor}")
            
            # Caso 1: Nodo sin hijos (hoja)
            if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
                print(f"  - Tipo: Nodo hoja (sin hijos)")
                return None
            
            # Caso 2: Nodo con un solo hijo
            elif nodo_actual.izquierdo is None:
                print(f"  - Tipo: Nodo con un hijo derecho")
                return nodo_actual.derecho
            elif nodo_actual.derecho is None:
                print(f"  - Tipo: Nodo con un hijo izquierdo")
                return nodo_actual.izquierdo
            
            # Caso 3: Nodo con dos hijos
            else:
                print(f"  - Tipo: Nodo con dos hijos")
                # Opción 1: Usar predecesor (máximo del subárbol izquierdo)
                print(f"  - Usando predecesor inorden")
                predecesor = self._encontrar_maximo(nodo_actual.izquierdo)
                nodo_actual.valor = predecesor.valor
                nodo_actual.izquierdo = self._eliminar_recursivo(nodo_actual.izquierdo, predecesor.valor)
        
        return nodo_actual
    
    def _encontrar_maximo(self, nodo):
        """Encuentra el nodo con el valor máximo en un subárbol"""
        while nodo.derecho is not None:
            nodo = nodo.derecho
        return nodo
    
    def _encontrar_minimo(self, nodo):
        """Encuentra el nodo con el valor mínimo en un subárbol"""
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo
    
    def recorrido_inorden(self):
        """Realiza un recorrido inorden (izquierda, raíz, derecha)"""
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

def main():
    # Crear el árbol ABB
    abb = ArbolBinarioBusqueda()
    
    # Datos iniciales del ejercicio
    datos_iniciales = [51, 52, 63, 14, 18, 11, 25, 56, 40, 22, 87]
    
    print("=== CREACIÓN DEL ÁRBOL BINARIO DE BÚSQUEDA ===")
    print(f"Datos iniciales: {datos_iniciales}")
    print("\nAgregando elementos al árbol...")
    
    for valor in datos_iniciales:
        abb.agregar(valor)
        print(f"Agregado: {valor}")
    
    print("\n=== ESTRUCTURA INICIAL DEL ÁRBOL ===")
    abb.mostrar_arbol()
    
    print(f"\nRecorrido inorden (ordenado): {abb.recorrido_inorden()}")
    
    # Agregar nuevos elementos
    print("\n=== AGREGANDO NUEVOS ELEMENTOS ===")
    nuevos_elementos = [27, 12, 99]
    
    for valor in nuevos_elementos:
        print(f"\nAgregando: {valor}")
        abb.agregar(valor)
    
    print("\n=== ÁRBOL DESPUÉS DE AGREGAR NUEVOS ELEMENTOS ===")
    abb.mostrar_arbol()
    print(f"\nRecorrido inorden actualizado: {abb.recorrido_inorden()}")
    
    # Demonstrar eliminaciones
    print("\n=== DEMONSTRACIÓN DE ELIMINACIONES ===")
    
    # 1. Eliminar nodo sin hijos (hoja)
    print("\n1. Eliminando nodo SIN HIJOS (hoja):")
    # Buscar una hoja en el árbol actual
    elementos_ordenados = abb.recorrido_inorden()
    print(f"Elementos actuales: {elementos_ordenados}")
    
    # Eliminar 12 (debería ser una hoja)
    abb.eliminar(12)
    
    print("\nÁrbol después de eliminar nodo hoja:")
    abb.mostrar_arbol()
    
    # 2. Eliminar nodo con 1 hijo
    print("\n2. Eliminando nodo CON 1 HIJO:")
    # Eliminar 18 (debería tener un hijo)
    abb.eliminar(18)
    
    print("\nÁrbol después de eliminar nodo con 1 hijo:")
    abb.mostrar_arbol()
    
    # 3. Eliminar nodo con 2 hijos
    print("\n3. Eliminando nodo CON 2 HIJOS:")
    # Eliminar 14 (debería tener dos hijos)
    abb.eliminar(14)
    
    print("\nÁrbol después de eliminar nodo con 2 hijos:")
    abb.mostrar_arbol()
    
    print(f"\nRecorrido final inorden: {abb.recorrido_inorden()}")
    
    # Información adicional sobre los métodos de eliminación
    print("\n=== INFORMACIÓN SOBRE MÉTODOS DE ELIMINACIÓN ===")
    print("1. Nodo sin hijos: Se elimina directamente")
    print("2. Nodo con 1 hijo: Se reemplaza por su único hijo")
    print("3. Nodo con 2 hijos: Se puede reemplazar por:")
    print("   - Predecesor inorden (máximo del subárbol izquierdo)")
    print("   - Sucesor inorden (mínimo del subárbol derecho)")
    print("   En este código se usa el predecesor inorden")

if __name__ == "__main__":
    main()