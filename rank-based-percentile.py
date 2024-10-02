from tkinter import *
from tkinter import messagebox

def getPercentile():
    try:
   
        students = int(total_participantField.get())
        rank = int(rankField.get())

     
        if students < 1 or rank < 1 or rank > students:
            messagebox.showerror("Input Error", "Please ensure the rank is between 1 and the total number of participants.")
            return

      
        result = round((students - rank) / students * 100, 3)

       
        percentileField.delete(0, END)
        percentileField.insert(10, str(result))

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for both rank and total participants.")

def Clear():
   
    rankField.delete(0, END)
    total_participantField.delete(0, END)
    percentileField.delete(0, END)

    rankField.focus_set()

if __name__ == "__main__":


    gui = Tk()
    gui.configure(background="light green")
    gui.title("Rank Based Percentile Calculator")
    gui.geometry("500x200")

    rank = Label(gui, text="Rank", bg="blue", fg="white", font=("Arial", 12, "bold"))
    andl = Label(gui, text="And", bg="light green", font=("Arial", 12))
    total_participant = Label(gui, text="Total Participants", bg="blue", fg="white", font=("Arial", 12, "bold"))
    percentile = Label(gui, text="Percentile", bg="blue", fg="white", font=("Arial", 12, "bold"))

  
    rankField = Entry(gui, font=("Arial", 12), justify="center")
    total_participantField = Entry(gui, font=("Arial", 12), justify="center")
    percentileField = Entry(gui, font=("Arial", 12), justify="center")

  
    find = Button(gui, text="Find Percentile", fg="Black", bg="Red", font=("Arial", 12, "bold"), command=getPercentile)
    clear = Button(gui, text="Clear", fg="Black", bg="Red", font=("Arial", 12, "bold"), command=Clear)

   
    rank.grid(row=1, column=1, padx=10, pady=10, sticky=E)
    rankField.grid(row=1, column=2, padx=10, pady=10)

    andl.grid(row=1, column=3, padx=10, pady=10)

    total_participant.grid(row=1, column=4, padx=10, pady=10, sticky=E)
    total_participantField.grid(row=1, column=5, padx=10, pady=10)

    find.grid(row=3, column=2, pady=20)
    percentile.grid(row=4, column=1, padx=10, pady=10, sticky=E)
    percentileField.grid(row=4, column=2, padx=10, pady=10)

    clear.grid(row=5, column=2, pady=10)

  
    rankField.focus_set()

   
    gui.mainloop()
