import tkinter as tk
from tkinter import *
import json
import requests
import prec
import news
import graph
import model
import covaxin
import webbrowser
import covishield
import Sputnik
import regfrm

def min():

    def graap():
        graph.graph1()

    def fram():
        regfrm.graph2()

    def country1():
        model.country_stat()

    app = tk.Tk()
    app.title("CHITI ")
    app.state("zoomed")
    app.configure(bg='#855388')

    def createNewWindow_stat():  # Creates a new tab
        newWindow = tk.Toplevel(app)
        newWindow.state("zoomed")
        newWindow.configure(bg='#855388')

        b1 = tk.Button(newWindow, text="COUNTRYWISE STATISTICS", width=25, font=("bold", 15), bd=10, bg="light blue",
                       command=country1)
        b1.place(x=200, y=100)

        def state_stat():
            def get_state_info():
                url = "https://api.covid19india.org/data.json"
                response = requests.request("GET", url)

                # Get​ Data from API and store in json
                data = json.loads(response.text)

                # Get Index for Country
                searchstate = txt.get()

                def get_state_index(state):
                    for index, item in enumerate(data['statewise']):
                        if item['state'] == state:
                            return index

                stateid = get_state_index(searchstate)

                # Get​ New New Confirmed & Total Confirmed
                confirmed = data['statewise'][stateid]['confirmed']
                active = data['statewise'][stateid]['active']
                deaths = data['statewise'][stateid]['deaths']
                recovered = data['statewise'][stateid]['recovered']

                covid_msg = f'\n\n TOTAL NUMBER OF CONFIRMED CASES TILL DATE  {searchstate} = {confirmed}.\n THE TOTOAL NUMBER OF ACTIVE CASES =  {active}.\n TOTAL NUMBER OF DEATHS TILL DATE = {deaths}.\n TOTAL NUMBER OF RECOVERED TILL DATE = {recovered}.'

                # Return covid msg to gui
                output_text.set(covid_msg)

            window = Tk()
            window.title('CHITTI')
            window.geometry('400x400')

            # Create Label
            lbl = Label(window, text='Enter the State Name', font=("helvetica", 15))
            lbl.grid(column=6, row=1)

            # Create Entry Field
            txt = Entry(window, width=30)
            txt.grid(column=11, row=1)

            # Create Button
            btn = Button(window, text='Get Information', bg="light blue", bd=10, font=("bold", 10),
                         command=get_state_info)
            btn.grid(column=8, row=8)

            output_text = StringVar()
            lbl_output = Label(window, textvariable=output_text)
            lbl_output.grid(column=10, columnspan=4, row=18)

            window.mainloop()

        b2 = tk.Button(newWindow, text="STATE WISE STATISTICS", width=23, font=("bold", 15), bd=10, bg="light blue",command=state_stat)
        b2.place(x=200, y=300)

        b3 = tk.Button(newWindow, text="COUNTRY WISE COMPARISON OF GRAPHS", width=40, font=("bold", 15), bd=10,
                       bg="light blue",
                       command=fram)
        b3.place(x=200, y=500)

        b4 = tk.Button(newWindow, text="CONFIRMED CASES COMPARISON ", width=40, font=("bold", 15), bd=10,
                       bg="light blue",
                       command=graap)
        b4.place(x=700, y=300)

        button1 = Button(newWindow, text="Back", font=("bold", 15),bg="light blue", bd=10, command=app.destroy)
        button1.place(x=950, y=500)

    def createNewWindow_vacc():  # Creates a new tab
        newWindow = tk.Toplevel(app)
        newWindow.state("zoomed")
        newWindow.configure(bg='#855388')

        new = 1
        url = "https://www.cowin.gov.in/home"

        def openweb():
            webbrowser.open(url, new=new)

        def vac():
            covaxin.vaxin()

        b1 = tk.Button(newWindow, text="COVAXIN", width=25, font=("bold", 15), bd=10, bg="light blue", command=vac)
        b1.place(x=80, y=150)

        def vac1():
            covishield.shield()

        b2 = tk.Button(newWindow, text="COVISHIELD", width=23, font=("bold", 15), bd=10, bg="light blue", command=vac1)
        b2.place(x=430, y=150)

        def vac2():
            Sputnik.vaxin_1()

        b3 = Button(newWindow, text="SPUTNIK V ", width=32, font=("bold", 15), bd=10, bg="light blue",
                    command=vac2)
        b3.place(x=800, y=150)

        b4 = Button(newWindow, text="Find  your  Nearest  Vaccination  Center ", width=33, font=("bold", 17),bd=10 ,
                    bg="light blue",
                    command=openweb)
        b4.place(x=400, y=280)

        lbl = Label(newWindow, text="Would You Like to take a Vaccine ??...", font=('arial', 18), bd=18)
        lbl.place(x=100, y=450)

        b3 = tk.Button(newWindow, text="Yes", bg="light blue", bd=10,font=("bold", 15), command=openweb)
        b3.place(x=150, y=550)

        b4 = tk.Button(newWindow, text="No", bg="light blue", bd=10,font=("bold", 15), command=newWindow.destroy)
        b4.place(x=500, y=550)


    tk.Label(app, text="WELCOME  TO  COVID-19 RECOMMENDATION SYSTEM (CHATBOT) ", fg="red", font=("bold ", 30)).pack()

    def news_covid():
        news.news1()

    b = tk.Button(app, text="Info of Corona Virus", width=23, font=("bold", 17), bg="light blue", bd=10,
                  command=news_covid)
    b.place(x=220, y=150)

    b1 = tk.Button(app, text="Statistics", width=20, font=("bold", 17), bg="light blue", bd=10,
                   command=createNewWindow_stat)
    b1.place(x=570, y=150)

    def pree():
        prec.prec()

    b2 = tk.Button(app, text="Precautions", width=20, font=("bold", 17), bd=10, bg="light blue", command=pree)
    b2.place(x=880, y=150)


    b3 = tk.Button(app, text="Chat with Bot", width=20, font=("bold", 17), bd=10, bg="light blue")
    b3.place(x=400, y=350)

    b4 = tk.Button(app, text="Info About Vaccines", width=20, font=("bold", 17), bd=10, bg="light blue",
                   command=createNewWindow_vacc)
    b4.place(x=730, y=350)

    b4 = tk.Button(app, text="Exit", command=app.destroy, width=20, font=("bold", 17), bd=10, bg="light blue")
    b4.place(x=600, y=530)

    tk.mainloop()
