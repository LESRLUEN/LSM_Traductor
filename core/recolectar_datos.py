# core/recolectar_datos.py
import cv2
import mediapipe as mp
import numpy as np
import os

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Carpeta para guardar los datos
DATA_DIR = './dataset'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Etiquetas: letras, palabras, etc.
etiquetas = ['hola', 'gracias', 'A', 'B', 'C']

# Tamaño por clase
NUM_MUESTRAS = 100

# Iniciar captura
cap = cv2.VideoCapture(0)

with mp_hands.Hands(static_image_mode=False,
                    max_num_hands=1,
                    min_detection_confidence=0.7) as hands:

    for etiqueta in etiquetas:
        print(f'[INFO] Recolectando: {etiqueta}')
        data_etiqueta = os.path.join(DATA_DIR, etiqueta)
        os.makedirs(data_etiqueta, exist_ok=True)
        muestra = 0

        while muestra < NUM_MUESTRAS:
            ret, frame = cap.read()
            if not ret:
                continue

            img = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            res = hands.process(rgb)

            if res.multi_hand_landmarks:
                for hand_landmarks in res.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    coords = []
                    for lm in hand_landmarks.landmark:
                        coords.extend([lm.x, lm.y, lm.z])

                    coords_np = np.array(coords)
                    np.save(os.path.join(data_etiqueta, f'{muestra}.npy'), coords_np)
                    muestra += 1

            cv2.putText(img, f'Muestra {muestra}/{NUM_MUESTRAS}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('Recolector de datos', img)
            if cv2.waitKey(1) & 0xFF == 27:
                break

cap.release()
cv2.destroyAllWindows()
