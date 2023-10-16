from tkinter import *
from pytube import YouTube

#Tkinter
root = Tk()
root.title('Youtube Downloader')
#Pytube
#Default, change later
path = "C:\\Users\\16506\\Documents\\Coding\\Python\\VideoDownloader\\Videos"
link = "https://www.youtube.com/watch?v=iMjsSLTisao"

def downloadVideo():
    try:
        yt = YouTube(eLink.get())
    except:
        print('invalid Link!!')

    ys = yt.streams.get_highest_resolution()


    try:
        ys.download(ePath.get())
    except:
        print('Video Cannot Download!!')


#Path
labelPath = Label(root, text="Path")
labelPath.grid(row = 0, column = 0)
ePath = Entry(root, width=100)
ePath.insert(0, path)
ePath.grid(row = 0, column = 1, columnspan = 5, padx=50)

#YoutubeLink
labelLink = Label(root, text="YT Link")
labelLink.grid(row=1, column=0)
eLink = Entry(root, width=100)
eLink.insert(0,link)
eLink.grid(row=1, column=1, columnspan=5, padx=50)

#Button2Download
buttonDownload = Button(root, text="Download Video", padx=10, pady=10, command=downloadVideo)
buttonDownload.grid(row=2, column = 2)

#the window continues
root.mainloop()