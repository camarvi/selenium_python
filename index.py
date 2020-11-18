# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

#Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

#driver_patch= 'home/carlos/curso_python/selenium/chromedriver'

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
#driver = webdriver.Chrome(driver_patch,options=options)


#Inicializar el navegador
driver.get('https://www.eltiempo.es/')

#Aceptar las cookies de la pagina, pulsar en aceptar
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.')))).click()

#Posicionarse en la caja de texto
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input#inputSearch')))\
    .send_keys('Almeria')

#Pulsar el boton de buscar
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'i.icon.icon-search')))\
    .click()

#Selecionar elemento icon_weather_s icon icon-local
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'i.icon_weather_s.icon.icon-local')))\
    .click()

#Seleccionar por horas, la pestaña por horas
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[7]/main/div[4]/div/section[4]/section/div/article/section/ul/li[2]/a')))\
    .click()

#Cargar los datos por horas
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')))

#Gaurdar la informacion en una variable

texto_columnas = driver.find_element_by_xpath('/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')  

texto_columnas = texto_columnas.text

tiempo_hoy = texto_columnas.split('Mañana')[0].split('\n')[1:-1]

horas = list()
temp = list()
v_viento = list()

for i in range(0,len(tiempo_hoy), 4 ):
    horas.append(tiempo_hoy[i])
    temp.append(tiempo_hoy[i+1])
    v_viento.append(tiempo_hoy[i+2])

df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'Viento(Km/h)': v_viento})
print(df)
df.to_csv('tiempo_hoy.csv', index=False)
#df.to_excel('tiempo_hoy.xls')

driver.quit()
