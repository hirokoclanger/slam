#!/usr/bin/env python3
import cv2
import sdl2.ext
from display import Display 

W = 1920//2
H = 1080//2

sdl2.ext.init()
window = sdl2.ext.Window("slam", size=(W,H), position=(800,500))
window.show()

disp = Display(W,H)

def process_frame(img):
    img = cv2.resize(img, (W,H))
    events = sdl2.ext.get_events()
    disp.paint(img) 
    print(img.shape)
    print(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
