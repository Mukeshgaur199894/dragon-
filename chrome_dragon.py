import pyautogui
from PIL import Image,ImageGrab
from numpy import asarray
import time



def hit(key):
    pyautogui.press(key)
    return
def isCollide(data):
    # draw the rectangle for birds
    for i in range(195, 240):
        for j in range(312, 411):
            if data[i, j] <100:
                hit("down")
                return

    # draw the rectangle for cactus
    for i in range(250, 290):
        for j in range(411, 485):
           if data[i, j] < 100:
               hit("up")
               return
    return


# def draw():
if __name__ =="__main__":
    print("HEY ... dino games start about to start in 3 seconds ")
    time.sleep(1)
    hit("up")
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        isCollide(data)
        '''
        #draw the rectangle for cactus
        for i in range(220,250):
            for j in range(411,485):
                data[i,j]=0
        # draw the rectangle for birds
        for i in range(190, 220):
            for j in range(312, 411):
                data[i, j] = 171
        image.show()
        break
'''