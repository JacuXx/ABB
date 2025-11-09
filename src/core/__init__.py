"""
Módulo Core - Implementaciones principales del ABB
===================================================

Contiene las clases base del Árbol Binario de Búsqueda con diferentes
estrategias de eliminación.
"""

from .arbol_abb import ArbolBinarioBusqueda, Nodo
from .abb_sucesor import ABBConSucesor, NodoABB

__all__ = [
    'ArbolBinarioBusqueda',
    'Nodo',
    'ABBConSucesor',
    'NodoABB'
]
