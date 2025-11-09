"""
Ejemplo 3: Visualizaciones del ABB
===================================

Demuestra las diferentes formas de visualizar el árbol.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.visualization.visualizador_basico import VisualizadorABB
from src.visualization.visualizador_grafico import ArbolGrafico
from src.visualization.visualizador_circulos import ArbolCirculos


def demo_visualizaciones():
    """Demuestra diferentes tipos de visualización"""
    
    print("=" * 70)
    print("EJEMPLO 3: DIFERENTES VISUALIZACIONES DEL ABB")
    print("=" * 70)
    
    datos = [50, 30, 70, 20, 40, 60, 80, 15, 25]
    
    # Visualización básica
    print("\n\n📊 1. VISUALIZACIÓN BÁSICA")
    print("-" * 70)
    
    vis_basico = VisualizadorABB()
    for valor in datos:
        vis_basico.agregar(valor)
    
    vis_basico.dibujar_arbol_simple()
    
    # Visualización gráfica
    print("\n\n🎨 2. VISUALIZACIÓN GRÁFICA CON CONEXIONES")
    print("-" * 70)
    
    vis_grafico = ArbolGrafico()
    for valor in datos:
        vis_grafico.agregar(valor)
    
    vis_grafico.dibujar_con_conexiones()
    vis_grafico.crear_imagen_texto()
    
    # Visualización con círculos
    print("\n\n⭕ 3. VISUALIZACIÓN CON CÍRCULOS")
    print("-" * 70)
    
    vis_circulos = ArbolCirculos()
    for valor in datos:
        vis_circulos.agregar(valor)
    
    vis_circulos.dibujar_estilo_simple()
    
    print("\n\n✅ Se han mostrado 3 tipos diferentes de visualización")
    print("   Puedes elegir la que más te guste para tus proyectos!")


if __name__ == "__main__":
    demo_visualizaciones()
