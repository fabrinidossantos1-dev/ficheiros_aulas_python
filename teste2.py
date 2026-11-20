from ultralytics import YOLO
# Importa a ferramenta YOLO da biblioteca Ultralytics.
# YOLO é um modelo de inteligência artificial utilizado
# para detetar e identificar objetos em imagens e vídeos.
 
import cv2
# Importa a biblioteca OpenCV.
# Permite aceder à webcam, capturar imagens e apresentar vídeos.
 
modelo = YOLO("yolov8n.pt")
# Carrega o modelo YOLOv8 Nano.
# O ficheiro yolov8n.pt contém um modelo de inteligência artificial
# treinado para reconhecer diferentes objetos.
# O modelo será guardado na variável modelo.
 
camera = cv2.VideoCapture(0)
# Abre a webcam do computador.
# O número 0 representa normalmente a câmara principal.
# Se existirem várias câmaras, podemos experimentar 1 ou 2.
 
while True:
# Cria um ciclo infinito.
# O programa vai continuar a executar enquanto não for interrompido.
 
    ret, frame = camera.read()
    # Captura uma imagem da webcam.
    # ret indica se a captura foi bem-sucedida (True ou False).
    # frame contém a imagem capturada pela webcam.
 
    resultados = modelo(frame)
    # Envia a imagem capturada para o modelo YOLO.
    # A inteligência artificial analisa a imagem e procura objetos.
    # Os resultados ficam guardados na variável resultados.
 
    imagem = resultados[0].plot()
    # Desenha na imagem os resultados da deteção.
    # Identifica os objetos através de caixas delimitadoras,
    # nomes dos objetos e valores de confiança.
    # A imagem com as deteções fica guardada em imagem.
 
    cv2.imshow("YOLO", imagem)
    # Apresenta a imagem numa janela com o nome YOLO.
    # Mostra o vídeo da webcam com os objetos identificados.
 
    if cv2.waitKey(1) == ord("q"):
        # Verifica se a tecla Q foi pressionada.
        # waitKey(1) aguarda aproximadamente 1 milissegundo.
        # ord("q") converte a letra q no seu código numérico.
 
        break
        # Interrompe o ciclo while quando pressionamos Q.
 
camera.release()
# Liberta a webcam.
# Permite que outros programas possam utilizar a câmara.
 
cv2.destroyAllWindows()
# Fecha todas as janelas abertas pelo OpenCV.