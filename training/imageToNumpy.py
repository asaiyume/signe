import os
import cv2

BASE_DIR = 'archive'

TRAIN_DIR = os.path.join(BASE_DIR, 'asl_alphabet_train/asl_alphabet_train')

TEST_DIR = os.path.join(BASE_DIR, 'asl_alphabet_test/asl_alphabet_test')


def convert_img_to_data(img_dir, img_size):
    x = []
    y = []
    labels = os.listdir(img_dir)

    for i in labels:
        img_file_path = os.path.join(img_dir, i)
        img_list = os.listdir(img_file_path)

        for img_name in img_list:
            img_path = os.path.join(img_file_path, img_name)
            img = cv2.imread(img_path)
            resized_img = cv2.resize(img, (img_size, img_size))
            resized_img = resized_img/255.0
            x.append(resized_img)
            y.append(i)
            print(img_name)
    print('Done')
    return x, y


if __name__ == '__main__':
    convert_img_to_data(
        '../data/archive/asl_alphabet_train/asl_alphabet_train', 128)
