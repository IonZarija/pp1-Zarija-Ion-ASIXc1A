"""
Ion Zarija
ASIXc1A
M03 UF3 Prova Pràctica
10/05/2024
"""

import tasca1
import tasca2
import logging
import time
import os

logging.basicConfig(filename='paraules.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

inicio = time.time()
logging.info('Inici del process.')
tasca1.procesar_palabras()
tasca2.calcular_paraules()
fin = time.time()
logging.info('Fi del process.')
logging.info(f'El procesamiento de palabras tardó {fin - inicio} segundos.')