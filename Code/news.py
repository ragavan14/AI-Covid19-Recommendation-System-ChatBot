import tkinter as tk
from win32com.client import Dispatch
from tkinter import messagebox
import webbrowser
import tkinter
from tkinter import *
from PIL import Image, ImageTk


def news1():
    app = tk.Tk()
    app.title("CHITI ")
    app.state("zoomed")
    app.configure(bg='#855388')

    new = 1
    url = "https://www.who.int/health-topics/coronavirus#tab=tab_1"

    def openweb():
        webbrowser.open(url, new=new)

    url_1 = "https://www.mohfw.gov.in/"

    def openweb_1():
        webbrowser.open(url_1, new=new)

    tk.Label(app, text="BASIC  NEWS  ON  COVID-19 \n", fg="red", font=("bold", 20)).pack()
    text = Text(app, width=150, height=150, font=("helvetica", 13))
    text.insert(tk.END,
                "\n  Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Coronavirus disease 2019 (COVID-19) is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first case was identified in Wuhan, China, in December 2019. The disease has since spread worldwide, leading to an       ongoing pandemic.\n\n 1. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment. Older people, and those with \n underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.\n\n\n2. The best way to prevent and slow down transmission is to be well informed about the COVID-19 virus, the disease it causes and how it spreads.\n Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face. The COVID-19 virus spreads primarily through    droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s  important that you  also practice respiratory etiquette. ")

    lbl = Label(app, text="Symptoms:", font=('arial', 15), bd=8)
    lbl.place(x=75, y=325)

    text.insert(tk.END,
                "\n\n\n\n\n\t\tSymptoms of COVID-19 are variable, but often include fever, cough, fatigue, breathing difficulties, and loss of smell and taste. Symptoms may begin   one to fourteen days after exposure to the virus. At least a third of people who are infected do not develop noticeable symptoms.\n\n\n\tFor further details please click this button")

    Btn = tk.Button(app, text=" Click  here  for   WHO  website", bg="light blue", bd=10, font=("bold", 13),
                    command=openweb)
    Btn.place(x=150, y=530)

    Btn = tk.Button(app, text=" Click  here  for  MoHFW  website", bg="light blue", bd=10, font=("bold", 13),
                    command=openweb_1)
    Btn.place(x=150, y=630)
    text.pack()

    def talk():
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(
            " 1.Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Coronavirus disease 2019 (COVID-19) is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first case was identified in Wuhan, China, in December 2019. The disease has since spread worldwide, leading to an ongoing pandemic.\nMost people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.   Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.\n\n\n2. The best way to prevent and slow down transmission is to be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face. The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette .SymptomsSymptoms of COVID-19 are variable, but often include fever, cough, fatigue, breathing difficulties, and loss of smell and taste. Symptoms may begin   one to fourteen days after exposure to the virus. At least a third of people who are infected do not develop noticeable symptoms.  \n\n\n\tFor further details please click this button")

    button1 = Button(app, text="Back", bg="light blue", bd=15, font=("bold", 13), command=app.destroy)
    button1.place(x=580, y=630)

    button2 = Button(app, text=" Voice Assistance", bg="light blue", bd=15, font=("bold", 13), command=talk)
    button2.place(x=580, y=530)

