# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:48:45 2020

@author: User
"""

from pytube import YouTube
from tkinter import *
root = Tk()
root.geometry("300x600")
root.title("Youtube Vedio Downloader")
def youtube():
    a= var.get()
    ytvideo = YouTube(a).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
    ytvideo.download(r"C:\Users\User\Desktop")
    
    print("Entry Box",a)
l1 = Label(text = "Youtube vedio link",fg="Red")
l1.place(x=30,y=20)
var=StringVar()
e1=Entry(root,textvariable=var,width=50)
e1.place(x=60,y=80)
b1=Button(root,text="download",command=youtube,bg="green",width=20,fg="white")
b1.place(x=80,y=120)
root.mainloop()