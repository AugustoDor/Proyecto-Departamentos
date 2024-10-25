# <h1 align=center> **PROYECTO WEB SCRAPING** </h1>

Este proyecto realiza web scraping de datos de una página web utilizando Selenium y BeautifulSoup. Los datos obtenidos son procesados utilizando pandas, con el fin de guardarlos como .csv para poder tenerlos como fuentes de datos.
Es un proyecto simple, solo se enfoca en la práctica del WebScraping y su aprendizaje en simples pasos, más no se enfoca en el ETL, EDA o ML, para ello cuento con otros repositorios que puedes visitar.

## **Contexto**
El proyecto tiene como objetivo extraer datos de Inmuebles y en base a ellos calcular distintas métricas relacionadas con el beneficio posterior a adquirir el inmueble, esas métricas se pueden observar en **`calculos.py`**

**Nota**: Este proyecto es únicamente con fines educativos y de aprendizaje. No se busca que con él se tomen decisiones de ningún tipo. Los datos pertenecen a la página de donde fueron extraídos [zonaprop.com](https://www.zonaprop.com.ar/).

## **Requisitos**

Asegúrate de tener instalados los siguientes paquetes de Python:

- `selenium`
- `beautifulsoup4`
- `pandas`

Puedes instalarlos utilizando `pip`:

`pip install selenium beautifulsoup4 pandas`

Además, necesitarás tener un controlador web compatible con Selenium (por ejemplo, ChromeDriver para Google Chrome).

## **Uso**
### **Realizar Web Scraping (solo si se quiere ejecutar el scraping, mas no limpiar los datos)**
Los scripts **`scraping_deptos.py`** y **`scraping_dolar.py`** utilizan Selenium para navegar por la página web y BeautifulSoup para extraer los datos relevantes.

**Para ejecutar el script de scraping:**

`python scraping_deptos.py`

`python scraping_dolar.py`

### **Limpieza de Datos (si se quiere realizar scraping y además limpiar los datos)**
El script **`limpiardatos.py`** tiene a la función que scrapea comentada, hay que descomentarla y ejecutar el script.

**Para ejecutar el script de limpieza de datos:**

`python limpiardatos.py`

## **Contribuciones**
Las contribuciones son bienvenidas. Para contribuir, por favor, comunicate conmigo.
