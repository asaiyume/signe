from tensorflow import keras
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import load_img, img_to_array

IMG_SIZE = 128
dire = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
dire.insert(4, 'del')
dire.insert(19, 'space')
dire.insert(14, 'nothing')

model = keras.models.load_model('training/testModel.h5')


def prediction(model, array, items_l):
    prob = model.predict(array.reshape(1, IMG_SIZE, IMG_SIZE, 3))
    pro_df = pd.DataFrame(prob, columns=items_l)
    if np.argmax(prob) > 0.9:
        result = items_l[np.argmax(prob)]
    else:
        result = 'The model is not confident to give a prediction at the moment.'
    return pro_df, result


def image_process(img):
    image = load_img(img, target_size=(IMG_SIZE, IMG_SIZE))
    image_array = img_to_array(image)/255
    return image_array


if __name__ == '__main__':
    img_array = image_process('training/a.jpg')
    pro_df, result = prediction(model, img_array, dire)
    print(result)
