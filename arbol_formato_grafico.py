class NodoGrafico:
    """Nodo para visualización gráfica del ABB"""
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolGrafico:
    """Árbol con visualización gráfica mejorada"""
    
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor):
        """Agrega un elemento al árbol"""
        if self.raiz is None:
            self.raiz = NodoGrafico(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)
    
    def _agregar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoGrafico(valor)
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoGrafico(valor)
            else:
                self._agregar_recursivo(nodo_actual.derecho, valor)
    
    def imprimir_arbol_bonito(self):
        """Imprime el árbol en formato similar a tu imagen"""
        if not self.raiz:
            print("Árbol vacío")
            return
        
        print("\n" + "="*60)
        print("🌳 ÁRBOL BINARIO DE BÚSQUEDA - FORMATO GRÁFICO 🌳")
        print("="*60)
        
        lineas = []
        self._construir_lineas(self.raiz, lineas, 0, 0, "C")
        
        # Ordenar por fila y luego por columna
        lineas.sort(key=lambda x: (x[1], x[2]))
        
        # Imprimir las líneas
        fila_actual = -1
        for valor, fila, col, pos in lineas:
            if fila != fila_actual:
                if fila_actual != -1:
                    print()
                fila_actual = fila
                print()  # Línea en blanco entre niveles
                espacios_necesarios = col
            else:
                espacios_necesarios = col - len(str(lineas[lineas.index((valor, fila, col, pos)) - 1][0])) - 3
            
            print(" " * max(0, espacios_necesarios), end="")
            print(f"({valor})", end="")
        
        print("\n")
    
    def _construir_lineas(self, nodo, lineas, fila, col_base, posicion):
        """Construye las líneas para imprimir"""
        if nodo is None:
            return col_base
        
        # Procesar hijo izquierdo
        if nodo.izquierdo:
            col_base = self._construir_lineas(nodo.izquierdo, lineas, fila + 1, col_base, "I")
        
        # Agregar nodo actual
        lineas.append((nodo.valor, fila, col_base, posicion))
        col_base += len(str(nodo.valor)) + 8  # Espaciado
        
        # Procesar hijo derecho
        if nodo.derecho:
            col_base = self._construir_lineas(nodo.derecho, lineas, fila + 1, col_base, "D")
        
        return col_base
    
    def dibujar_con_conexiones(self):
        """Dibuja el árbol con conexiones visuales"""
        if not self.raiz:
            print("Árbol vacío")
            return
        
        print("\n" + "🌳" * 20)
        print("ÁRBOL CON CONEXIONES VISUALES")
        print("🌳" * 20)
        
        self._imprimir_nivel([self.raiz], 1, self._calcular_altura(self.raiz))
    
    def _imprimir_nivel(self, nodos, nivel, altura_max):
        """Imprime un nivel del árbol con conexiones"""
        if not any(nodos) or nivel > altura_max:
            return
        
        # Calcular espaciado basado en el nivel
        espacios_entre = 2 ** (altura_max - nivel + 2)
        espacios_iniciales = 2 ** (altura_max - nivel + 1) - 3
        
        # Imprimir espacios iniciales
        print(" " * espacios_iniciales, end="")
        
        # Imprimir nodos
        siguiente_nivel = []
        for i, nodo in enumerate(nodos):
            if nodo:
                # Formatear el nodo como círculo
                print(f"({nodo.valor})", end="")
                siguiente_nivel.extend([nodo.izquierdo, nodo.derecho])
            else:
                print("   ", end="")
                siguiente_nivel.extend([None, None])
            
            # Espacios entre nodos
            if i < len(nodos) - 1:
                print(" " * espacios_entre, end="")
        
        print()  # Nueva línea después del nivel
        
        # Dibujar conexiones si no es el último nivel
        if nivel < altura_max and any(siguiente_nivel):
            self._dibujar_conexiones_nivel(nodos, espacios_iniciales, espacios_entre)
        
        # Llamada recursiva para el siguiente nivel
        self._imprimir_nivel(siguiente_nivel, nivel + 1, altura_max)
    
    def _dibujar_conexiones_nivel(self, nodos, espacios_iniciales, espacios_entre):
        """Dibuja las conexiones entre niveles"""
        print(" " * (espacios_iniciales), end="")
        
        for i, nodo in enumerate(nodos):
            if nodo:
                # Dibujar conexiones
                izq = "/" if nodo.izquierdo else " "
                der = "\\" if nodo.derecho else " "
                print(f"{izq} {der}", end="")
            else:
                print("   ", end="")
            
            # Espacios entre grupos de conexiones
            if i < len(nodos) - 1:
                print(" " * espacios_entre, end="")
        
        print()  # Nueva línea
    
    def _calcular_altura(self, nodo):
        """Calcula la altura del árbol"""
        if nodo is None:
            return 0
        return 1 + max(self._calcular_altura(nodo.izquierdo), 
                      self._calcular_altura(nodo.derecho))
    
    def crear_imagen_texto(self):
        """Crea una representación en texto del árbol similar a tu imagen"""
        if not self.raiz:
            return
        
        print("\n" + "━" * 50)
        print("📊 REPRESENTACIÓN VISUAL TIPO DIAGRAMA")
        print("━" * 50)
        
        # Crear representación más visual
        self._imprimir_como_diagrama(self.raiz, "", True, True)
    
    def _imprimir_como_diagrama(self, nodo, prefijo, es_ultimo, es_raiz):
        """Imprime el nodo como un diagrama con líneas"""
        if nodo is None:
            return
        
        if es_raiz:
            print(f"       ┌─── ({nodo.valor}) ───┐")
        else:
            conector = "└─── " if es_ultimo else "├─── "
            print(f"{prefijo}{conector}({nodo.valor})")
        
        # Preparar prefijos para los hijos
        if not es_raiz:
            nuevo_prefijo = prefijo + ("     " if es_ultimo else "│    ")
        else:
            nuevo_prefijo = "       "
        
        # Contar hijos no nulos
        hijos = [nodo.izquierdo, nodo.derecho]
        hijos_no_nulos = [h for h in hijos if h is not None]
        
        # Imprimir hijos
        if hijos_no_nulos:
            if nodo.izquierdo:
                es_ultimo_hijo = len(hijos_no_nulos) == 1
                self._imprimir_como_diagrama(nodo.izquierdo, nuevo_prefijo, es_ultimo_hijo, False)
            
            if nodo.derecho:
                self._imprimir_como_diagrama(nodo.derecho, nuevo_prefijo, True, False)

def main():
    """Demostración de las visualizaciones"""
    
    # Árbol con los datos del ejercicio
    print("🚀 CREANDO ÁRBOL CON LOS DATOS DEL EJERCICIO")
    arbol = ArbolGrafico()
    
    # Datos del ejercicio
    datos = [51, 52, 63, 14, 18, 11, 25, 56, 40, 22, 87, 27, 12, 99]
    
    for valor in datos:
        arbol.agregar(valor)
    
    # Diferentes tipos de visualización
    arbol.dibujar_con_conexiones()
    arbol.crear_imagen_texto()
    
    # Crear un árbol más simple para demostrar mejor el formato
    print("\n\n🎯 EJEMPLO SIMPLIFICADO (similar a tu imagen):")
    arbol_simple = ArbolGrafico()
    
    # Datos más simples para mejor visualización
    datos_simples = [7, 3, 11, 1, 5, 9, 13, 2, 4, 6, 8, 10, 12, 14]
    
    for valor in datos_simples:
        arbol_simple.agregar(valor)
    
    arbol_simple.dibujar_con_conexiones()
    arbol_simple.crear_imagen_texto()

if __name__ == "__main__":
    main()