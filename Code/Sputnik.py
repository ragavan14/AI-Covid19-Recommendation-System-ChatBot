import tkinter as tk  # Working and  integrated
from win32com.client import Dispatch
from tkinter import *
import webbrowser


def vaxin_1():
    app = tk.Tk()
    app.title("CHITI ")
    app.state("zoomed")
    app.configure(bg='#855388')

    new = 1
    url = "https://en.wikipedia.org/wiki/Sputnik_V_COVID-19_vaccine"

    def openweb():
        webbrowser.open(url, new=new)

    url_1 = "https://sputnikvaccine.com/"

    def openweb_1():
        webbrowser.open(url_1, new=new)

    tk.Label(app, text="BASIC  INFORMATION  ABOUT  SPUTNIK - V\n", fg="red", font=("bold", 20)).pack()
    text = Text(app, width=100, height=100,font=("helvetica", 13))
    text.insert(tk.END,
                "\n\n 1. The Russian Sputnik V vaccine acknowledges that immunity to the viral vector could be a problem, but comes up with a   different solution. It uses two different human adenoviruses – Ad26 and Ad5 (out of the 50 that affect humans) – for its two \nvaccine doses. This heterologous (or hybrid) vaccine, with different vectors for prime and booster vaccinations, is less likely  to have one jab generate an immune response against the viral vector that then interferes with the other.\n\n The vaccine is therefore less likely to have a reduced efficacy..\n\n\n\tFor further details please click this button...")


    Btn = tk.Button(app, text=" Click here to know about SPUTNIK V from  wikipedia", bg="light blue", bd=10,font=("bold", 13), command=openweb)
    Btn.place(x=300, y=500)

    Btn = tk.Button(app, text=" Click here to know about SPUTNIK V from  Official Website", bg="light blue", bd=10,font=("bold", 13), command=openweb_1)
    Btn.place(x=300, y=580)

    text.pack()

    def talk():
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(
            " \n\n The Russian Sputnik V vaccine acknowledges that immunity to the viral vector could be a problem, but comes up with a different solution. It uses two different human adenoviruses – Ad26 and Ad5 (out of the 50 that affect humans) – for its two vaccine doses. This heterologous (or hybrid) vaccine, with different vectors for prime and booster vaccinations, is less likely to have one jab generate an immune response against the viral vector that then interferes with the other. The vaccine is therefore less likely to have a reduced efficacy..\n\n\n\tFor further details please click this button....")

    button = Button(app, text="Voice Assistance", bg="light blue", bd=10,font=("bold", 13), command=talk)
    button.place(x=900, y=500)

    button1 = Button(app, text="Back", bg="light blue", bd=10, font=("bold", 13),command=app.destroy)
    button1.place(x=900, y=600)