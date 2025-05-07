import cv2
import os

# Ruta base del dataset
dataset_dir = "dataset"

# Tamaño del recorte (puedes ajustarlo si es necesario)
ancho, alto = 200, 200

# Pedimos al usuario qué letra va a capturar
letra = input("¿Qué letra quieres capturar? (ejemplo: A, B, C, Ñ): ").upper()
ruta_guardado = os.path.join(dataset_dir, letra)

if not os.path.exists(ruta_guardado):
    print(f"❌ La carpeta para la letra {letra} no existe. Crea las carpetas con 'setup_dataset.py' primero.")
    exit()

# Iniciar la cámara
cap = cv2.VideoCapture(0)

# Contador de imágenes
contador = 0
max_capturas = 200  # puedes cambiar el número de imágenes por clase

print(f"📸 Presiona 'c' para capturar imagen. 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # espejo para comodidad
    h, w, _ = frame.shape

    # Definir región de interés (ROI) centrada
    x1, y1 = int(w / 2 - ancho / 2), int(h / 2 - alto / 2)
    x2, y2 = x1 + ancho, y1 + alto

    # Dibujar el rectángulo
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Mostrar el frame
    cv2.imshow("Captura - Lengua de Señas", frame)

    key = cv2.waitKey(1)

    if key & 0xFF == ord('c'):
        # Cortar el ROI y guardar imagen
        recorte = frame[y1:y2, x1:x2]
        nombre_archivo = f"{letra}_{contador:03d}.jpg"
        cv2.imwrite(os.path.join(ruta_guardado, nombre_archivo), recorte)
        contador += 1
        print(f"✅ Imagen {contador} guardada como {nombre_archivo}")

        if contador >= max_capturas:
            print("✅ Captura completa.")
            break

    elif key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
