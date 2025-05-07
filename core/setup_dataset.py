# core/setup_dataset.py
import os

# Lista de letras incluyendo la Ñ
letras = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

base_path = 'dataset'

for letra in letras:
    dir_path = os.path.join(base_path, letra)
    os.makedirs(dir_path, exist_ok=True)
    print(f'📁 Carpeta creada: {dir_path}')
