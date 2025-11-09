# Árbol Binario de Búsqueda (ABB) - Proyecto Completo

Un proyecto completo en Python que implementa Árboles Binarios de Búsqueda con múltiples estrategias de eliminación y opciones de visualización.

## 📁 Estructura del Proyecto

```
ABB/
│
├── src/                          # Código fuente principal
│   ├── __init__.py
│   ├── core/                     # Implementaciones core del ABB
│   │   ├── __init__.py
│   │   ├── arbol_abb.py         # ABB con predecesor inorden
│   │   └── abb_sucesor.py       # ABB con sucesor inorden
│   │
│   └── visualization/            # Módulos de visualización
│       ├── __init__.py
│       ├── visualizador_basico.py    # Visualización básica
│       ├── visualizador_grafico.py   # Visualización gráfica
│       └── visualizador_circulos.py  # Visualización con círculos
│
├── examples/                     # Ejemplos de uso
│   ├── demo_completa.py         # Demo completa del ejercicio
│   ├── ejemplo_basico.py        # Ejemplo de uso básico
│   ├── ejemplo_comparacion.py   # Comparación predecesor vs sucesor
│   └── ejemplo_visualizaciones.py # Demo de visualizaciones
│
├── docs/                         # Documentación
│   └── README_original.md       # README original del proyecto
│
└── README.md                     # Este archivo

```

## 🚀 Inicio Rápido

### Requisitos
- Python 3.7 o superior
- No requiere librerías externas

### Instalación

1. Clona o descarga este repositorio
2. No es necesario instalar dependencias adicionales

### Uso Básico

```python
# Importar la clase principal
from src.core.arbol_abb import ArbolBinarioBusqueda

# Crear un árbol
abb = ArbolBinarioBusqueda()

# Agregar elementos
datos = [50, 30, 70, 20, 40, 60, 80]
for valor in datos:
    abb.agregar(valor)

# Mostrar el árbol
abb.mostrar_arbol()

# Buscar un elemento
existe = abb.buscar(40)  # True

# Eliminar un elemento
abb.eliminar(30)

# Recorrido inorden (ordenado)
elementos = abb.recorrido_inorden()
print(elementos)
```

## 📚 Ejemplos Disponibles

### 1. Ejemplo Básico
Demuestra las operaciones fundamentales del ABB.

```bash
python examples/ejemplo_basico.py
```

### 2. Comparación Predecesor vs Sucesor
Muestra la diferencia entre las dos estrategias de eliminación para nodos con 2 hijos.

```bash
python examples/ejemplo_comparacion.py
```

### 3. Visualizaciones
Demuestra las diferentes formas de visualizar el árbol.

```bash
python examples/ejemplo_visualizaciones.py
```

### 4. Demo Completa del Ejercicio
Ejecuta la demostración completa del ejercicio académico.

```bash
python examples/demo_completa.py
```

## 🌳 Características Implementadas

### Operaciones del ABB

- ✅ **Inserción** - Agregar elementos manteniendo las propiedades del ABB
- ✅ **Búsqueda** - Encontrar elementos de forma eficiente
- ✅ **Eliminación** - Tres casos:
  - Nodo sin hijos (hoja)
  - Nodo con un hijo
  - Nodo con dos hijos (predecesor y sucesor)
- ✅ **Recorrido Inorden** - Obtener elementos ordenados

### Estrategias de Eliminación

1. **Predecesor Inorden** (`arbol_abb.py`)
   - Reemplaza el nodo con el máximo del subárbol izquierdo
   - Útil cuando el subárbol derecho es más pesado

2. **Sucesor Inorden** (`abb_sucesor.py`)
   - Reemplaza el nodo con el mínimo del subárbol derecho
   - Útil cuando el subárbol izquierdo es más pesado

### Visualizaciones

1. **Básica** - Formato simple con conectores ASCII
2. **Gráfica** - Formato con conexiones visuales mejoradas
3. **Círculos** - Estilo similar a diagramas con nodos circulares

## 📖 Documentación de las Clases

### `ArbolBinarioBusqueda`

**Clase principal del ABB con eliminación por predecesor**

#### Métodos principales:
- `agregar(valor)` - Agrega un elemento al árbol
- `buscar(valor)` - Busca un elemento (retorna True/False)
- `eliminar(valor)` - Elimina un elemento del árbol
- `recorrido_inorden()` - Retorna lista de elementos ordenados
- `mostrar_arbol()` - Muestra la estructura visual del árbol

### `ABBConSucesor`

**Versión alternativa que usa sucesor inorden**

#### Métodos principales:
- `agregar(valor)` - Agrega un elemento al árbol
- `eliminar_con_sucesor(valor)` - Elimina usando sucesor inorden
- `recorrido_inorden()` - Retorna lista de elementos ordenados
- `mostrar_arbol()` - Muestra la estructura visual del árbol

## 🎯 Complejidad Temporal

| Operación | Caso Promedio | Peor Caso |
|-----------|---------------|-----------|
| Inserción | O(log n)      | O(n)      |
| Búsqueda  | O(log n)      | O(n)      |
| Eliminación | O(log n)    | O(n)      |
| Recorrido | O(n)          | O(n)      |

*Nota: El peor caso O(n) ocurre cuando el árbol se degenera en una lista enlazada*

## 💡 Conceptos Clave

### Propiedades del ABB
- Todos los elementos del subárbol izquierdo < nodo actual
- Todos los elementos del subárbol derecho > nodo actual
- El recorrido inorden produce una secuencia ordenada

### Casos de Eliminación
1. **Nodo hoja**: Se elimina directamente
2. **Nodo con un hijo**: Se reemplaza por su único hijo
3. **Nodo con dos hijos**: Se reemplaza por el predecesor o sucesor inorden

## 🔧 Personalización

Puedes extender las clases para agregar funcionalidades adicionales:

```python
from src.core.arbol_abb import ArbolBinarioBusqueda

class MiABBPersonalizado(ArbolBinarioBusqueda):
    def contar_nodos(self):
        """Cuenta el número total de nodos"""
        return len(self.recorrido_inorden())
    
    def encontrar_minimo(self):
        """Encuentra el valor mínimo del árbol"""
        elementos = self.recorrido_inorden()
        return elementos[0] if elementos else None
```

## 📋 Ejercicio Académico

Este proyecto implementa el siguiente ejercicio:

**Datos iniciales**: 51, 52, 63, 14, 18, 11, 25, 56, 40, 22, 87  
**Elementos a agregar**: 27, 12, 99  
**Eliminaciones a demostrar**:
- Nodo sin hijos (12)
- Nodo con 1 hijo (18)
- Nodo con 2 hijos (14)

Ejecuta `python examples/demo_completa.py` para ver la solución completa.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Algunas ideas para mejorar:

- Implementar balanceo del árbol (AVL, Rojo-Negro)
- Agregar más tipos de recorridos (preorden, postorden)
- Implementar serialización/deserialización del árbol
- Agregar visualización gráfica con bibliotecas como matplotlib
- Implementar tests unitarios

## 📝 Licencia

Este proyecto es de uso educativo y puede ser utilizado libremente.

## 👤 Autor

Proyecto ABB - Implementación educativa de Árboles Binarios de Búsqueda

---

**Versión**: 1.0.0  
**Última actualización**: Noviembre 2025
