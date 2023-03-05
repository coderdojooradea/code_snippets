import random
import tkinter as tk

#definim dictionarul pentru culori
COLORS = {
    0 : "red",
    1 : "blue",
    2 : "green",
    3 : "yellow",
    4 : "cyan",
    5 : "magenta"
}

GUESSES = {
    0 : "white",
    1 : "white",
    2 : "gray",
    3 : "black"
}


# lista pentru pozitii in joc
POSITIONS = [0, 1, 2, 3]
    

def create_gui():
    # create color buttons
    for i in range(6):
        color = COLORS[i]
        button = tk.Button(window, bg=color, command=lambda c=color: choose_color(c))
        button.place(x=i*70+20, y=350, width = 60, height = 60)
    # create guess buttons
    for i in range(4):
        button = tk.Button(window, text="", command=lambda x=i: make_guess(x))
        button.place(x=i*100+50, y=50, width = 60, height = 60)
    # create submit button
    button = tk.Button(window, text="Submit", command=check_guess)
    button.place(x=150, y=300, width = 100, height = 50)
    for i in range(4):
        button = tk.Button(window, command=lambda x=i: show_result(x))
        button.place(x=i*100+50, y=500, width = 10, height = 50)



def choose_color(color):
    if len(colors) <4:
        colors.append(color)
        button = tk.Button(window, bg=color)
        button.place(x= len(colors)*100-50, y=120, width = 50, height = 50)

def generate_code():
    code = []
    for i in range(4):
        code.append(random.randint(0,5))
    return code

def make_guess(position):
    if len(colors) <4:
        color = colors[position]
        button = tk.Button(window, bg=color)
        button.place(x= position*100+50, y=50, width = 50, height = 50)

def show_result(position):
    if len(colors) <4:
        color = status[position]
        button = tk.Button(window, bg=color)
        button.place(x= position*100+50, y=50, width = 50, height = 50)


def check_guess():
    global attemps_left, status
    if len(colors) == 4:
        attemps_left -= 1
        # modificam label incercari
        
        guess = [list(COLORS.values()).index(c) for c in colors]
        correct_positions, correct_colors = check_guess_result(guess)
        if correct_positions == 4:
            print("You won")
        elif attemps_left == 0:
            print("Game over. The code was: {}".format(code))
        else:
            colors.clear()
            for i in range(4):
                button = tk.Button(window, bg=GUESSES[status[i]], command=lambda x=i: make_guess(x))
                button.place(x=i*100+50, y=50, width=60, height=60)
            print(status)
            status = [0,0,0,0]

def check_guess_result(guess):
    global status
    correct_positions = 0
    correct_colors = 0
    for i in range(4):
        if guess[i] in code:
            correct_colors += 1
            status[i] = 2
        if guess[i] == code[i]:
            correct_positions +=1
            status[i]= 3
        if guess[i] not in code:
            status[i] = 0
    return correct_positions, correct_colors


attemps_left = 10
colors = []
code = generate_code()
status = [0,0,0,0]
print(code)

window = tk.Tk()
window.title("Mastermind")
window.geometry("600x400")
create_gui()
window.mainloop()
print(colors)
