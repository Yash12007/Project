from tkinter import *
import pyzbar.pyzbar as pyzbar
import cv2

def back():
    print("Have a good day...")
    exit()

def scan():
    root = Tk()
    root.geometry("720x500")
    i = 0
    cap = cv2.VideoCapture(0)
    while i<4:
        _, frame = cap.read()
        decoded = pyzbar.decode(frame)
        for obj in decoded:
            print(obj.data)
            i=i+1
            btn = Label(root, text=obj.data, font=("calibre", 19, "bold"), bg="black", fg="cyan")
            btn.pack()
            btn0 = Label(root, bg="white", fg="black", font=("calibre", 19), relief=SUNKEN)
            btn0.pack(side=RIGHT, anchor="se")
            btn1 = Button(btn0, text="Exit", command=back)
            btn1.pack(side=RIGHT, anchor="se")
            root.mainloop()
        cv2.imshow("Alice is Scanning", frame)
        cv2.waitKey(5)
        cv2.destroyAllWindows
scan()
