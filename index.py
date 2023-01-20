import tkinter
import customtkinter
from pytube import YouTube


def start_download():
    try:
        ytLink = link.get()
        ytObj = YouTube(ytLink, on_progress_callback=progress)
        video = ytObj.streams.get_highest_resolution()

        title.configure(text=ytObj.title, text_color="white")
        finish_label.configure(text="")
        video.download()
        finish_label.configure(text="Download finished", text_color="white")

    except:
        finish_label.configure(text="Error", text_color="red")


def progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    per = str(int(percentage_of_completion))
    percentage.configure(text=per + "%", text_color="white")
    percentage.update()

    progress_bar.set(float(percentage_of_completion) / 100)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a youtube link", text_color="white")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finish_label = customtkinter.CTkLabel(app, text="", text_color="white")
finish_label.pack()

percentage = customtkinter.CTkLabel(app, text="0%", text_color="white")
percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=350, height=40)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(
    app, text="Download", width=350, command=start_download
)
download.pack()

app.mainloop()
