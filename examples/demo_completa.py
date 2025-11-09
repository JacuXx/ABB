"""
Demo Completa del Ejercicio ABB
================================

Implementación completa del ejercicio de Árbol Binario de Búsqueda
con todos los pasos requeridos.
"""

import sys
import os

# Agregar el directorio padre al path para importar los módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class NodoEjercicio:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolEjercicio:
    def __init__(self):
        self.raiz = None
    
    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = NodoEjercicio(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)
    
    def _agregar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoEjercicio(valor)
            else:
                self._agregar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoEjercicio(valor)
            else:
                self._agregar_recursivo(nodo.derecho, valor)
    
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)
    
    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            # Nodo encontrado
            if nodo.izquierdo is None and nodo.derecho is None:
                print(f"✅ Eliminando {valor} - NODO SIN HIJOS")
                return None
            elif nodo.izquierdo is None:
                print(f"✅ Eliminando {valor} - NODO CON 1 HIJO (derecho)")
                return nodo.derecho
            elif nodo.derecho is None:
                print(f"✅ Eliminando {valor} - NODO CON 1 HIJO (izquierdo)")
                return nodo.izquierdo
            else:
                print(f"✅ Eliminando {valor} - NODO CON 2 HIJOS (usando predecesor)")
                predecesor = self._encontrar_maximo(nodo.izquierdo)
                nodo.valor = predecesor.valor
                nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, predecesor.valor)
        
        return nodo
    
    def _encontrar_maximo(self, nodo):
        while nodo.derecho is not None:
            nodo = nodo.derecho
        return nodo
    
    def mostrar_arbol_visual(self):
        """ÚNICA visualización - formato con círculos"""
        if not self.raiz:
            print("Árbol vacío")
            return
        
        print("\n" + "═" * 60)
        print("🌳 ÁRBOL BINARIO DE BÚSQUEDA - RESULTADO FINAL")
        print("═" * 60)
        
        self._imprimir_con_conexiones(self.raiz, "", True)
        
        print("\n" + "═" * 60)
    
    def _imprimir_con_conexiones(self, nodo, prefijo, es_ultimo):
        if nodo is None:
            return
        
        conector = "└── " if es_ultimo else "├── "
        print(f"{prefijo}{conector}⭕ {nodo.valor}")
        
        extension = "    " if es_ultimo else "│   "
        nuevo_prefijo = prefijo + extension
        
        hijos = []
        if nodo.izquierdo:
            hijos.append(nodo.izquierdo)
        if nodo.derecho:
            hijos.append(nodo.derecho)
        
        for i, hijo in enumerate(hijos):
            es_ultimo_hijo = (i == len(hijos) - 1)
            self._imprimir_con_conexiones(hijo, nuevo_prefijo, es_ultimo_hijo)

def main():
    """RESULTADO FINAL DEL EJERCICIO"""
    
    print("🎯 EJERCICIO ÁRBOL BINARIO DE BÚSQUEDA")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # PASO 1: Crear árbol con datos iniciales
    arbol = ArbolEjercicio()
    datos_iniciales = [51, 52, 63, 14, 18, 11, 25, 56, 40, 22, 87]
    
    print(f"📝 Datos iniciales: {datos_iniciales}")
    
    for valor in datos_iniciales:
        arbol.agregar(valor)
    
    print("\n🔸 ÁRBOL INICIAL:")
    arbol.mostrar_arbol_visual()
    
    # PASO 2: Agregar nuevos elementos
    print("➕ Agregando elementos: 27, 12, 99")
    arbol.agregar(27)
    arbol.agregar(12)
    arbol.agregar(99)
    
    print("\n🔸 ÁRBOL DESPUÉS DE AGREGAR 27, 12, 99:")
    arbol.mostrar_arbol_visual()
    
    # PASO 3: Eliminar 3 nodos (uno de cada tipo)
    print("🗑️  ELIMINANDO 3 NODOS:")
    print("──────────────────────")
    
    # Eliminar nodo sin hijos (hoja)
    arbol.eliminar(12)
    
    # Eliminar nodo con 1 hijo
    arbol.eliminar(18)
    
    # Eliminar nodo with 2 hijos
    arbol.eliminar(14)
    
    print("\n🏆 ÁRBOL FINAL (después de todas las eliminaciones):")
    arbol.mostrar_arbol_visual()
    
    print("✅ EJERCICIO COMPLETADO")
    print("━━━━━━━━━━━━━━━━━━━━━━━━")

if __name__ == "__main__":
    main()
