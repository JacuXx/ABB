import math
from collections import deque

class NodoVisual:
    """Clase para el nodo del árbol con visualización mejorada"""
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class VisualizadorABB:
    """Clase para crear visualizaciones gráficas del ABB"""
    
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor):
        """Agrega un elemento al árbol"""
        if self.raiz is None:
            self.raiz = NodoVisual(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)
    
    def _agregar_recursivo(self, nodo_actual, valor):
        """Método auxiliar recursivo para agregar elementos"""
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoVisual(valor)
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoVisual(valor)
            else:
                self._agregar_recursivo(nodo_actual.derecho, valor)
    
    def dibujar_arbol_grafico(self):
        """Dibuja el árbol en formato gráfico como el ejemplo"""
        if not self.raiz:
            print("Árbol vacío")
            return
        
        # Calcular la altura del árbol
        altura = self._calcular_altura(self.raiz)
        
        # Crear matriz para dibujar
        ancho = 2 ** (altura + 1) - 1
        alto = altura * 4 + 1
        matriz = [[' ' for _ in range(ancho)] for _ in range(alto)]
        
        # Llenar la matriz con el árbol
        self._llenar_matriz(matriz, self.raiz, 0, 0, ancho - 1)
        
        # Imprimir la matriz
        for fila in matriz:
            print(''.join(fila))
    
    def _calcular_altura(self, nodo):
        """Calcula la altura del árbol"""
        if nodo is None:
            return 0
        return 1 + max(self._calcular_altura(nodo.izquierdo), 
                      self._calcular_altura(nodo.derecho))
    
    def _llenar_matriz(self, matriz, nodo, fila, col_min, col_max):
        """Llena la matriz con los nodos y conexiones"""
        if nodo is None:
            return
        
        # Calcular posición del nodo
        col_medio = (col_min + col_max) // 2
        
        # Colocar el valor del nodo (centrado en un círculo)
        valor_str = str(nodo.valor)
        inicio = col_medio - len(valor_str) // 2
        
        # Dibujar círculo alrededor del número
        if col_medio > 0 and col_medio < len(matriz[0]) - 1:
            matriz[fila][col_medio - 1] = '('
            for i, char in enumerate(valor_str):
                matriz[fila][inicio + i] = char
            matriz[fila][col_medio + len(valor_str) // 2] = ')'
        
        # Dibujar conexiones a hijos
        if nodo.izquierdo or nodo.derecho:
            fila_conexion = fila + 1
            fila_hijo = fila + 2
            
            # Hijo izquierdo
            if nodo.izquierdo:
                col_hijo_izq = (col_min + col_medio) // 2
                # Línea diagonal hacia abajo-izquierda
                if col_hijo_izq < col_medio and fila_conexion < len(matriz):
                    for c in range(col_hijo_izq, col_medio):
                        if c < len(matriz[0]):
                            matriz[fila_conexion][c] = '_'
                    if col_hijo_izq < len(matriz[0]):
                        matriz[fila_conexion][col_hijo_izq] = '/'
                
                self._llenar_matriz(matriz, nodo.izquierdo, fila_hijo, col_min, col_medio - 1)
            
            # Hijo derecho
            if nodo.derecho:
                col_hijo_der = (col_medio + col_max) // 2
                # Línea diagonal hacia abajo-derecha
                if col_medio < col_hijo_der and fila_conexion < len(matriz):
                    for c in range(col_medio + 1, col_hijo_der + 1):
                        if c < len(matriz[0]):
                            matriz[fila_conexion][c] = '_'
                    if col_hijo_der < len(matriz[0]):
                        matriz[fila_conexion][col_hijo_der] = '\\'
                
                self._llenar_matriz(matriz, nodo.derecho, fila_hijo, col_medio + 1, col_max)
    
    def dibujar_arbol_simple(self):
        """Dibuja el árbol con formato de nodos conectados"""
        if not self.raiz:
            print("Árbol vacío")
            return
        
        print("\n" + "="*50)
        print("VISUALIZACIÓN GRÁFICA DEL ÁRBOL")
        print("="*50)
        
        # Obtener estructura por niveles
        niveles = self._obtener_niveles()
        
        for i, nivel in enumerate(niveles):
            # Calcular espaciado
            espacios_entre_nodos = 2 ** (len(niveles) - i + 1)
            espacios_iniciales = 2 ** (len(niveles) - i) - 1
            
            # Imprimir espacios iniciales
            print(" " * espacios_iniciales, end="")
            
            # Imprimir nodos del nivel
            for j, nodo in enumerate(nivel):
                if nodo is None:
                    print("   ", end="")
                else:
                    # Formatear número en círculo
                    valor_str = f"({nodo.valor})"
                    print(f"{valor_str:^4}", end="")
                
                # Espacios entre nodos (excepto el último)
                if j < len(nivel) - 1:
                    print(" " * espacios_entre_nodos, end="")
            
            print()  # Nueva línea
            
            # Dibujar conexiones (excepto en el último nivel)
            if i < len(niveles) - 1:
                self._dibujar_conexiones(niveles[i], espacios_iniciales, espacios_entre_nodos)
    
    def _obtener_niveles(self):
        """Obtiene los nodos organizados por niveles"""
        if not self.raiz:
            return []
        
        niveles = []
        cola = deque([self.raiz])
        
        while cola:
            nivel_actual = []
            nivel_size = len(cola)
            
            for _ in range(nivel_size):
                nodo = cola.popleft()
                nivel_actual.append(nodo)
                
                if nodo:
                    cola.append(nodo.izquierdo)
                    cola.append(nodo.derecho)
                else:
                    cola.append(None)
                    cola.append(None)
            
            # Verificar si hay nodos no nulos en este nivel
            if any(nodo is not None for nodo in nivel_actual):
                niveles.append(nivel_actual)
            else:
                break
        
        return niveles
    
    def _dibujar_conexiones(self, nivel, espacios_iniciales, espacios_entre_nodos):
        """Dibuja las líneas de conexión entre niveles"""
        print(" " * (espacios_iniciales - 1), end="")
        
        for i, nodo in enumerate(nivel):
            if nodo:
                # Dibujar conexiones a hijos
                if nodo.izquierdo or nodo.derecho:
                    if nodo.izquierdo:
                        print("/", end="")
                    else:
                        print(" ", end="")
                    
                    print(" ", end="")
                    
                    if nodo.derecho:
                        print("\\", end="")
                    else:
                        print(" ", end="")
                else:
                    print("   ", end="")
            else:
                print("   ", end="")
            
            # Espacios entre grupos de conexiones
            if i < len(nivel) - 1:
                print(" " * espacios_entre_nodos, end="")
        
        print()  # Nueva línea

def main():
    """Función principal para demostrar la visualización"""
    
    # Crear árbol con los datos del ejercicio
    abb = VisualizadorABB()
    
    # Datos iniciales
    datos_iniciales = [51, 52, 63, 14, 18, 11, 25, 56, 40, 22, 87]
    print("CREANDO ÁRBOL ABB CON VISUALIZACIÓN GRÁFICA")
    print("=" * 50)
    print(f"Datos iniciales: {datos_iniciales}")
    
    for valor in datos_iniciales:
        abb.agregar(valor)
    
    print(f"\nAgregando elementos: 27, 12, 99")
    abb.agregar(27)
    abb.agregar(12)
    abb.agregar(99)
    
    # Mostrar visualización simple
    abb.dibujar_arbol_simple()
    
    print("\n" + "="*50)
    print("EJEMPLO DE ÁRBOL SIMILAR A TU IMAGEN:")
    print("="*50)
    
    # Crear un árbol más pequeño similar al ejemplo
    abb_ejemplo = VisualizadorABB()
    datos_ejemplo = [2, 7, 5, 2, 6, 9, 5, 11, 4]  # Valores del ejemplo de tu imagen
    
    # Nota: ajustamos algunos valores para evitar duplicados
    datos_ejemplo = [7, 2, 5, 6, 9, 11, 4]
    
    for valor in datos_ejemplo:
        abb_ejemplo.agregar(valor)
    
    abb_ejemplo.dibujar_arbol_simple()

if __name__ == "__main__":
    main()