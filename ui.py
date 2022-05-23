from datetime import datetime

import webbrowser
from tkinter import *

import requests

from tkmacosx import Button
from params import *

THEME_COLOR = "#cdbdf2"


class Interface:

    def __init__(self):



        self.window = Tk()
        self.window.title("Code Habit Tracker")
        self.window.config(padx= 20, pady = 20, bg = THEME_COLOR)

        self.hoursToAdd = Entry(width = 7)
        self.hoursToAdd.grid(column = 1, row= 0)

        self.hoursLb = Label(text= "                                       hours coded",
                             bg= THEME_COLOR,
                             fg= "black")
        self.hoursLb.grid(column = 0, row = 0)

        self.canvas = Canvas(height= 50, width= 300, bg= "white")

        #Create a Label to display the link
        self.link = Label(text="Code Habit Tracker",font=('Arial bold', 20), fg="black", bg = "white", cursor="hand2")

        self.link.bind("<Button-1>", lambda e:
        webbrowser.open_new_tab("https://pixe.la/v1/users/matviiev/graphs/graph1.html"))
        self.link.grid(column = 0, row = 1, columnspan= 2)

        self.question_text = self.canvas.create_text(150, 25,
                                                     fill = "black",
                                                     font = "Arial 20 italic",
                                                     width= 280)

        self.canvas.grid(column = 0, row = 1, columnspan= 2, pady= 20)





        # right button



        self.rightBtn = Button(text= "CHANGE HOURS",
                              bg = "#9d91b8",
                              fg = THEME_COLOR,
                              borderwidth = 4,
                              activebackground = (THEME_COLOR, THEME_COLOR),
                              activeforeground= "white",
                              command= self.addHours

                          )

        self.rightBtn.grid(column = 0, row= 2, columnspan= 2)


        self.window.mainloop()


    def addHours(self):
        graphDraw_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
        #
        # now = datetime(year = 2021, month = 5, day = 23)
        now = datetime.now()
        today = now.strftime("%Y%m%d")
        # hours = int(self.hoursToAdd.get())
        hours = self.hoursToAdd.get()

        graphDraw_config = {
            "date": today,
            "quantity": hours,
        }

        response = requests.post(url = graphDraw_endpoint, json = graphDraw_config, headers = headers)
        print(response.text)












