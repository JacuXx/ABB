"""
Script Principal - Menú Interactivo
====================================

Proporciona un menú interactivo para ejecutar las diferentes demos y ejemplos.
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(__file__))


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 70)
    print("🌳 ÁRBOL BINARIO DE BÚSQUEDA - MENÚ PRINCIPAL")
    print("=" * 70)
    print("\nElige una opción:")
    print("\n  1. 📚 Ejemplo Básico - Operaciones fundamentales del ABB")
    print("  2. 🔄 Comparación - Predecesor vs Sucesor")
    print("  3. 🎨 Visualizaciones - Diferentes formatos de visualización")
    print("  4. 🎯 Demo Completa - Ejercicio académico completo")
    print("  5. ❌ Salir")
    print("\n" + "=" * 70)


def ejecutar_opcion(opcion):
    """Ejecuta la opción seleccionada"""
    
    if opcion == '1':
        print("\n🚀 Ejecutando Ejemplo Básico...\n")
        from examples.ejemplo_basico import ejemplo_basico
        ejemplo_basico()
        
    elif opcion == '2':
        print("\n🚀 Ejecutando Comparación Predecesor vs Sucesor...\n")
        from examples.ejemplo_comparacion import comparar_estrategias
        comparar_estrategias()
        
    elif opcion == '3':
        print("\n🚀 Ejecutando Demo de Visualizaciones...\n")
        from examples.ejemplo_visualizaciones import demo_visualizaciones
        demo_visualizaciones()
        
    elif opcion == '4':
        print("\n🚀 Ejecutando Demo Completa del Ejercicio...\n")
        from examples.demo_completa import main
        main()
        
    elif opcion == '5':
        print("\n👋 ¡Hasta pronto!\n")
        return False
        
    else:
        print("\n⚠️  Opción no válida. Por favor, elige una opción del 1 al 5.")
    
    return True


def main():
    """Función principal del menú interactivo"""
    
    continuar = True
    
    while continuar:
        mostrar_menu()
        
        try:
            opcion = input("\nIngresa el número de tu opción: ").strip()
            continuar = ejecutar_opcion(opcion)
            
            if continuar and opcion in ['1', '2', '3', '4']:
                input("\n\n📍 Presiona ENTER para volver al menú principal...")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta pronto!\n")
            break
        except Exception as e:
            print(f"\n⚠️  Error: {e}")
            input("\n📍 Presiona ENTER para continuar...")


if __name__ == "__main__":
    main()
