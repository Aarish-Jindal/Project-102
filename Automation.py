from email.mime import image
from operator import truediv
import cv2
import dropbox
import time
import random

startTime = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        startTime = time.time()
        result = False
    return image_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token = 'sl.A_lzK0WnasvAKYSCBMAyvYm71ZgTka5JRP8kjf7x25JrDXoz50sNsUl_bFKwrejqg_BHWHMNTsulJRnwv1Zt1MgeNCeXqM9ft3K_ApVxdEixUa8Lj8O2BsaB-xAnKLr3Nu7zYIZDJ5U7'
    file = image_name
    file_from = file
    file_to = "/newFolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_uploaded(f.read(), file_to, mode = dropbox.files.WriteMode.overWrite)
        print("file uploaded")

def main():
    while(True):
        if ((time.time() - startTime) >=3):
            name = take_snapshot()
            upload_file(name)

main()