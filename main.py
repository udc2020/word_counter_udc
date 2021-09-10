#############################################
### word Counter App Created By UltrasDzCoder 
#############################################

from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        ###### SETTINGS ⚙ ######
        self._black_color = "#222"
        self._white_color = "#f2f2f2"
        self.font = "Courier"


        ###### GUI ######
        self.Gui()

    def Gui(self):
        ###### WINDOW SETTINGS ######
        self.title("word Counter")
        self.iconbitmap(r"C:\Users\UDC\Desktop\tkinter\images.ico")

        

        app_width = 600
        app_height = 800
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        x = (width / 2) - (app_width / 2)
        y = (height / 2) - (app_height / 2)

        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.config(bg=self._black_color, padx=20)

        ###### INNER SHAPE ######
        title_label = Label(self,
                            text="word Counter",
                            bg="#222",
                            fg="#f2f2f2",
                            width=200,
                            font=(self.font, "25"))

        title_label.grid(row=0, column=1)
        title_label.pack(pady=5)

        fram = Frame(self, width=100, height=2, bg=self._black_color)
        fram.config(highlightbackground=self._white_color,
                    highlightthickness=1)
        fram.pack()

        input_box = Text(fram,
                         bg="#111",
                         fg="#f2f2f2",
                         font=(self.font, 20),
                         pady=15,
                         padx=15,
                         height=10)

        input_box.pack()
        canvas = Label(self, height=1, bg=self._black_color)
        canvas.pack()

        btn_count = Button(self,
                           text="Count All",
                           bg="#ccc",
                           width=10,
                           command=lambda: self.print_all_in_label(
                               input_box.get("1.0", "end")),
                           padx=10)
        btn_count.config(font=(self.font, 20))
        btn_count.pack()

        canvas = Label(self, height=1, bg=self._black_color)
        canvas.pack()

        self.text1 = StringVar()
        self.text2 = StringVar()
        self.text3 = StringVar()
        self.text4 = StringVar()

        self.text1.set("0")
        self.text2.set("0")
        self.text3.set("0")
        self.text4.set("0")

        self.label_Creator("char ", self.text1)
        self.label_Creator("words ", self.text2)
        self.label_Creator("uppercase ", self.text3)
        self.label_Creator("number ", self.text4)

    ###### LABEL CREATETOR ######
    def label_Creator(self, title, var):
        lb6 = Label(self,
                    text=title,
                    fg="white",
                    bg=self._black_color,
                    font=(self.font, "20"))
        lb6.pack()

        lb7 = Label(self,
                    textvariable=var,
                    fg="white",
                    bg=self._black_color,
                    font=(self.font, "20"))
        lb7.pack()

    ###### PROCESSES ######
    def print_all_in_label(self, text):
        all_list = self.count_all(text)
        self.text1.set(str(all_list[0]))
        self.text2.set(str(all_list[1]))
        self.text3.set(str(all_list[2]))
        self.text4.set(str(all_list[3]))

    def count_all(self, text):

        len_char = self.get_len(text)
        len_words = self.get_words(text)
        count_upper = self.get_upper(text)
        count_num = self.get_numb(text)

        return (len_char, len_words, count_upper, count_num)

    def get_len(self, text):
        return len(text.replace(" ", "").strip())

    def get_words(self, text):
        return len(text.split())

    def get_upper(self, text):
        counter = 0
        for t in text:
            if t.isupper():
                counter += 1
        return counter

    def get_numb(self, text):
        counter = 0
        for t in text:
            if t.isnumeric():
                counter += 1
        return counter


def main():
    myApp = App()
    myApp.mainloop()


if "__main__" == __name__: main()



#### Make This file to EXE 
#### pip install auto-py-to-exe
#### auto-py-to-exe