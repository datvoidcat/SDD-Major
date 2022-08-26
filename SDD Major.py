from glob import glob
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox

# Defining the variables that control what virus is being modelled
setr0 = 2.28
setincubation = 5
setpercent_weak = 0.8
setweak_recovery = (7,14)
setpercent_strong = 0.2
setstrong_recovery = (21,42)
setstrong_death = (14,56)
setfatality_rate = 0.034
setserial_interval = 7

startscreen = tkinter.Tk()
startscreen.title("Covid simulation")
startscreen.geometry("500x300")

def openAdvsettings():
    global setr0
    global setincubation
    global setpercent_weak
    global setweak_recovery
    global setpercent_strong
    global setstrong_recovery
    global setstrong_death
    global setfatality_rate
    global setserial_interval
    Advsettings = Toplevel(startscreen)
 
    Advsettings.title("Advanced settings")
 
    Advsettings.geometry("500x1000")

    # Button for changing the value of r0 (average number of new infections as a result of 1 person becoming infected)
    r0_label = tkinter.Label(Advsettings, text='r0, default = 2.28')
    #r0_label.pack(pady=10)
    r0_entry = tkinter.Entry (Advsettings) 
    #r0_entry.pack(pady=10)
    def change_r0 (): 
        global setr0
        x1 = r0_entry.get()
        setr0 = str(x1)
        #print(setr0)
    r0_button = Button(Advsettings, text='Change r0', command=change_r0)

    r0_label.grid(row=1, column=1)
    r0_entry.grid(row=1, column=2)
    r0_button.grid(row=2, column=2, padx=10, pady=10)

    # Button for changing the incubation period
    inc_label = tkinter.Label(Advsettings, text='Incubation, default = 5')
    inc_entry = tkinter.Entry (Advsettings) 
    def change_inc ():  
        global setincubation
        x2 = inc_entry.get()
        setincubation = str(x2)
        print(setincubation)
    inc_button = Button(Advsettings, text='Change incubation period', command=change_inc)

    inc_label.grid(row=3, column=1)
    inc_entry.grid(row=3, column=2)
    inc_button.grid(row=4, column=2, padx=10, pady=10)

    # Button for changing the chance of a case being considered 'weak'
    pweak_label = tkinter.Label(Advsettings, text='Percent weak, default = 0.8')
    pweak_entry = tkinter.Entry (Advsettings) 
    def change_pweak (): 
        global setpercent_weak 
        x3 = pweak_entry.get()
        setpercent_weak = str(x3)
        print(setpercent_weak)
    pweak_button = Button(Advsettings, text='Change percent weak', command=change_pweak)

    pweak_label.grid(row=5, column=1)
    pweak_entry.grid(row=5, column=2)
    pweak_button.grid(row=6, column=2, padx=10, pady=10)

    # Button for changing the time until recovery from a weak case
    weakrec_label = tkinter.Label(Advsettings, text='Weak recovery, default = (7, 14)')
    weakrec_entry = tkinter.Entry (Advsettings) 
    def change_weakrec ():
        global setweak_recovery  
        x4 = weakrec_entry.get()
        setweak_recovery = str(x4)
        print(setweak_recovery)
    weakrec_button = Button(Advsettings, text='Change weak recovery time', command=change_weakrec)

    weakrec_label.grid(row=7, column=1)
    weakrec_entry.grid(row=7, column=2)
    weakrec_button.grid(row=8, column=2, padx=10, pady=10)

    # Button for changing the chance of cases being considered 'strong'
    pstrong_label = tkinter.Label(Advsettings, text='Percent strong, default = 0.2')
    pstrong_entry = tkinter.Entry (Advsettings) 
    def change_pstrong (): 
        global setpercent_strong 
        x5 = pstrong_entry.get()
        setpercent_strong = str(x5)
        print(setpercent_strong)
    pstrong_button = Button(Advsettings, text='Change percent strong', command=change_pstrong)

    pstrong_label.grid(row=9, column=1)
    pstrong_entry.grid(row=9, column=2)
    pstrong_button.grid(row=10, column=2, padx=10, pady=10)

    # Button for changing the time until recovery from a strong case
    strongrec_label = tkinter.Label(Advsettings, text='Strong recovery, default = (21, 42)')
    strongrec_entry = tkinter.Entry (Advsettings) 
    def change_strongrec ():  
        global setstrong_recovery
        x6 = strongrec_entry.get()
        setstrong_recovery = str(x6)
        print(setstrong_recovery)
    strongrec_button = Button(Advsettings, text='Change strong recovery time', command=change_strongrec)

    strongrec_label.grid(row=11, column=1)
    strongrec_entry.grid(row=11, column=2)
    strongrec_button.grid(row=12, column=2, padx=10, pady=10)

    # Button for changing the time until death due to a strong case
    dstrong_label = tkinter.Label(Advsettings, text='Strong death, default = (14, 56)')
    dstrong_entry = tkinter.Entry (Advsettings) 
    def change_dstrong ():  
        global setstrong_death
        x7 = dstrong_entry.get()
        setstrong_death = str(x7)
        print(setstrong_death)
    dstrong_button = Button(Advsettings, text='Change strong death time', command=change_dstrong)

    dstrong_label.grid(row=13, column=1)
    dstrong_entry.grid(row=13, column=2)
    dstrong_button.grid(row=14, column=2, padx=10, pady=10)

    # Button for changing the fatality rate
    frate_label = tkinter.Label(Advsettings, text='Fatality rate, default = 0.034')
    frate_entry = tkinter.Entry (Advsettings) 
    def change_frate ():  
        global setfatality_rate
        x8 = frate_entry.get()
        setfatality_rate = str(x8)
        print(setfatality_rate)
    frate_button = Button(Advsettings, text='Change fatality rate', command=change_frate)

    frate_label.grid(row=15, column=1)
    frate_entry.grid(row=15, column=2)
    frate_button.grid(row=16, column=2, padx=10, pady=10)

    # Button for changing the serial interval
    serialint_label = tkinter.Label(Advsettings, text='Serial interval, default = 7')
    serialint_entry = tkinter.Entry (Advsettings) 
    def change_serialint ():  
        global setserial_interval
        x9 = serialint_entry.get()
        setserial_interval = str(x9)
        print(setserial_interval)
    serialint_button = Button(Advsettings, text='Change serial interval', command=change_serialint)

    serialint_label.grid(row=17, column=1)
    serialint_entry.grid(row=17, column=2)
    serialint_button.grid(row=18, column=2, padx=10, pady=10)

    # closes the advanced settings menu
    def advClose():
        Advsettings.destroy()

    exit_button = Button(Advsettings, text="Return to main menu", command=advClose)
    exit_button.grid(row=20, column=2, padx=10, pady=10)

