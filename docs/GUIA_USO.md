# Guía de Uso del Proyecto ABB

Este documento proporciona instrucciones detalladas sobre cómo usar el proyecto.

## Estructura de Carpetas

### `src/core/`
Contiene las implementaciones principales del ABB:
- **`arbol_abb.py`**: Implementación con predecesor inorden
- **`abb_sucesor.py`**: Implementación con sucesor inorden

### `src/visualization/`
Contiene los módulos de visualización:
- **`visualizador_basico.py`**: Visualización simple
- **`visualizador_grafico.py`**: Visualización con gráficos
- **`visualizador_circulos.py`**: Visualización con círculos

### `examples/`
Contiene ejemplos de uso:
- **`ejemplo_basico.py`**: Operaciones básicas
- **`ejemplo_comparacion.py`**: Comparación de estrategias
- **`ejemplo_visualizaciones.py`**: Demos de visualización
- **`demo_completa.py`**: Ejercicio completo

## Formas de Ejecutar el Proyecto

### 1. Menú Interactivo (Recomendado)

```bash
python main.py
```

Esto abrirá un menú interactivo donde puedes elegir qué ejemplo ejecutar.

### 2. Ejecutar Ejemplos Individuales

```bash
# Ejemplo básico
python examples/ejemplo_basico.py

# Comparación de estrategias
python examples/ejemplo_comparacion.py

# Visualizaciones
python examples/ejemplo_visualizaciones.py

# Demo completa
python examples/demo_completa.py
```

### 3. Usar como Librería

Puedes importar las clases en tus propios scripts:

```python
from src.core.arbol_abb import ArbolBinarioBusqueda

# Crear y usar el árbol
abb = ArbolBinarioBusqueda()
abb.agregar(50)
abb.agregar(30)
abb.agregar(70)
abb.mostrar_arbol()
```

## Operaciones Disponibles

### Crear un Árbol

```python
from src.core.arbol_abb import ArbolBinarioBusqueda

abb = ArbolBinarioBusqueda()
```

### Agregar Elementos

```python
# Agregar uno a uno
abb.agregar(50)
abb.agregar(30)

# Agregar múltiples elementos
datos = [50, 30, 70, 20, 40]
for valor in datos:
    abb.agregar(valor)
```

### Buscar Elementos

```python
existe = abb.buscar(30)  # Returns True o False
if existe:
    print("El elemento existe en el árbol")
```

### Eliminar Elementos

```python
# Eliminar un elemento
abb.eliminar(30)

# El método detecta automáticamente el tipo de nodo:
# - Sin hijos (hoja)
# - Con un hijo
# - Con dos hijos (usa predecesor o sucesor)
```

### Recorrido del Árbol

```python
# Obtener elementos ordenados
elementos = abb.recorrido_inorden()
print(elementos)  # [20, 30, 40, 50, 70]
```

### Visualizar el Árbol

```python
# Visualización básica
abb.mostrar_arbol()

# O usar visualizadores especiales
from src.visualization.visualizador_circulos import ArbolCirculos

vis = ArbolCirculos()
for valor in [50, 30, 70]:
    vis.agregar(valor)
vis.dibujar_estilo_simple()
```

## Estrategias de Eliminación

### Predecesor Inorden

```python
from src.core.arbol_abb import ArbolBinarioBusqueda

abb = ArbolBinarioBusqueda()
# Al eliminar un nodo con 2 hijos, usa el máximo del subárbol izquierdo
abb.eliminar(valor)
```

### Sucesor Inorden

```python
from src.core.abb_sucesor import ABBConSucesor

abb = ABBConSucesor()
# Al eliminar un nodo con 2 hijos, usa el mínimo del subárbol derecho
abb.eliminar_con_sucesor(valor)
```

## Tipos de Visualización

### 1. Visualización Básica (Texto Estructurado)

```python
from src.core.arbol_abb import ArbolBinarioBusqueda

abb = ArbolBinarioBusqueda()
abb.agregar(50)
abb.agregar(30)
abb.mostrar_arbol()
```

Salida:
```
Raíz: 50
    ├── I: 30
    └── D: 70
```

### 2. Visualización Gráfica

```python
from src.visualization.visualizador_grafico import ArbolGrafico

vis = ArbolGrafico()
vis.agregar(50)
vis.dibujar_con_conexiones()
```

### 3. Visualización con Círculos

```python
from src.visualization.visualizador_circulos import ArbolCirculos

vis = ArbolCirculos()
vis.agregar(50)
vis.dibujar_estilo_simple()
```

## Solución del Ejercicio

Para ver la solución completa del ejercicio académico:

```bash
python examples/demo_completa.py
```

O desde el menú interactivo, selecciona la opción 4.

## Consejos y Mejores Prácticas

1. **Evitar duplicados**: El ABB no permite elementos duplicados
2. **Orden de inserción**: El orden afecta el balance del árbol
3. **Visualización**: Usa diferentes visualizadores según tus necesidades
4. **Estrategia de eliminación**: Elige predecesor o sucesor según tu caso de uso

## Solución de Problemas

### Error de importación

Si obtienes errores de importación, asegúrate de:
1. Ejecutar los scripts desde el directorio raíz del proyecto
2. Los archivos `__init__.py` existen en todas las carpetas

### El árbol no se visualiza correctamente

- Algunos terminales pueden no soportar caracteres Unicode
- Prueba diferentes visualizadores
- Asegúrate de que tu terminal use codificación UTF-8

## Extensiones Futuras

Ideas para extender el proyecto:
- Implementar recorridos preorden y postorden
- Agregar balanceo automático (AVL)
- Implementar árbol rojo-negro
- Agregar persistencia (guardar/cargar árbol)
- Crear interfaz gráfica con Tkinter o PyQt
