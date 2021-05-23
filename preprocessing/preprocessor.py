import mediapipe as mp
import cv2
import time
from google.protobuf.json_format import MessageToDict
import os
from os import listdir
from os.path import isfile, join
import numpy
import csv


class preprocessor:

    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()  # hand object from mediapipe
        self.mpDraw = mp.solutions.drawing_utils  # line drawing utilities

    def directory_to_csv(self, path, outputFile):
        # get actual script location
        try:
            dire = listdir(path)

        except FileNotFoundError:
            print("Location not found!")
            return False

        output = []

        files = [f for f in listdir(path) if isfile(
            join(path + '\\', f))]  # all files in dir listed

        for i in range(len(files)):
            line = []
            line.append(files[i])
            file = path + "\\" + \
                files[i]
            print(file)
            img = cv2.imread(file)
            # conversion into RGB for hands object
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # process method in hands into results
            results = self.hands.process(imgRGB)

            if results.multi_hand_landmarks:  # if hand is detected

                for handLms in results.multi_hand_landmarks:  # for each hand in the results

                    for id, hand_handedness in enumerate(results.multi_handedness):
                        handedness_dict = MessageToDict(hand_handedness)

                    line.append(handedness_dict['classification'][0]['label'])

                    for id, lm in enumerate(handLms.landmark):  # location of landmarks
                        lm_dict = MessageToDict(lm)
                        line.append(lm_dict['x'])
                        line.append(lm_dict['y'])
                        line.append(lm_dict['z'])
                    break
            output.append(line)

        colName = ['word', 'letter']
        for i in range(1, 64):
            colName.append(str(i))

        with open(outputFile, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(colName)
            writer.writerows(output)

        print("Successfully generated " + outputFile + '.')
        return True

    def directory_in_directory_to_csv(self, path, outputFile):
        try:
            dire = listdir(path)
        except FileNotFoundError:
            print("Location not found!")
            return False
        output = []

        for j in dire:
            files = [f for f in listdir(path + '\\' + j) if isfile(
                join(path + '\\' + j, f))]  # all files in dir listed

            for i in range(len(files)):
                line = []
                line.append(j)
                file = path + "\\" + j + '\\' + \
                    files[i]
                print(file)
                img = cv2.imread(file)
                # conversion into RGB for hands object
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # process method in hands into results
                results = self.hands.process(imgRGB)

                if results.multi_hand_landmarks:  # if hand is detected

                    for handLms in results.multi_hand_landmarks:  # for each hand in the results

                        for id, hand_handedness in enumerate(results.multi_handedness):
                            handedness_dict = MessageToDict(hand_handedness)

                        line.append(
                            handedness_dict['classification'][0]['label'])

                        # location of landmarks
                        for id, lm in enumerate(handLms.landmark):
                            lm_dict = MessageToDict(lm)
                            line.append(lm_dict['x'])
                            line.append(lm_dict['y'])
                            line.append(lm_dict['z'])
                        break
                output.append(line)

        colName = ['word', 'letter']
        for i in range(1, 64):
            colName.append(str(i))

        with open(outputFile, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(colName)
            writer.writerows(output)

        print("Successfully generated " + outputFile + '.')
        return True

    def single_image_to_numpy(self, filename):

        line = []

        file = filename
        print('Converting ' + filename + ' to numpy array...')
        try:
            img = cv2.imread(file)
        except cv2.error:
            print("File not found!")
            return False
        # conversion into RGB for hands object
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # process method in hands into results
        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks:  # if hand is detected

            for handLms in results.multi_hand_landmarks:  # for each hand in the results

                for id, hand_handedness in enumerate(results.multi_handedness):
                    handedness_dict = MessageToDict(hand_handedness)

                for id, lm in enumerate(handLms.landmark):  # location of landmarks
                    lm_dict = MessageToDict(lm)
                    line.append(lm_dict['x'])
                    line.append(lm_dict['y'])
                    line.append(lm_dict['z'])
                break
        if line != []:
            array = numpy.array(line)
            array = array.reshape(21, 3)
        else:
            print('Hand not detected!')
            return []
        return array

    def multiple_image_to_numpy(self, path):
        try:
            dire = listdir(path)
        except FileNotFoundError:
            print("Location not found!")
            return
        output = []
        print('Converting images in ' + path + ' to numpy array...')

        files = [f for f in listdir(path) if isfile(
            join(path + '\\', f))]  # all files in dir listed

        for i in range(len(files)):
            line = []
            file = path + "\\" + \
                files[i]
            print(file)
            img = cv2.imread(file)

            # conversion into RGB for hands object
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # process method in hands into results
            results = self.hands.process(imgRGB)
            if results.multi_hand_landmarks:  # if hand is detected

                for handLms in results.multi_hand_landmarks:  # for each hand in the results

                    for id, hand_handedness in enumerate(results.multi_handedness):
                        handedness_dict = MessageToDict(hand_handedness)

                    for id, lm in enumerate(handLms.landmark):  # location of landmarks
                        lm_dict = MessageToDict(lm)
                        line.append(lm_dict['x'])
                        line.append(lm_dict['y'])
                        line.append(lm_dict['z'])
                    break
            if line != []:
                output.append(line)
        if output != []:
            array = numpy.array(output)
            array = array.reshape(-1, 21, 3)
        return array

    def videoToNumpy(self):
        # WIP
        return


if __name__ == '__main__':
    print("RUNNING TESTS")
    preprocessor = preprocessor()
    if preprocessor.directory_to_csv(
            'data/archive/asl_alphabet_test/asl_alphabet_test', 'test.csv'):
        print("Directory to CSV SUCCESS")

    if preprocessor.single_image_to_numpy('data/archive/asl_alphabet_test/asl_alphabet_test/F_test.jpg') != []:
        print("NUMPY CONVERSION SUCCESS")

    if preprocessor.multiple_image_to_numpy(
            'data/archive/asl_alphabet_test/asl_alphabet_test') != []:
        print("MULTTIPLE NUMPY CONVERSION SUCCESS")
