from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import os

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()

path = ruta_dolar = os.path.join(directorio_actual, 'CHROME DRIVER', 'chromedriver-win64', 'chromedriver.exe')
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)


def obtener_valores_dolar():
    # Creamos las listas donde se guardan los values
    tipo_dolar = []
    valor_compra = []
    valor_venta = []
    # Definimos la web de donde vamos a sacar la info
    web = 'https://dolarhoy.com'
    driver.get(web)
    # Accedemos a la ruta xpath de donde esta el nodo padre
    valores_dolar = driver.find_elements(by='xpath', value='//div[@class="tile is-parent is-7 is-vertical"]/.. | //div[@class="tile is-parent is-5"]/..')
    # Accedemos a la info que necesitamos a partir de ese nodo padre
    for valor in valores_dolar:
        tipo_dolar.append(valor.find_element(by='xpath', value='./div[1]/div[@class="tile is-child"]/a').text)
        valor_compra.append(
            valor.find_element(by='xpath', value='./div[1]/div[@class="tile is-child"]/div/div[1]/div[2]').text)
        valor_venta.append(
            valor.find_element(by='xpath', value='./div[1]/div[@class="tile is-child"]/div/div[2]/div[2]').text)
        for x in range(2, 6):
            tipo_dolar.append(valor.find_element(by='xpath', value=f'./div[2]/div[{x}]/a').text)
            valor_compra.append(valor.find_element(by='xpath', value=f'./div[2]/div[{x}]/div/div[1]/div[2]').text)
            valor_venta.append(valor.find_element(by='xpath', value=f'./div[2]/div[{x}]/div/div[2]/div[2]').text)
    # Convertimos las listas a diccionario
    dict_dolar = {'tipo_dolar': tipo_dolar, 'valor_compra': valor_compra, 'valor_venta': valor_venta}
    time.sleep(2)
    driver.quit()
    df_dolar = pd.DataFrame(dict_dolar)
    ruta_dolar = os.path.join(directorio_actual, 'dataframes', 'cotizacion_dolar_hoy.csv')
    df_dolar.to_csv(path_or_buf=ruta_dolar, index=False)
    return print('Todo salio bien')