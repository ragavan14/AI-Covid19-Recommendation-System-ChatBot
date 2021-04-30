from tkinter import *


def graph2():
    app = Tk()
    app.geometry("500x500")
    app.title("Covid-19 Tracker - By Country")

    # 'china','italy','usa','spain','germany',

    def displayData():
        from matplotlib import pyplot as plt
        import matplotlib.patches as mpatches
        from covid import Covid

        # default source = john_hopkins
        covid = Covid(source='worldometers')
        cases = []
        confirmed = []
        active = []
        deaths = []
        recovered = []

        try:
            app.update()
            countries = data.get()
            country_names = countries.strip()
            country_names = country_names.replace(" ", ",")
            country_names = country_names.split(",")
            for country in country_names:
                cases.append(covid.get_status_by_country_name(country))
                app.update()

            for case in cases:
                confirmed.append(case['confirmed'])
                active.append(case['active'])
                deaths.append(case['deaths'])
                recovered.append(case['recovered'])

            confirmed_patch = mpatches.Patch(color='red', label='Confirmed')
            active_patch = mpatches.Patch(color='blue', label='Active')
            recovered_patch = mpatches.Patch(color='green', label='Recovered')
            deaths_patch = mpatches.Patch(color='black', label='Deaths')

            plt.legend(handles=[confirmed_patch, active_patch, recovered_patch, deaths_patch])
            for country in range(len(country_names)):
                plt.bar(country_names[country], confirmed[country], color="red")
                plt.bar(country_names[country], active[country], color="blue")
                plt.bar(country_names[country], recovered[country], color="green")
                plt.bar(country_names[country], deaths[country], color="black")

            plt.title('Current Covid-19 Cases')
            plt.xlabel('Country Name')
            plt.ylabel('Cases (in millions)')
            plt.show()
        except Exception as e:
            print(f"Enter correct details country. \n {e}")

    Label(app, text="Enter all countries, for whom you want to get!", font="Consolas 15").pack()

    Label(app, text="Enter country name: ").pack()

    data = StringVar()
    data.set("Seperate country names using comma or space (not both)")

    entry = Entry(app, textvariable=data, width=60).pack()

    Button(app, text="Show Data", command=displayData).pack()

    app.mainloop()
