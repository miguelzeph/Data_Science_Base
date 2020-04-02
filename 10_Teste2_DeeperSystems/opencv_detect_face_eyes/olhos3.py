
import cv2

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eyeCascade= cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')



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



# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), 255, 2)
    roi = image[y:y+h, x:x+w]

    eyes = eyeCascade.detectMultiScale(roi)
    for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh), 255, 2)
# Exibir a imagem
cv2.imshow("Titulo da imagem", image)
cv2.waitKey(0)



