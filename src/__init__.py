"""
Árbol Binario de Búsqueda (ABB) - Paquete Principal
====================================================

Este paquete contiene implementaciones de Árboles Binarios de Búsqueda
con diferentes estrategias de eliminación y visualización.
"""

__version__ = "1.0.0"
__author__ = "Proyecto ABB"

from .core.arbol_abb import ArbolBinarioBusqueda, Nodo
from .core.abb_sucesor import ABBConSucesor, NodoABB

__all__ = [
    'ArbolBinarioBusqueda',
    'Nodo',
    'ABBConSucesor',
    'NodoABB'
]
