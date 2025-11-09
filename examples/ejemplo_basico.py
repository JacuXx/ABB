"""
Ejemplo 1: Uso Básico del ABB con Predecesor
=============================================

Demuestra las operaciones básicas del árbol binario de búsqueda
usando la estrategia de predecesor inorden para eliminación.
"""

import sys
import os

# Agregar el directorio padre al path para importar los módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.arbol_abb import ArbolBinarioBusqueda


def ejemplo_basico():
    """Demuestra el uso básico del ABB"""
    
    print("=" * 60)
    print("EJEMPLO 1: USO BÁSICO DEL ÁRBOL BINARIO DE BÚSQUEDA")
    print("=" * 60)
    
    # Crear el árbol
    abb = ArbolBinarioBusqueda()
    
    # Agregar elementos
    print("\n📝 Agregando elementos...")
    datos = [50, 30, 70, 20, 40, 60, 80]
    
    for valor in datos:
        abb.agregar(valor)
        print(f"  ✓ Agregado: {valor}")
    
    # Mostrar estructura
    print("\n🌳 Estructura del árbol:")
    abb.mostrar_arbol()
    
    # Recorrido inorden
    print(f"\n📊 Recorrido inorden (ordenado): {abb.recorrido_inorden()}")
    
    # Buscar elementos
    print("\n🔍 Buscando elementos:")
    elementos_buscar = [40, 100, 70]
    
    for valor in elementos_buscar:
        encontrado = abb.buscar(valor)
        estado = "✓ Encontrado" if encontrado else "✗ No encontrado"
        print(f"  {valor}: {estado}")
    
    # Eliminar un elemento
    print("\n🗑️  Eliminando elemento 30 (nodo con 2 hijos)...")
    abb.eliminar(30)
    
    print("\n🌳 Estructura después de eliminar:")
    abb.mostrar_arbol()
    
    print(f"\n📊 Recorrido inorden final: {abb.recorrido_inorden()}")


if __name__ == "__main__":
    ejemplo_basico()
