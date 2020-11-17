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