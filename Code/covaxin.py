import tkinter as tk  # Working and  integrated
from win32com.client import Dispatch
from tkinter import *
import webbrowser


def vaxin():
    app = tk.Tk()
    app.title("CHITI ")
    app.state("zoomed")
    app.configure(bg='#855388')

    new = 1
    url = "https://en.wikipedia.org/wiki/BBV152"

    def openweb():
        webbrowser.open(url, new=new)

    url_1 = "https://www.bharatbiotech.com/covaxin.html"

    def openweb_1():
        webbrowser.open(url_1, new=new)

    url_2 = "https://vaccine.icmr.org.in/covid-19-vaccine"

    def openweb_2():
        webbrowser.open(url_2, new=new)

    tk.Label(app, text="BASIC  INFORMATION  ABOUT  COVAXIN\n", fg="red", font=("bold", 20)).pack()
    text = Text(app, width=160, height=150, font=("helvetica", 13))
    text.insert(tk.END,
                "\n  BBV152 (also known as Covaxin) is an inactivated virus-based COVID-19 vaccine being developed by Bharat Biotech in collaboration with the Indian Council of Medical Research.\n\n1. The vaccine candidate is produced with Bharat Biotech's in-house vero cell manufacturing platform that has the capacity to deliver about 300 million doses. The company is in the \nprocess of setting up a second plant at its Genome Valley facility in Hyderabad to make Covaxin. The firm is in talks with other state governments like Odisha for another site in the country to make the vaccine.\n\n 2. In November 2020, Covaxin received the approval to conduct Phase III human trials after completion of Phase I and II. The trial involves a randomised, double-blinded and controlled \nstudy among volunteers of age group 18 and above and started on 25 November. The Phase III trials involved around 26,000 volunteers from across India. \n\n 3. The phase III trials covered a total of 22 sites consisting several states in the country, including Delhi, Karnataka and West Bengal. Refusal rate for Phase III trials was much higher \nthan that for Phase I and Phase II. As a result only 13,000 volunteers had been recruited by 22 December with the number increasing to 23,000 by 5 January .\n\n 4. Beside this, they are also exploring global tie-ups for Covaxin manufacturing.In December 2020, Ocugen Inc entered a partnership with Bharat Biotech to co-develop Covaxin for the US market. In January 2021, Precisa Med entered an agreement with Bharat Biotech to supply Covaxin in Brazil.\n\n\tFor further details please click this button")

    Btn = tk.Button(app, text=" Click here to know about Covaxin from  wikipedia", bg="light blue", bd=10,
                    font=("bold", 13), command=openweb)
    Btn.place(x=90, y=550)

    Btn = tk.Button(app, text=" Click here to know about Covaxin from  Bharath BioTech", bg="light blue", bd=10,
                    font=("bold", 13), command=openweb_1)
    Btn.place(x=90, y=480)

    Btn = tk.Button(app, text=" Click here to know about Covaxin from  ICMR", bg="light blue", bd=10, font=("bold", 13),
                    command=openweb_2)
    Btn.place(x=90, y=630)
    text.pack()

    def talk():
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(
            " \n\n BBV152 (also known as Covaxin) is an inactivated virus-based COVID-19 vaccine being developed by Bharat Biotech in collaboration with the Indian Council of Medical Research.\n\n1. The vaccine candidate is produced with Bharat Biotech's in-house vero cell manufacturing platform that has the capacity to deliver about 300 million doses. The company is in the process of setting up a second plant at its Genome Valley facility in Hyderabad to make Covaxin. The firm is in talks with other state governments like Odisha for another site in the country to make the vaccine. \n\n\n 2. Beside this, they are also exploring global tie-ups for Covaxin manufacturing.In December 2020, Ocugen Inc entered a partnership with Bharat Biotech to co-develop Covaxin for the U.S. market. In January 2021, Precisa Med entered an agreement with Bharat Biotech to supply Covaxin in Brazil.\n\n\n\tFor further details please click this button")

    button = Button(app, text="Voice Assistance", bg="light blue", bd=10, font=("bold", 13), command=talk)
    button.place(x=950, y=500)

    button1 = Button(app, text="Back", bg="light blue", bd=10, font=("bold", 13), command=app.destroy)
    button1.place(x=1200, y=500)
