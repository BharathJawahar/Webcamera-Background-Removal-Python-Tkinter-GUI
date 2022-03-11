from tkinter import *
import cv2
from PIL import Image, ImageTk
from cvzone.SelfiSegmentationModule import SelfiSegmentation

class App:
    def __init__(self):
        self.bg_flag = False
        self.window = Tk()
        self.window.title("DIP Meeting | Team 11")
        self.window.resizable(0,0)
        self.window['bg']='white'
        self.video = VideoCapture()
        self.label = Label(self.window, text="DIP Meeting | Team 11", font=15, bg="blue", fg="white").pack(side=TOP, fill=BOTH)
        
        self.canvas = Canvas(self.window, width=self.video.width, height=self.video.height, bg="white")
        self.canvas.pack()

        self.bg_button = Button(self.window, text="Remove/Show Background", width=30, bg='white', activebackground="blue", command=self.switch_bg_flag)
        self.bg_button.pack(anchor=CENTER, expand=True)

        self.update()
        self.window.mainloop()
    def switch_bg_flag(self):
        if(self.bg_flag==True):
            self.bg_flag = False
        else:
            self.bg_flag = True
        #flag, frame = self.video.getFrame()
        #image = "B:\VITCC\Winter Sem 2021 . 8\Digital Image Processing . SWE1010\Project\Background-Removal-API\image1.png"
        #cv2.imwrite(image , frame)
        #cv2.imwrite('Frame'+str(i)+'.jpg', frame)
        #i += 1

        #msg = Label(self.window, text="bg_flag : " + str(self.bg_flag), bg="black", fg="green").place(x=430, y=510)
    def update(self):
        if(self.bg_flag==True):
            flag, frame = self.video.getFgFrame()
        else:
            flag, frame = self.video.getFrame()
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.window.after(1, self.update)

class VideoCapture:
    def __init__(self):
        self.segmentor = SelfiSegmentation()
        self.video = cv2.VideoCapture(0)
        self.width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    def getFrame(self):
        flag, frame = self.video.read()
        return(flag, frame)
    def getFgFrame(self):
        flag, frame = self.video.read()
        frame = self.segmentor.removeBG(frame, (0, 0, 0), threshold=0.5)
        return(flag, frame)
    def __del__(self):
        self.video.release()


App()