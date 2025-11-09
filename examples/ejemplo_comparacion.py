"""
Ejemplo 2: Comparación Predecesor vs Sucesor
=============================================

Demuestra la diferencia entre usar predecesor y sucesor inorden
para eliminar nodos con dos hijos.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.arbol_abb import ArbolBinarioBusqueda
from src.core.abb_sucesor import ABBConSucesor


def comparar_estrategias():
    """Compara las dos estrategias de eliminación"""
    
    print("=" * 70)
    print("EJEMPLO 2: COMPARACIÓN PREDECESOR vs SUCESOR")
    print("=" * 70)
    
    datos = [50, 30, 70, 20, 40, 60, 80, 15, 25, 35, 45]
    
    # Árbol con predecesor
    print("\n🔵 ÁRBOL CON PREDECESOR INORDEN")
    print("-" * 70)
    
    abb_pred = ArbolBinarioBusqueda()
    for valor in datos:
        abb_pred.agregar(valor)
    
    print("\nÁrbol original:")
    abb_pred.mostrar_arbol()
    print(f"\nInorden: {abb_pred.recorrido_inorden()}")
    
    print("\n➤ Eliminando nodo 30 (con 2 hijos) usando PREDECESOR:")
    abb_pred.eliminar(30)
    
    print("\nÁrbol después de eliminar:")
    abb_pred.mostrar_arbol()
    print(f"\nInorden: {abb_pred.recorrido_inorden()}")
    
    # Árbol con sucesor
    print("\n\n🟢 ÁRBOL CON SUCESOR INORDEN")
    print("-" * 70)
    
    abb_suc = ABBConSucesor()
    for valor in datos:
        abb_suc.agregar(valor)
    
    print("\nÁrbol original:")
    abb_suc.mostrar_arbol()
    print(f"\nInorden: {abb_suc.recorrido_inorden()}")
    
    print("\n➤ Eliminando nodo 30 (con 2 hijos) usando SUCESOR:")
    abb_suc.eliminar_con_sucesor(30)
    
    print("\nÁrbol después de eliminar:")
    abb_suc.mostrar_arbol()
    print(f"\nInorden: {abb_suc.recorrido_inorden()}")
    
    # Explicación
    print("\n" + "=" * 70)
    print("💡 EXPLICACIÓN:")
    print("=" * 70)
    print("""
    PREDECESOR: Reemplaza el nodo eliminado con el MÁXIMO del subárbol IZQUIERDO
    - En este caso: El nodo 30 se reemplazó con 25
    
    SUCESOR: Reemplaza el nodo eliminado con el MÍNIMO del subárbol DERECHO
    - En este caso: El nodo 30 se reemplazó con 35
    
    Ambos métodos mantienen las propiedades del ABB correctamente.
    """)


if __name__ == "__main__":
    comparar_estrategias()