def Close():
    startscreen.destroy()

exit_button = Button(startscreen, text="Start Simulation", command=Close)
exit_button.pack(pady=20)
 
### Volatile advanced settings for changing variables
# May cause issues 
varbtn = Button(startscreen, text ="Advanced settings", command = openAdvsettings)
varbtn.pack(pady=20)


def opencreditsb():

    creditsb = Toplevel(startscreen)
 
    creditsb.title("Credits")
 
    creditsb.geometry("400x200")

    credittext = Label(creditsb, text="Made by Alex Soo, some code borrowed from kiteco")
    credittext.pack(pady=20)

    def credclose():
        creditsb.destroy()
    
    exit_buttoncred = Button(creditsb, text="Return to main menu", command=credclose)
    exit_buttoncred.pack(pady=20)

creditbtn = Button(startscreen, text="Credits", command=opencreditsb)
creditbtn.pack(pady=20)


startscreen.mainloop()


GREY = (0.75, 0.75, 0.75)   # Healthy
RED = (1, 0, 0)    # Infected
GREEN = (0, 1, 0)   # Recovered
BLACK = (0, 0, 0)   # Dead

#print(setr0)
#print(setincubation)
#print(setweak_recovery)
#print(setpercent_strong)
#print(setstrong_recovery)
#print(setstrong_death)
#print(setfatality_rate)
#print(setserial_interval)

#try using buttons to change setr0, hopefully that works

Covid_Settings = {
    "r0": float(setr0),
    "incubation": setincubation,
    "percent_weak": float(setpercent_weak),
    "weak_recovery": setweak_recovery,
    "percent_strong": float(setpercent_strong),
    "strong_recovery": setstrong_recovery,
    "strong_death": setstrong_death,
    "fatality_rate": float(setfatality_rate),
    "serial_interval": setserial_interval
}

day_graph = []
infect_graph = []


