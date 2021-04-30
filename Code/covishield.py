import tkinter as tk  # Working and  integrated
from win32com.client import Dispatch
from tkinter import *
import webbrowser


def shield():
    app = tk.Tk()
    app.title("CHITI ")
    app.state("zoomed")
    app.configure(bg='#855388')

    new = 1
    url = "https://en.wikipedia.org/wiki/Oxford%E2%80%93AstraZeneca_COVID-19_vaccine"

    def openweb():
        webbrowser.open(url, new=new)

    url_1 = "https://www.seruminstitute.com/product_covishield.php"

    def openweb_1():
        webbrowser.open(url_1, new=new)

    url_2 = "hhttps://vaccine.icmr.org.in/covid-19-vaccine"

    def openweb_2():
        webbrowser.open(url_2, new=new)

    tk.Label(app, text="BASIC  INFORMATION  ABOUT  COVISHIELD \n", fg="red", font=("bold", 20)).pack()
    text = Text(app, width=180, height=180, font=("helvetica", 13))
    text.insert(tk.END,
                "\n1. The Oxford–AstraZeneca COVID-19 vaccine, codenamed AZD1222 and sold under the brand name Covishield and Vaxzevria among others,is a viral vector vaccine for COVID-19 \ndeveloped by Oxford University and AstraZeneca given by intramuscular injection, using as a vector the modified chimpanzee adenovirus ChAdOx1..\n\n 2. One dosing regimen showed 90% efficacy in preventing contracting COVID-19 when a half-dose was followed by a full-dose after at least one month, based on mixed trials with no \nparticipants over 55 years of age,no individuals who were clinically obese and individuals who for the most part had no underlying condition. \n\n 3.The vaccine has a good safety profile; though more than 10% of recipients during clinical trials reported mild adverse effects including injection site pain, headache and nausea; all \ngenerally resolving within a few days. More rarely, anaphylaxis may occur (the UK Medicines and Healthcare products Regulatory Agency (MHRA) has 234 reports out of approximately\n 11.7 million vaccinations as of 7 March 2021).\n\n 4.  The protein of interest is the spike protein, an external protein that enables the SARS-type coronavirus to enter cells through the enzymatic domain of ACE2.Producing it following \nvaccination will prompt the immune system to attack the coronavirus through antibodies and T-cells if it later infects the body.\n\n\n\n\tFor further details please click this button")

    Btn = tk.Button(app, text=" Click here to know from Wikipedia ", bg="light blue", bd=10, font=("bold", 13),
                    command=openweb)
    Btn.place(x=100, y=500)

    Btn = tk.Button(app, text=" Click here to know about Covishield from Serum Institute ", bg="light blue", bd=10,
                    font=("bold", 13), command = openweb_1)
    Btn.place(x=450, y=500)

    Btn = tk.Button(app, text=" Click here to know about Covishield from  ICMR", bg="light blue", bd=10,
                    font=("bold", 13), command = openweb_2)
    Btn.place(x=930, y=500)
    text.pack()

    def talk():
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(
            "\n\n1. The Oxford–AstraZeneca COVID-19 vaccine, codenamed AZD1222 and sold under the brand name Covishield and Vaxzevria among others,is a viral vector vaccine for COVID-19 developed by Oxford University and AstraZeneca given by intramuscular injection, using as a vector the modified chimpanzee adenovirus ChAdOx1..\n\n\n 2. One dosing regimen showed 90% efficacy in preventing contracting COVID-19 when a half-dose was followed by a full-dose after at least one month, based on mixed trials with no participants over 55 years of age,no individuals who were clinically obese and individuals who for the most part had no underlying condition. \n\n\n 3.The vaccine has a good safety profile; though more than 10% of recipients during clinical trials reported mild adverse effects including injection site pain, headache and nausea; all generally resolving within a few days. More rarely, anaphylaxis may occur (the UK Medicines and Healthcare products Regulatory Agency (MHRA) has 234 reports out of approximately 11.7 million vaccinations as of 7 March 2021) \n\n\n 4.  The protein of interest is the spike protein, an external protein that enables the SARS-type coronavirus to enter cells through the enzymatic domain of ACE2.Producing it following vaccination will prompt the immune system to attack the coronavirus through antibodies and T-cells if it later infects the body.\n\n\n\tFor further details please click this button")

    button = Button(app, text="Voice Assistance", bg="light blue", bd=10,font=("bold", 13), command=talk)
    button.place(x=450, y=600)

    button1 = Button(app, text="Back", bg="light blue", bd=10,font=("bold", 13), command=app.destroy)
    button1.place(x=930, y=600)
