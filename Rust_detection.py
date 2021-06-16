import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import urllib.request
import time

def rust_detection(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = tensorflow.keras.models.load_model('keras_model.h5')

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array isz
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(img)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)


    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    if (prediction[0][0]) >0.8  :
        result=0
    else:
        result=1
    print(result)
    return result

url="http://192.168.1.2:8080/shot.jpg"

statement = ""
col = (0, 0, 0)

while True:
    count=+1
    imgresp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgresp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    key = cv2.resizkey=cv2.waitKey(10)
    if key==ord('q'):
        break


    if key==ord('z'):
        cv2.imwrite("scan.jpeg", img)
        result=rust_detection("scan.jpeg")
        if result==0:
            statement="RUST DETECTED"
            col=(0,0,255)
        else:
            statement = "RUST NOT DETECTED"
            col = (0, 255, 0)
    if key==ord('s'):
        result = rust_detection(img="test_image.jpeg")
        if result == 0:
            statement="RUST DETECTED"
            col = (0, 0,255)
    cv2.putText(img, statement, (30, 240), cv2.FONT_HERSHEY_SIMPLEX, 1,col, 2, cv2.LINE_AA)

    cv2.imshow("test", img)
