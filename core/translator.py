# core/translator.py
"""
Este módulo usa la cámara para detectar la forma de la mano y
reconocer letras del alfabeto (A-E) en Lengua de Señas Mexicana (LSM).
"""

import cv2
import mediapipe as mp
import numpy as np

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Diccionario de letras que vamos a entrenar (por ahora A-E)
letras_detectadas = {
    "A": "puño cerrado con pulgar al lado",
    "B": "mano extendida, palma al frente",
    "C": "forma de C con la mano",
    "D": "índice extendido, el resto doblado",
    "E": "dedos doblados hacia la palma"
}

def detectar_mano():
    cap = cv2.VideoCapture(0)  # Abre la cámara

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip horizontal para que se vea como espejo
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Dibuja los puntos de la mano en pantalla
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Aquí podríamos reconocer señas más adelante con ML
                # Por ahora solo mostramos que hay una mano
                cv2.putText(frame, "Mano detectada", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Traductor LSM - A-E", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detectar_mano()
