from tensorflow import keras
import prediction
from pandas.core.frame import DataFrame
from google.protobuf.json_format import MessageToDict
import mediapipe as mp
import cv2
import time
import base64
from tkinter import Tk, messagebox
import os
import logging
import eel
import sys
import platform
print('Opening python...')


# from camera import VideoCamera


# Use latest version of Eel from parent directory
sys.path.insert(1, '../../')


@eel.expose  # Expose function to JavaScript
def say_hello_py(x):
    """Print message from JavaScript on app initialization, then call a JS function."""
    print('Hello from %s' % x)
    eel.say_hello_js('Python {from within say_hello_py()}!')


@eel.expose
def hello_world():
    return "Hello from python"


@eel.expose
def print_string(string):
    if len(string) > 20:
        print(string)
        return "Success!"
    else:
        return "Too few characters. Please type more than 20 characters."


###


def show_error(title, msg):
    root = Tk()
    root.withdraw()  # hide main window
    messagebox.showerror(title, msg)
    root.destroy()


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        print(selectedcamera)
        self.video = cv2.VideoCapture(selectedcamera)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        return image
        # ret, jpeg = cv2.imencode('.jpg', image)
        # return jpeg.tobytes()


def gen(camera, model):

    success = True
    framecount = 1
    framecount2 = 1

    while True:
        img = camera.get_frame()
        framecount += 1
        framecount2 += 1

        if not success:
            break
        # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   #conversion into RGB for hands object
        # results = hands.process(imgRGB)                 #process method in hands into results

        # if results.multi_hand_landmarks:                #if hand is detected
        #     handNo = 1

        #     for handLms in results.multi_hand_landmarks:#for each hand in the results

        #         for id, lm in enumerate(handLms.landmark):

        #             for id, hand_handedness in enumerate(results.multi_handedness):
        #                 handedness_dict = MessageToDict(hand_handedness)

        #         mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #drawing on BGR image
        # if cv2.waitKey(20) & 0xFF==ord('d'):
        #     break

        ret, jpeg = cv2.imencode('.jpg', img)

        # if framecount2 == 15:
        #     cv2.imwrite('temp.jpg', img)
        #     try:
        #         tempjpg = prediction.image_process('temp.jpg')
        #     except FileNotFoundError:
        #         print(FileNotFoundError)

        #     df, result = prediction.prediction(model , tempjpg, prediction.dire )
        #     if result != "none":
        #         print(result)
        #     if os.path.exists("temp.jpg"):

        #         os.remove('temp.jpg')
        #     framecount2 = 1

        frame = jpeg

        yield frame


def gen2(camera, model):

    success = True
    framecount = 1
    framecount2 = 1

    while True:
        framecount += 1
        framecount2 += 1

        if not success:
            break
        # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   #conversion into RGB for hands object
        # results = hands.process(imgRGB)                 #process method in hands into results

        # if results.multi_hand_landmarks:                #if hand is detected
        #     handNo = 1

        #     for handLms in results.multi_hand_landmarks:#for each hand in the results

        #         for id, lm in enumerate(handLms.landmark):

        #             for id, hand_handedness in enumerate(results.multi_handedness):
        #                 handedness_dict = MessageToDict(hand_handedness)

        #         mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #drawing on BGR image
        # if cv2.waitKey(20) & 0xFF==ord('d'):
        #     break

        if framecount2 == 30:
            img = camera.get_frame()

            cv2.imwrite('temp.jpg', img)

            try:
                tempjpg = prediction.image_process('temp.jpg')
            except FileNotFoundError:
                print(FileNotFoundError)

            df, result = prediction.prediction(model, tempjpg, prediction.dire)
            print(result)
            # if result != "none":
            #     print(result)
            #     yield result
            yield result

            if os.path.exists("temp.jpg"):

                os.remove('temp.jpg')
            framecount2 = 1


@eel.expose
def video_feed():

    model = keras.models.load_model('testModel.h5')

    # x = VideoCamera()
    # x.__del__
    # x = VideoCamera()

    y = gen(x, model)
    for each in y:
        # Convert bytes to base64 encoded str, as we can only pass json to frontend
        blob = base64.b64encode(each)
        blob = blob.decode("utf-8")
        eel.updateImageSrc(blob)()
        # time.sleep(0.1)

###


@eel.expose
def predict_output():

    model = keras.models.load_model('testModel.h5')

    # x = VideoCamera()
    # x.__del__
    # x = VideoCamera()

    print('initialized predict_output')
    y = gen2(x, model)
    for each in y:
        print(each)
        eel.updateTextSrc(each)()
        # time.sleep(0.1)


@eel.expose
def cameravalue(current):
    global selectedcamera
    selectedcamera = current

    if(current == 0):
        selectedcamera = current
    else:

        selectedcamera = current - 1

    global x

    x = VideoCamera()
    x.__del__()
    x = VideoCamera()
    print(selectedcamera)


@eel.expose
def getcamera():
    eel.getCameraValue(selectedcamera + 1)


@eel.expose
def callIncrement(questionBufferCounter, currentChar):
    eel.updateQuestion()
    eel.increment(questionBufferCounter, currentChar)


def start_eel(develop):
    """Start Eel with either production or development configuration."""
    directory = 'src'
    eel.init(directory)
    say_hello_py('Python World!')
    # Call a JavaScript function (must be after `eel.init()`)
    eel.say_hello_js('Python World!')

    global selectedcamera
    selectedcamera = 0

    global x
    x = VideoCamera()
    x.__del__()
    x = VideoCamera()

    eel_kwargs = dict(
        host='localhost',
        port=9000,
        # size=(1280, 800),
    )
    try:
        # eel.start(page, mode=app, **eel_kwargs)
        eel.start(**eel_kwargs)

    except EnvironmentError:
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start(page, mode='edge', **eel_kwargs)
        else:
            raise


if __name__ == '__main__':
    import sys

    # Pass any second argument to enable debugging
    start_eel(develop=len(sys.argv) == 2)
