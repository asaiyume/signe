from numpy.core.fromnumeric import argmax
from tensorflow import keras
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import os
import cv2

img_size = 58

# model = keras.models.load_model('training/testModel.h5')
# dire = os.listdir('data/train')


def prediction(model, array, items_l):
    prob = model.predict(array.reshape(1, img_size, img_size, 3))
    pro_df = pd.DataFrame(prob, columns=items_l)
    # if np.argmax(prob) > 0:
    #     result = items_l[np.argmax(prob)]
    # else:
    #     result = ''
    currentHigh = prob[0][np.argmax(prob)]
    if currentHigh >= 0.8:
        result = items_l[np.argmax(prob)]
    else:
        result = None
    return pro_df, result


def image_process(img):
    image = load_img(img, target_size=(img_size, img_size))
    image_array = img_to_array(image)/255.0
    return image_array


if __name__ == '__main__':
    model = load_model('training/testModel.h5')
    dire = os.listdir('data/train')
    print(dire)
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        # Display the resulting frame
        cv2.imshow('frame', frame)
        cv2.imwrite('test.jpg', frame)
        img = image_process('test.jpg')
        pro_df, result = prediction(model, img, dire)
        if result != None:
            print(result)

        if cv2.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
