import cv2

classification = "./haarcascades/haarcascade_eye_tree_eyeglasses.xml"

# Setando a classificacao do xml da OpenCV para olhos
faceCascade = cv2.CascadeClassifier(classification)

# Ler a imagem
image = cv2.imread("lena.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Fazer a deteccao da imagem
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=1,
    minSize=(5, 5)
)

print(faces)

# Setar o retangulo amarelo
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 210), 2)


# Exibir a imagem
cv2.imshow("Titulo da imagem", image)
cv2.waitKey(0)



