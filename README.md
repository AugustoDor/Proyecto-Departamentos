# Proyecto de Web Scraping de Departamentos en Resistencia, Chaco

Este proyecto realiza un web scraping de publicaciones de departamentos en venta en la ciudad de Resistencia, Chaco, desde el sitio web de Zonaprop, almacena la información en un archivo CSV y realiza una limpieza de los datos. Finalmente, se implementa una API que permite obtener recomendaciones de propiedades en base a distintos criterios.

## Contenido del Proyecto

### 1. scraping_deptos.py

Este archivo contiene el código para realizar el web scraping de Zonaprop. Las funciones principales son:

obtener_valores_depto():
Abre un navegador mediante undetected_chromedriver para simular un usuario real y evitar bloqueos.
Navega entre las páginas de Zonaprop para extraer enlaces a publicaciones de departamentos en venta.
Para cada publicación, obtiene detalles como el precio, dirección y características del inmueble (metros cuadrados, ambientes, baños, dormitorios, y cocheras).
Guarda los datos extraídos en un archivo CSV (venta_deptos.csv) en la carpeta dataframes.

### 2. limpiar_datos.py

Este archivo realiza la limpieza y transformación de los datos extraídos. Las principales tareas son:

Limpieza de valores nulos y ajuste de los precios multiplicándolos por 1000 (dado que los precios suelen estar en miles en Zonaprop).
Separación de calle y altura a partir de la dirección del departamento.
Extracción de características de los inmuebles (metros totales, metros cubiertos, cantidad de ambientes, baños, dormitorios y cocheras) mediante expresiones regulares.
Guardado de los datos limpios en un nuevo archivo CSV (venta_deptos_limpio.csv) en la misma carpeta dataframes.

### 3. EDA.py

Este archivo realiza un análisis exploratorio de los datos (EDA) sobre el conjunto de datos limpio. Aquí puedes agregar gráficos y estadísticas básicas, como:

Distribución de precios, tamaños (metros cuadrados) y cantidad de ambientes.
Correlaciones entre variables.
Estadísticas descriptivas de las propiedades.

### 4. main.py
Este archivo implementa una API usando FastAPI para exponer los datos y ofrecer recomendaciones basadas en las propiedades.

## Las principales rutas de la API son:

/recomendar/puntuacion: Proporciona recomendaciones de departamentos según un rango de precio y criterios ponderados como cantidad de ambientes, dormitorios, baños y cocheras. La recomendación se basa en una puntuación calculada en base a estos pesos.
/recomendar/knn: Proporciona recomendaciones de departamentos utilizando el algoritmo K-Nearest Neighbors (KNN). Requiere como entrada una nueva propiedad con características como precio, metros cuadrados, cantidad de ambientes, dormitorios, baños y cocheras para recomendar propiedades similares.

## Requisitos

Python 3.x

## Bibliotecas necesarias (pueden instalarse con el archivo requirements.txt):

pip install requests beautifulsoup4 pandas selenium undetected_chromedriver fastapi pydantic scikit-learn
Selenium y undetected_chromedriver: usados para el scraping.
FastAPI: para implementar la API de recomendaciones.
Ejecución del Proyecto
Ejecutar scraping_deptos.py para obtener los datos iniciales de Zonaprop.
Ejecutar limpiar_datos.py para procesar y limpiar los datos.
(Opcional) Ejecutar EDA.py para analizar los datos obtenidos.

## Ejecutar main.py para iniciar la API de recomendaciones:

uvicorn main:app --reload

## Ejemplos de Uso de la API

Recomendación por Puntuación:
GET /recomendar/puntuacion?rango_precio_min=50000&rango_precio_max=100000&peso_ambientes=2&peso_dormitorios=1&peso_banios=1&peso_cocheras=1

Recomendación por KNN:
POST /recomendar/knn
{
  "precio": 75000,
  "metros_totales": 50,
  "ambientes": 2,
  "dormitorios": 1,
  "banios": 1,
  "cocheras": 1
}

## Notas
El archivo scraping_deptos.py contiene pausas y una espera implícita para reducir la carga en el sitio web y evitar bloqueos.
limpiar_datos.py requiere ajustes adicionales si los datos obtenidos tienen variaciones en el formato.

## Contribuidores
