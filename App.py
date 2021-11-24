from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageDraw, ImageFont, ImageTk


class App(Tk):
    def __init__(self):
        self.window = Tk()
        self.window.title("WaterMarkIt")
        self.window.config(width=500, height=300, bg="#71DFE7", padx=15, pady=15)
        self.label = Label(text="WaterMarkIt!", font=("Helvetica",
                                                      35,
                                                      "bold"), fg="#FFE652")
        self.label.config(bg="#71DFE7")
        self.label.grid(column=0, row=0, pady=8)
        self.button = Button(activebackground="#FFE652", command=self.open_file,
                             text="Upload Image", padx=8, font=("Helvetica",
                                                                12), fg="white", highlightthickness=0,
                             bg="#009DAE").grid(column=0, row=1, pady=8)

        self.file_path = ""
        self.label2 = Label(text="", font=("Helvetica",
                                           12,
                                           "bold"), fg="white")
        self.label2.config(bg="#71DFE7")
        self.label2.grid(column=0, row=3, pady=9)
        self.window.mainloop()

    def watermarkImage(self):
        im = Image.open(self.file_path)
        width, height = im.size

        draw = ImageDraw.Draw(im)
        text = "www.yourwebsite.com/brandname"
        font = ImageFont.truetype('arial.ttf', 36)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, font=font)
        im.show()

        im.save('watermark.jpeg')
        self.label2 = Label(text="Watermark saved!", font=("Helvetica",
                                                           10,
                                                           "bold"), fg="white")
        self.label2.config(bg="#71DFE7")
        self.label2.grid(column=0, row=5, pady=9)

    def open_file(self):
        self.file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')]).name

        if self.file_path is not None:
            self.label2.config(text=f"{self.file_path.split('/')[-1]} uploaded")
            self.button2 = Button(activebackground="#FFE652", command=self.watermarkImage,
                                  text="WaterMark Image", padx=8, font=("Helvetica",
                                                                        12), fg="white", highlightthickness=0,
                                  bg="#009DAE").grid(column=0, row=4, pady=10)
        else:
            pass