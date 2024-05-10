import tasca1
import logging
import os

def calcular_paraules():
    arxiu = 'paraules.txt'
    if not os.path.exists(arxiu):
        logging.error(f'No es va trobar el arxiu {arxiu} per a la Tasca 2.')
        return
    else:
        with open(arxiu, 'r') as f:
            palabras = f.read().split('\n')
        with open('paraulesQuantitat.txt', 'w') as f:
            for palabra in palabras:
                f.write(f'{len(palabra)}\t{palabra}\n')
                logging.info(f'Paraula {palabra} escrita en el arxiu paraulesQuantitat.txt amb la seva llargada.')