class Virus():
    def __init__(self, params):
        # create visual
        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(111, projection="polar")
        self.axes.grid(False)
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])
        self.axes.set_ylim(0, 1)

        # create text
        self.day_text = self.axes.annotate(
            "Day 0", xy=[np.pi / 2, 1], ha="center", va="bottom")
        self.infected_text = self.axes.annotate(
            "Infected: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=RED)
        self.deaths_text = self.axes.annotate(
            "\nDeaths: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=BLACK)
        self.recovered_text = self.axes.annotate(
            "\n\nRecovered: 0", xy=[3 * np.pi / 2, 1], ha="center", va="top", color=GREEN)

        # create variables
        self.day = 0
        self.total_infected = 0
        self.num_currently_infected = 0
        self.num_recovered = 0
        self.num_deaths = 0
        self.r0 = params["r0"]
        self.percent_weak = params["percent_weak"]
        self.percent_strong = params["percent_strong"]
        self.fatality_rate = params["fatality_rate"]
        self.serial_interval = params["serial_interval"]

        self.weak_fast = params["incubation"] + params["weak_recovery"][0]
        #self.weak_fast = float(self.weak_fast)
        self.weak_slow = params["incubation"] + params["weak_recovery"][1]
        self.strong_fast = params["incubation"] + params["strong_recovery"][0]
        self.strong_slow = params["incubation"] + params["strong_recovery"][1]
        self.death_fast = params["incubation"] + params["strong_death"][0]
        self.death_slow = params["incubation"] + params["strong_death"][1]

        self.weak = {i: {"thetas": [], "rs": []} for i in range(self.weak_fast, 365)}
        self.strong = {
            "recovery": {i: {"thetas": [], "rs": []} for i in range(self.strong_fast, 365)},
            "death": {i: {"thetas": [], "rs": []} for i in range(self.death_fast, 365)}
        }

        self.affected_before = 0
        self.affected_after = 1

        self.starting_population()

        """
        The function `starting_population` creates a population of 4200 people, and assigns the first
        person to be infected
        """
    def starting_population(self):
        population = 4200
        self.num_currently_infected = 1
        self.total_infected = 1
        indices = np.arange(0, population) + 0.5
        self.thetas = np.pi * (1 + 5**0.5) * indices
        self.rs = np.sqrt(indices / population)
        self.plot = self.axes.scatter(self.thetas, self.rs, s=5, color=GREY)
        # assign the middle person to be patient zero
        self.axes.scatter(self.thetas[0], self.rs[0], s=5, color=RED)
        self.weak[self.weak_fast]["thetas"].append(self.thetas[0])
        self.weak[self.weak_fast]["rs"].append(self.rs[0])


    def spread_virus(self, i):
        self.affected_before = self.affected_after
        if self.day % self.serial_interval == 0 and self.affected_before < 4200:
            self.num_new_infected = round(self.r0 * self.total_infected)
            self.affected_after += round(self.num_new_infected * 1.1)
            if self.affected_after > 4200:
                self.num_new_infected = round((4200 - self.affected_before) * 0.9)
                self.affected_after = 4200
            self.num_currently_infected += self.num_new_infected
            self.total_infected += self.num_new_infected
            self.new_infected_indices = list(
                np.random.choice(
                    range(self.affected_before, self.affected_after),
                    self.num_new_infected,
                    replace=False))
            thetas = [self.thetas[i] for i in self.new_infected_indices]
            rs = [self.rs[i] for i in self.new_infected_indices]
            self.anim.event_source.stop()
            if len(self.new_infected_indices) > 24:
                size_list = round(len(self.new_infected_indices) / 24)
                theta_chunks = list(self.chunks(thetas, size_list))
                r_chunks = list(self.chunks(rs, size_list))
                self.anim2 = ani.FuncAnimation(
                    self.fig,
                    self.one_by_one,
                    interval=50,
                    frames=len(theta_chunks),
                    fargs=(theta_chunks, r_chunks, RED))
            else:
                self.anim2 = ani.FuncAnimation(
                    self.fig,
                    self.one_by_one,
                    interval=50,
                    frames=len(thetas),
                    fargs=(thetas, rs, RED))
            self.assign_symptoms()

        self.day += 1

        self.update_status()
        self.update_text()

        """
        It takes in the current index, the thetas and rs, and the color, and plots the point at the
        current index
        
        :param i: the index of the current point
        :param thetas: the list of theta values
        :param rs: the radius of the point
        :param color: The color of the points
        """
    def one_by_one(self, i, thetas, rs, color):
        self.axes.scatter(thetas[i], rs[i], s=5, color=color)
        if i == (len(thetas) - 1):
            self.anim2.event_source.stop()
            self.anim.event_source.start()


    def chunks(self, a_list, n):
        for i in range(0, len(a_list), n):
            yield a_list[i:i + n]


    """
        We randomly assign a subset of the newly infected to have weak symptoms, and the rest to have
        strong symptoms. 
        
        We then randomly assign a recovery or death day to each of the newly infected. 
        
        The recovery and death days are randomly chosen from a range of days. 
        
        The range of days is determined by the fast and slow recovery/death days. 
        
        The fast and slow recovery/death days are determined by the weak_fast, weak_slow, strong_fast,
        strong_slow, death_fast, and death_slow parameters. 
        
        The fast and slow recovery/death days are randomly chosen from a range of days. 
        
        The range of days is determined by the fast and slow recovery/death days. 
        
        The fast and slow recovery/death days are determined by the weak_fast, weak_slow, strong_fast,
        strong_slow, death_fast, and death_slow parameters
        """
    def assign_symptoms(self):
        num_weak = round(self.percent_weak * self.num_new_infected)
        num_strong = round(self.percent_strong * self.num_new_infected)
        # choose random subset of newly infected to have weak symptoms
        self.weak_indices = np.random.choice(self.new_infected_indices, num_weak, replace=False)
        # assign the rest strong symptoms, either resulting in recovery or death
        remaining_indices = [i for i in self.new_infected_indices if i not in self.weak_indices]
        percent_strong_recovery = 1 - (self.fatality_rate / self.percent_strong)
        num_strong_recovery = round(percent_strong_recovery * num_strong)
        self.strong_indices = []
        self.death_indices = []
        if remaining_indices:
            self.strong_indices = np.random.choice(remaining_indices, num_strong_recovery, replace=False)
            self.death_indices = [i for i in remaining_indices if i not in self.strong_indices]

        # assign recovery/death day
        low = self.day + self.weak_fast
        high = self.day + self.weak_slow
        for weak in self.weak_indices:
            recovery_day = np.random.randint(low, high)
            weak_theta = self.thetas[weak]
            weak_r = self.rs[weak]
            self.weak[recovery_day]["thetas"].append(weak_theta)
            self.weak[recovery_day]["rs"].append(weak_r)
        low = self.day + self.strong_fast
        high = self.day + self.strong_slow
        for recovery in self.strong_indices:
            recovery_day = np.random.randint(low, high)
            recovery_theta = self.thetas[recovery]
            recovery_r = self.rs[recovery]
            self.strong["recovery"][recovery_day]["thetas"].append(recovery_theta)
            self.strong["recovery"][recovery_day]["rs"].append(recovery_r)
        low = self.day + self.death_fast
        high = self.day + self.death_slow
        for death in self.death_indices:
            death_day = np.random.randint(low, high)
            death_theta = self.thetas[death]
            death_r = self.rs[death]
            self.strong["death"][death_day]["thetas"].append(death_theta)
            self.strong["death"][death_day]["rs"].append(death_r)

    """
        If the day is greater than the day that the weak cases are supposed to recover, then plot the
        weak cases as green(recovered). If the day is greater than the day that the strong cases are supposed to
        recover, then plot the strong cases as green(recovered). If the day is greater than the day that the strong
        cases are supposed to die, then plot the strong cases as black(dead)
        """
    def update_status(self):
        if self.day >= self.weak_fast:
            weak_thetas = self.weak[self.day]["thetas"]
            weak_rs = self.weak[self.day]["rs"]
            self.axes.scatter(weak_thetas, weak_rs, s=5, color=GREEN)
            self.num_recovered += len(weak_thetas)
            self.num_currently_infected -= len(weak_thetas)
        if self.day >= self.strong_fast:
            rec_thetas = self.strong["recovery"][self.day]["thetas"]
            rec_rs = self.strong["recovery"][self.day]["rs"]
            self.axes.scatter(rec_thetas, rec_rs, s=5, color=GREEN)
            self.num_recovered += len(rec_thetas)
            self.num_currently_infected -= len(rec_thetas)
        if self.day >= self.death_fast:
            death_thetas = self.strong["death"][self.day]["thetas"]
            death_rs = self.strong["death"][self.day]["rs"]
            self.axes.scatter(death_thetas, death_rs, s=5, color=BLACK)
            self.num_deaths += len(death_thetas)
            self.num_currently_infected -= len(death_thetas)


    def update_text(self):
        self.day_text.set_text("Day {}".format(self.day))
        self.infected_text.set_text("Infected: {}".format(self.num_currently_infected))
        self.deaths_text.set_text("\nDeaths: {}".format(self.num_deaths))
        self.recovered_text.set_text("\n\nRecovered: {}".format(self.num_recovered))

        
        day_graph.append(self.day)
        #print(day_graph)

        infect_graph.append(self.num_currently_infected)
        #print(infect_graph)


    def gen(self):
        while self.num_deaths + self.num_recovered < self.total_infected:
            yield


    def animated(self):
        self.anim = ani.FuncAnimation(
            self.fig,
            self.spread_virus,
            frames=self.gen,
            repeat=True)


def main():
    coronavirus = Virus(Covid_Settings)
    coronavirus.animated()
    plt.show()

def main2():
    x = np.array(day_graph)
    y = np.array(infect_graph)
    plt.plot(x, y)
    #graph2 = plt.plot(day_graph, infect_graph)
    plt.xlabel("Day")
    plt.ylabel("Num. currently infected")
    plt.show()


#def main2():


if __name__ == "__main__":
    main()
    main2()
