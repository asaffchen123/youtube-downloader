from tkinter import*
import tkinter as tk
import pytube
from tkinter import messagebox,filedialog
import pytube
from moviepy.editor import *
from PIL import ImageTk,Image
from time import sleep

root=tk.Tk()
root.title("Youtube Downloader")
root.geometry("900x506")
x=StringVar()
y=StringVar()

C=Canvas(root, bg="grey", height=900, width=506)
filename=ImageTk.PhotoImage(Image.open(r"C:\Users\Home\Documents\studying\youtube downloader\wallpaper.png"))
background_label=Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()


label1=tk.Label(root,text="Enter Link:",font="Helvetica 12 bold",fg="white",bg="#E62922")
label1.place(x=10,y=10)
entry1=tk.Entry(root,textvariable=x)
entry1.place(x=100,y=10,width=250,height=23)
label2=tk.Label(root,text="Save As:",font="Helvetica 12 bold",fg="white",bg="#E62922")
label2.place(x=380,y=10)
entry2=tk.Entry(root,textvariable=y)
entry2.place(x=460,y=10,width=250,height=23)
label3=tk.Label(root,text="",font="Helvetica 12 bold",fg="white",bg="#E62922")
label3.place(x=360,y=90)


def toaudio():
    name=y.get()
    mp4_file = r'C:\Users\Home\Documents\studying\youtube downloader\downloadfolder\{}.mp4'.format(name)
    mp3_file = r'C:\Users\Home\Documents\studying\youtube downloader\downloadfolder\{}.mp3'.format(name)

    videoclip = VideoFileClip(mp4_file)

    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()
    label3.place_forget()
    label3.place(x=320,y=90)
    label3.config(text="Video has been converted to MP3")
    convert_button.place_forget()

def downloade():
    url=x.get()
    name=y.get()
    youtube=pytube.YouTube(url)
    video=youtube.streams.get_highest_resolution()
    video.download(output_path=r"C:\Users\Home\Documents\studying\youtube downloader\downloadfolder",filename=name)
    label3.config(text="Download completed")
    convert_button.place(x=340,y=115,width=200)
    

def clear_all():
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    label3.place_forget()



download_button=tk.Button(root,text="Download",font= "bold",fg="black",command=downloade,anchor="center",justify=CENTER)
download_button.place(x=1,y=50,width=898)

clear_button=tk.Button(root,text="Reset",font= "bold",fg="black",command=clear_all,anchor="center",justify=CENTER)
clear_button.place(x=720,y=10,height=25,width=150)
convert_button=tk.Button(root,text="Convert To MP3",font= "bold",fg="black",command=toaudio,anchor="center",justify=CENTER)

root.mainloop()
