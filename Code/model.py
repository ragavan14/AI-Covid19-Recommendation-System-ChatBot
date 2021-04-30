from covid import Covid
import tkinter
from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk


def country_stat():
    covid = Covid(source="worldometers")
    data = covid.get_data()

    confirmed = covid.get_total_confirmed_cases()
    active = covid.get_total_active_cases()

    recovered = covid.get_total_recovered()
    deaths = covid.get_total_deaths()

    new = 1
    url = "https://www.worldometers.info/coronavirus/"

    def openweb():
        webbrowser.open(url, new=new)

    def show_answer():
        gconfirmed.delete(0, 'end')
        gactive.delete(0, 'end')
        grecovered.delete(0, 'end')
        gdeaths.delete(0, 'end')
        sconfirmed.delete(0, 'end')
        sactive.delete(0, 'end')
        srecovered.delete(0, 'end')
        sdeaths.delete(0, 'end')

        gconfirmed.insert(0, confirmed)
        gactive.insert(0, active)
        grecovered.insert(0, recovered)
        gdeaths.insert(0, deaths)

        result = variable.get()

        for i in data:
            if i["country"] == result:
                sconfirmed.insert(0, i["confirmed"])
                sactive.insert(0, i["active"])
                srecovered.insert(0, i["recovered"])
                sdeaths.insert(0, i["deaths"])

    app = Tk()
    app.title("CHITI ")
    app.state("zoomed")

    Label(app, text=" Global Confirmed Cases :", font=("bold", 14)).grid(row=5, column=0)
    Label(app, text=" Global Active Cases :", font=("bold", 14)).grid(row=5, column=2)
    Label(app, text=" Global Recovered Cases :", font=("bold", 14)).grid(row=25, column=0)
    Label(app, text=" Global Death Cases :", font=("bold", 14)).grid(row=25, column=2)
    Label(app, text=" #########################################################").grid(row=45, column=1)
    Label(app, text=" Data for specific country", fg="red", font=("Helvetica", 20)).grid(row=47, column=1)
    Label(app, text="## ######################################################").grid(row=51, column=1)

    result = ['']
    value = 0
    for i in data:
        if value == 0:
            result[0] = (i['country'])
        else:
            result.append(i['country'])
        value += 1

    variable = StringVar(app)
    variable.set(result[0])

    Label(app, text="Select a country to monitor :", font=("Helvetica", 18)).grid(row=57, column=1)
    OptionMenu(app, variable, *result ).grid(row=57, column=2)

    Label(app, text=" Confirmed Cases :", font=("bold", 14)).grid(row=100, column=0)
    Label(app, text=" Active Cases :", font=("bold", 14)).grid(row=100, column=2)
    Label(app, text=" Recovered Cases :", font=("bold", 14)).grid(row=150, column=0)
    Label(app, text=" Death Cases :", font=("bold", 14)).grid(row=150, column=2)

    gconfirmed = Entry(app)
    gactive = Entry(app)
    grecovered = Entry(app)
    gdeaths = Entry(app)
    sconfirmed = Entry(app)
    sactive = Entry(app)
    srecovered = Entry(app)
    sdeaths = Entry(app)

    gconfirmed.grid(row=5, column=1, pady=6)
    gactive.grid(row=5, column=3)
    grecovered.grid(row=25, column=1)
    gdeaths.grid(row=25, column=3)

    sconfirmed.grid(row=100, column=1)
    sactive.grid(row=100, column=3)
    srecovered.grid(row=150, column=1)
    sdeaths.grid(row=150, column=3)

    Button(app, text='Quit', bg="light blue", bd=10, font=("bold", 13), command=app.destroy).grid(row=1200, column=1,
                                                                                                  sticky=W)
    Button(app, text='show', bg="light blue", bd=10, font=("bold", 13), command=show_answer).grid(row=1200, column=2,
                                                                                                  sticky=W, pady=6)
    Button(app, text='Click here for more Details', bg="light blue", bd=10, font=("bold", 13), command=openweb).grid(
        row=1200, column=4,
        sticky=W,
        pady=6)







