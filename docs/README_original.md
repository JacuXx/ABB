# Árbol Binario de Búsqueda (ABB) - Ejercicio Completo

Este proyecto implementa un **Árbol Binario de Búsqueda** en Python con todas las operaciones fundamentales.

## 📋 Datos del Ejercicio

- **Datos iniciales**: 51, 52, 63, 14, 18, 11, 25, 56, 40, 22, 87
- **Elementos a agregar**: 27, 12, 99
- **Eliminaciones a demostrar**:
  - Nodo sin hijos (hoja)
  - Nodo con 1 hijo
  - Nodo con 2 hijos (predecesor y sucesor)

## 📁 Archivos del Proyecto

1. **`arbol_abb.py`** - Implementación completa con predecesor inorden
2. **`abb_con_sucesor.py`** - Versión alternativa que usa sucesor inorden
3. **`visualizador_grafico.py`** - Visualización gráfica básica del árbol
4. **`arbol_formato_grafico.py`** - Visualización con múltiples formatos
5. **`arbol_circulos.py`** - ⭐ **Visualización con círculos como en tu imagen**

## 🌳 Características del ABB

### Operaciones Implementadas

- ✅ **Inserción** de elementos
- ✅ **Búsqueda** de elementos
- ✅ **Eliminación** con los 3 casos:
  - Nodo hoja (sin hijos)
  - Nodo con un hijo
  - Nodo con dos hijos
- ✅ **Recorrido inorden** (muestra elementos ordenados)
- ✅ **Visualización** de la estructura del árbol

### Visualización Gráfica 🎨

- ✅ **Formato de árbol tradicional** (texto estructurado)
- ✅ **Formato con círculos y líneas** (similar a diagramas)
- ✅ **Representación tipo diagrama** (con conectores Unicode)
- ✅ **Visualización por niveles** con conexiones

### Métodos de Eliminación para Nodos con 2 Hijos

1. **Predecesor Inorden**: Máximo del subárbol izquierdo
2. **Sucesor Inorden**: Mínimo del subárbol derecho

## 🚀 Cómo Ejecutar

```bash
# Ejecutar implementación principal
python arbol_abb.py

# Ejecutar demostración con sucesor
python abb_con_sucesor.py

# 🎨 Visualizaciones gráficas
python visualizador_grafico.py       # Visualización básica
python arbol_formato_grafico.py      # Múltiples formatos
python arbol_circulos.py             # ⭐ Formato con círculos
```

## 📊 Resultado del Ejercicio

### Árbol Inicial (después de agregar 27, 12, 99)
```
Raíz: 51
    ├── I: 14
        ├── I: 11
            └── D: 12
        └── D: 18
            └── D: 25
                ├── I: 22
                └── D: 40
                    ├── I: 27
    └── D: 52
        └── D: 63
            ├── I: 56
            └── D: 87
                └── D: 99
```

### Eliminaciones Demostradas

1. **Nodo 12** (sin hijos): Se elimina directamente
2. **Nodo 18** (con 1 hijo): Se reemplaza por su hijo derecho (25)
3. **Nodo 14** (con 2 hijos): Se reemplaza por su predecesor (11)

## 🔍 Conceptos Clave

### Propiedades del ABB
- Todos los elementos del subárbol izquierdo < nodo actual
- Todos los elementos del subárbol derecho > nodo actual
- El recorrido inorden produce una secuencia ordenada

### Casos de Eliminación
1. **Nodo hoja**: `return None`
2. **Un hijo**: `return hijo_único`
3. **Dos hijos**: 
   - Encontrar predecesor o sucesor
   - Reemplazar valor
   - Eliminar el nodo predecesor/sucesor

## 💡 Ventajas de Cada Método

### Predecesor Inorden
- Mantiene más balanceado el subárbol izquierdo
- Útil cuando el subárbol derecho es más pesado

### Sucesor Inorden  
- Mantiene más balanceado el subárbol derecho
- Útil cuando el subárbol izquierdo es más pesado

## 🎯 Complejidad

- **Inserción**: O(log n) promedio, O(n) peor caso
- **Búsqueda**: O(log n) promedio, O(n) peor caso  
- **Eliminación**: O(log n) promedio, O(n) peor caso
- **Recorrido**: O(n)

*Nota: El peor caso O(n) ocurre cuando el árbol se degenera en una lista enlazada*