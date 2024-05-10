import os
import logging

def procesar_palabras():
    if not os.path.exists('paraules.txt'):
        logging.error('No es va trobar el arxiu paraules.txt per a la Tasca 1.')
        return
    else:
        with open('paraules.txt', 'r') as f:
            palabras = f.read().split('\n')
        for palabra in palabras:

            if palabra[0] == 'a' or palabra[0] == 'ä' or palabra[0] == 'á' or palabra[0] == 'à':
                with open(f'paraules-a.txt', 'a') as f:
                    f.write(palabra + '\n')
                logging.info(f'Paraula {palabra} escrita en el arxiu paraules-a.txt')

            elif palabra[0] == 'e' or palabra[0] == 'é' or palabra[0] == 'è' or palabra[0] == 'ë':
                with open(f'paraules-e.txt', 'a') as f:
                    f.write(palabra + '\n')
                logging.info(f'Paraula {palabra} escrita en el arxiu paraules-e.txt')

            elif palabra[0] == 'i' or palabra[0] == 'í' or palabra[0] == 'ì' or palabra[0] == 'ï':
                with open(f'paraules-i.txt', 'a') as f:
                    f.write(palabra + '\n')
                logging.info(f'Paraula {palabra} escrita en el arxiu paraules-i.txt')

            elif palabra[0] == 'o' or palabra[0] == 'ó' or palabra[0] == 'ò' or palabra[0] == 'ö':
                with open(f'paraules-o.txt', 'a') as f:
                    f.write(palabra + '\n')
                logging.info(f'Paraula {palabra} escrita en el arxiu paraules-o.txt')

            elif palabra[0] == 'u' or palabra[0] == 'ú' or palabra[0] == 'ù' or palabra[0] == 'ü':
                with open(f'paraules-u.txt', 'a') as f:
                    f.write(palabra + '\n')
                logging.info(f'Paraula {palabra} escrita en el arxiu paraules-u.txt')
