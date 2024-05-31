# Torres de Hanoi Visualizer

## Descripción
Este proyecto es un visualizador de las Torres de Hanoi implementado en Python utilizando la biblioteca `matplotlib`. El programa muestra gráficamente los movimientos de los discos entre las torres para resolver el juego de acuerdo con el número de discos configurado.

## Requisitos
Para ejecutar este programa, necesitarás Python y algunas bibliotecas que están listadas en el archivo `requirements.txt`. Asegúrate de tener Python instalado en tu sistema y luego instala las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Configuración
Puedes configurar el número de discos y otros parámetros del visualizador en el archivo `config.json`. Los parámetros configurables incluyen:

- `num_disks`: Número de discos en la torre (por defecto es 3).
- `speed`: Velocidad de la animación (no implementado completamente en el código actual).
- `colors`: Colores de los discos (no implementado completamente en el código actual).
- `window_size`: Tamaño de la ventana de visualización (no implementado completamente en el código actual).
- `title`: Título de la ventana (no implementado completamente en el código actual).

## Ejecución
Para ejecutar el visualizador, simplemente corre el archivo `main.py` con Python. Esto abrirá una ventana que muestra la solución gráfica del problema de las Torres de Hanoi con la configuración especificada.

```bash
python main.py
```

## Estructura del Proyecto
El proyecto incluye los siguientes archivos:
- `requirements.txt`: Contiene las bibliotecas necesarias para ejecutar el programa.
- `main.py`: El script principal que ejecuta la visualización de las Torres de Hanoi.
- `config.json`: Un archivo de configuración para personalizar la ejecución del visualizador.
- `README.md`: Este archivo, que proporciona información sobre el proyecto y cómo ejecutarlo.

## Contribuciones
Las contribuciones a este proyecto son bienvenidas. Si tienes sugerencias para mejorar el visualizador o para implementar características adicionales, no dudes en crear un pull request o abrir un issue en el repositorio del proyecto.

