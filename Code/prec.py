import tkinter as tk
from win32com.client import Dispatch
from tkinter import *
import webbrowser

def prec():
    app = tk.Tk()
    app.title("CHITI ")
    app.state("zoomed")
    app.configure(bg='#855388')
    new = 1
    url = "https://www.mohfw.gov.in/"

    def openweb():
        webbrowser.open(url, new=new)

    url_1 = "https://www.cdc.gov/library/researchguides/2019novelcoronavirus/websites.html"

    def openweb_1():
        webbrowser.open(url_1, new=new)

    url_2 = "https://www.who.int/teams/integrated-health-services/infection-prevention-control"

    def openweb_2():
        webbrowser.open(url_2, new=new)

    tk.Label(app, text="PRECAUTIONS TO AVOID THE SPREAD OF COVID-19", fg="red", font=("bold", 20)).pack()
    text = Text(app, width=150, height=150, font=("helvetica", 13))
    text.insert(tk.END,
                "   You can reduce yours chances of being infected or Spreading COVID-19 by taking some simple precautions. \n\n1. Stay home and Self isolate even with minor symptoms of cough , sneeze , mild headache or fever. Wear a mask when physical distancing is not possible. Don’t touch your eyes, nose or mouth. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n\n\n2. Stay home if you feel unwell. If you have a fever , cough and difficulty breathing , seek medical attention immediately and follow the directions of your healthcare authority. WHY???...\n\tNational and Local authorities will have the most up to date information on the situation in yoour area. Calling in advance will allow your healthcare provider to quickly direct you    to the right health facility. This will also protect you and help prevent spread of viruses and other infections.\n\n\n3. Everyone 2 years and older should wear masks in public. Masks should be worn  in addition to staying at least 6 feet apart, especially around people who don’t live with you.\n If someone in your household is infected, people in the household should take precautions including wearing masks to avoid spread to others. \n\n\n 4. Wash your hands or use hand sanitizer before putting on your mask. Wear your mask over your nose and mouth and secure it under your chin. Fit the mask snugly against the sides of your face, slipping the loops over your ears or tying the strings behind your head.\n\n\n5. If you have to continually adjust your mask, it doesn’t fit properly, and you might need to find a different mask type or brand. Make sure you can breathe easily. \n\n\n 6. Consider going for a walk, bike ride, or wheelchair roll in your neighborhood or in another safe location where you can maintain at least 6 feet  of distance between yourself and other pedestrians and cyclists. If you decide to visit a nearby park, trail, or recreational facility, first check for closures or restrictions. \n\n\n 7.If open, consider how many other people might be there and choose a location where it will be possible to keep at least 6 feet of space between yourself and other people who are not  from your household. \n\n\n\tFor further details please click this button")

    Btn = tk.Button(app, text=" Click here for MoHFW website", bg="light blue", bd=10,font=("bold", 13), command=openweb)
    Btn.place(x=450, y=560)

    Btn = tk.Button(app, text=" Click here for CDC website", bg="light blue", bd=10,font=("bold", 13), command=openweb_1)
    Btn.place(x=450, y=630)

    Btn = tk.Button(app, text=" Click here for WHO  website", bg="light blue", bd=10,font=("bold", 13), command=openweb_2)
    Btn.place(x=750, y=600)
    text.pack()

    def talk():
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(
            "You can reduce yours chances of being infected or Spreading COVID-19 by taking some simple precautions :   \n\n1. Stay home and Self isolate even with minor symptoms of cough , sneeze , mild headache or fever. Wear a mask when physical distancing is not possible. Don’t touch your eyes, nose or mouth. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n\n\n2. Stay home if you feel unwell. If you have a fever , cough and difficulty breathing , seek medical attention immediately and follow the directions of your healthcare authority.Why?...\nNational and Local authorities will have the most up to date information on the situation in yoour area. Calling in advance will allow your healthcare provider to quickly direct you to the right health facility. This will also protect you and help prevent spread of viruses and other infections.\n\n\n3. Everyone 2 years and older should wear masks in public. Masks should be worn  in addition to staying at least 6 feet apart, especially around people who don’t live with you. If someone in your household is infected, people in the household should take precautions including wearing masks to avoid spread to others. \n\n\n 4. Wash your hands or use hand sanitizer before putting on your mask. Wear your mask over your nose and mouth and secure it under your chin. Fit the mask snugly against the sides of your face, slipping the loops over your ears or tying the strings behind your head. If you have to continually adjust your mask, it doesn’t fit properly, and you might need to find a different mask type or brand. Make sure you can breathe easily. \n\n\n 5. Consider going for a walk, bike ride, or wheelchair roll in your neighborhood or in another safe location where you can maintain at least 6 feet of distance between yourself and other pedestrians and cyclists. If you decide to visit a nearby park, trail, or recreational facility, first check for closures or restrictions. If open, consider how many other people might be there and choose a location where it will be possible to keep at least 6 feet of space between yourself and other people who are not from your household. \n\n\n\tFor further details please click this button")

    button1 = Button(app, text="Back", bg="light blue", bd=10,font=("bold", 13), command=app.destroy)
    button1.place(x=1200, y=565)

    button = Button(app, text="Voice Assistance", bg="light blue", bd=10,font=("bold", 13), command=talk)
    button.place(x=1190, y=640)
