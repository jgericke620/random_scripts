#!/usr/local/bin/python3

import time
from pynput.mouse import Button, Controller

def mouseMove():
    hor = 0.1
    ver = 0.1
    mouse = Controller()
    while(True):
        time.sleep(60)
        mouse.move(hor, ver)

if __name__ == "__main__":
    mouseMove()

