class NodoCirculo:
    """Nodo para representación con círculos"""
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolCirculos:
    """Árbol que se dibuja con círculos y líneas como en tu imagen"""
    
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = NodoCirculo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)
    
    def _agregar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoCirculo(valor)
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoCirculo(valor)
            else:
                self._agregar_recursivo(nodo_actual.derecho, valor)
    
    def dibujar_como_imagen(self):
        """Dibuja el árbol exactamente como en tu imagen con círculos"""
        if not self.raiz:
            print("Árbol vacío")
            return
        
        print("\n" + "●" * 60)
        print("🎯 ÁRBOL CON FORMATO DE CÍRCULOS (Como tu imagen)")
        print("●" * 60)
        
        # Calcular posiciones de los nodos
        posiciones = {}
        self._calcular_posiciones(self.raiz, posiciones, 40, 0, 80)
        
        # Crear matriz para dibujar
        max_fila = max(pos[1] for pos in posiciones.values()) + 1
        max_col = max(pos[0] for pos in posiciones.values()) + 5
        
        # Crear matriz de caracteres
        matriz = [[' ' for _ in range(max_col)] for _ in range(max_fila * 3)]
        
        # Dibujar conexiones primero
        self._dibujar_conexiones(self.raiz, posiciones, matriz)
        
        # Dibujar nodos después (para que estén encima de las líneas)
        for nodo_valor, (col, fila) in posiciones.items():
            fila_matriz = fila * 3
            # Dibujar círculo
            valor_str = str(nodo_valor)
            
            # Círculo simple
            if col > 1 and col < max_col - 3:
                matriz[fila_matriz][col-1] = '┌'
                matriz[fila_matriz][col] = '─'
                matriz[fila_matriz][col+1] = '┐'
                
                matriz[fila_matriz+1][col-1] = '│'
                for i, char in enumerate(valor_str):
                    if col + i - len(valor_str)//2 >= 0:
                        matriz[fila_matriz+1][col + i - len(valor_str)//2] = char
                matriz[fila_matriz+1][col+1] = '│'
                
                matriz[fila_matriz+2][col-1] = '└'
                matriz[fila_matriz+2][col] = '─'
                matriz[fila_matriz+2][col+1] = '┘'
        
        # Imprimir matriz
        for fila in matriz:
            print(''.join(fila).rstrip())
    
    def _calcular_posiciones(self, nodo, posiciones, col, fila, ancho):
        """Calcula las posiciones de cada nodo"""
        if nodo is None:
            return
        
        posiciones[nodo.valor] = (col, fila)
        
        nuevo_ancho = ancho // 2
        if nodo.izquierdo:
            self._calcular_posiciones(nodo.izquierdo, posiciones, 
                                    col - nuevo_ancho//2, fila + 1, nuevo_ancho)
        if nodo.derecho:
            self._calcular_posiciones(nodo.derecho, posiciones, 
                                    col + nuevo_ancho//2, fila + 1, nuevo_ancho)
    
    def _dibujar_conexiones(self, nodo, posiciones, matriz):
        """Dibuja las líneas de conexión entre nodos"""
        if nodo is None:
            return
        
        col_padre, fila_padre = posiciones[nodo.valor]
        fila_padre_matriz = fila_padre * 3 + 2  # Parte inferior del círculo padre
        
        # Conexión al hijo izquierdo
        if nodo.izquierdo:
            col_hijo, fila_hijo = posiciones[nodo.izquierdo.valor]
            fila_hijo_matriz = fila_hijo * 3  # Parte superior del círculo hijo
            
            # Dibujar línea diagonal
            self._dibujar_linea_diagonal(matriz, col_padre, fila_padre_matriz, 
                                       col_hijo, fila_hijo_matriz, True)
        
        # Conexión al hijo derecho
        if nodo.derecho:
            col_hijo, fila_hijo = posiciones[nodo.derecho.valor]
            fila_hijo_matriz = fila_hijo * 3
            
            # Dibujar línea diagonal
            self._dibujar_linea_diagonal(matriz, col_padre, fila_padre_matriz, 
                                       col_hijo, fila_hijo_matriz, False)
        
        # Recursión
        self._dibujar_conexiones(nodo.izquierdo, posiciones, matriz)
        self._dibujar_conexiones(nodo.derecho, posiciones, matriz)
    
    def _dibujar_linea_diagonal(self, matriz, x1, y1, x2, y2, es_izquierdo):
        """Dibuja una línea diagonal entre dos puntos"""
        if y2 <= y1:
            return
        
        # Línea simple
        pasos = max(abs(x2 - x1), abs(y2 - y1))
        if pasos == 0:
            return
        
        for i in range(1, pasos):
            x = x1 + (x2 - x1) * i // pasos
            y = y1 + (y2 - y1) * i // pasos
            
            if 0 <= y < len(matriz) and 0 <= x < len(matriz[0]):
                if es_izquierdo:
                    matriz[y][x] = '/'
                else:
                    matriz[y][x] = '\\'
    
    def dibujar_estilo_simple(self):
        """Versión más simple pero clara del árbol"""
        print("\n" + "◆" * 50)
        print("🌟 VISUALIZACIÓN SIMPLE Y CLARA")
        print("◆" * 50)
        
        self._imprimir_simple(self.raiz, "", True)
    
    def _imprimir_simple(self, nodo, prefijo, es_ultimo):
        """Imprime de forma simple con estructura clara"""
        if nodo is None:
            return
        
        # Símbolo del conector
        conector = "└── " if es_ultimo else "├── "
        print(f"{prefijo}{conector}● {nodo.valor}")
        
        # Nuevo prefijo para los hijos
        extension = "    " if es_ultimo else "│   "
        nuevo_prefijo = prefijo + extension
        
        # Imprimir hijos (primero izquierdo, luego derecho)
        hijos = []
        if nodo.izquierdo:
            hijos.append(('izq', nodo.izquierdo))
        if nodo.derecho:
            hijos.append(('der', nodo.derecho))
        
        for i, (tipo, hijo) in enumerate(hijos):
            es_ultimo_hijo = (i == len(hijos) - 1)
            self._imprimir_simple(hijo, nuevo_prefijo, es_ultimo_hijo)

def crear_arbol_ejercicio():
    """Crea el árbol con los datos del ejercicio"""
    arbol = ArbolCirculos()
    
    print("📋 DATOS DEL EJERCICIO:")
    print("Iniciales: 51, 52, 63, 14, 18, 11, 25, 56, 40, 22, 87")
    print("Agregamos: 27, 12, 99")
    print()
    
    # Datos iniciales
    datos = [51, 52, 63, 14, 18, 11, 25, 56, 40, 22, 87]
    for valor in datos:
        arbol.agregar(valor)
    
    # Elementos adicionales
    arbol.agregar(27)
    arbol.agregar(12)
    arbol.agregar(99)
    
    return arbol

def crear_arbol_ejemplo():
    """Crea un árbol similar al de tu imagen para comparar"""
    arbol = ArbolCirculos()
    
    # Intentar recrear algo similar a tu imagen
    # En tu imagen veo: raíz=2, hijos=7,5, etc.
    datos = [7, 2, 9, 6, 11, 5, 4]  # Ajustado para evitar duplicados
    
    for valor in datos:
        arbol.agregar(valor)
    
    return arbol

def main():
    """Función principal"""
    
    # Árbol del ejercicio
    print("🚀 ÁRBOL DEL EJERCICIO COMPLETO")
    print("=" * 50)
    
    arbol_ejercicio = crear_arbol_ejercicio()
    arbol_ejercicio.dibujar_estilo_simple()
    arbol_ejercicio.dibujar_como_imagen()
    
    # Ejemplo más simple
    print("\n\n🎯 EJEMPLO SIMPLIFICADO")
    print("=" * 50)
    
    arbol_ejemplo = crear_arbol_ejemplo()
    arbol_ejemplo.dibujar_estilo_simple()
    arbol_ejemplo.dibujar_como_imagen()
    
    print("\n✅ EXPLICACIÓN:")
    print("● Cada número está representado dentro de un círculo/nodo")
    print("● Las líneas conectan padres con hijos")
    print("● Hijo izquierdo < Padre < Hijo derecho")
    print("● Formato similar al de tu imagen de referencia")

if __name__ == "__main__":
    main()