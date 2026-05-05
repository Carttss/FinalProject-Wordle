#Carson Everhart
#period 6
#Tkinter Final
#Time Spent: 4 days


#Adding tkinter and random
import tkinter as tk
from tkinter import messagebox
import random
import json
import os

#Adding classes
class Logic:
    def __init__(self):
        self.words = ['climb', 'berry', 'pouch', 'flash', 'exist', 'rhyme', 'stamp', 'magic', 'devil', 'smile', 'chart', 'panic', 'stack', 'wagon', 'cream', 'bread', 'short', 'arrow', 'lunch', 'faith', 'crime', 'truck', 'chain', 'shape', 'chair', 'fancy', 'acute', 'ranch', 'cheap', 'never', 'pitch', 'grain', 'zebra', 'bench', 'legal', 'seven', 'haunt', 'frost', 'diary', 'limit', 'relay', 'river', 'choir', 'plate', 'quilt', 'elect', 'teach', 'quiet', 'sweet', 'greet', 'grasp', 'grass', 'suite', 'nasal', 'kebab', 'about', 'chaos', 'world', 'fence', 'beach', 'upset', 'heavy', 'enter', 'shade', 'bacon', 'needs', 'train', 'spell', 'apply', 'joint', 'badge', 'exact', 'rival', 'forth', 'trunk', 'unify', 'raise', 'coast', 'ridge', 'salon', 'doubt', 'meter', 'watch', 'sneak', 'space', 'these', 'crack', 'mercy', 'sting', 'spice', 'clerk', 'sweat', 'human', 'blood', 'reset', 'twice', 'grade', 'forum', 'trait', 'adopt']
        self.chosen_word = ""
        self.attempts = 0
        self.max_trys = 6
        self.restartgame()
        
    #Resetting game logic
    def restartgame(self):
        self.chosen_word = random.choice(self.words)
        self.attempts = 0
        print(f'The secret word was {self.chosen_word}')
    
    #Checks guess
    def checkattempt(self, guess):
        guess = guess.lower().strip()
        if len(guess) != 5:
            return "Invalid Guess! Please try again! (5 letter words only!)"
        
        self.attempts += 1
        #Begins comparing letters to check whats there or not
        end_result = []
        chosen_letters = list(self.chosen_word)

        #Checks for correct letters throughout the entire word
        for i in range(5):
            if guess[i] == self.chosen_word[i]:
                end_result.append("green")
                chosen_letters[i] = None
            else:
                end_result.append("gray")
        
        #Checks for misplaced letters throughout the entire word
        for i in range(5):
            if end_result[i] == "green": continue
            if guess[i] in chosen_letters:
                end_result[i] = "yellow"
                chosen_letters[chosen_letters.index(guess[i])] = None
        return end_result
#GUI Class Construction
#Creates Base GUI (background, title, etc)

class WGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Wordle - Final Project")
        self.root.configure(bg='#121213')
        #Amount of games played
        self.gamesplayed = tk.IntVar(value=self.load_games_played())
        for i in range(5):
            self.root.columnconfigure(i, weight=1)

        self.logic = Logic()
        self.cells = [[None for _ in range(5)]for _ in range(6)]

        self.header = tk.Label(self.root, text="WORDLE", font=("Helvetica", 36, "bold"), bg='#121213', fg="white", pady=20)
        self.header.grid(row=0, column=0, columnspan=5)
        self.author = tk.Label(self.root, text="By Carson Everhart", font=("Helvetica", 8, "bold"), bg='#121213', fg="white", pady=20)
        self.author.grid(row=0, column=3, columnspan=5)

        self.grid_creation()
        self.create_input()
    def grid_creation(self):
        for r in range(6):
            for c in range(5):
                #Creates Frame for Tkinter
                frame = tk.Frame(self.root, width=62, height=62, highlightbackground="#3a3a3c", highlightthickness=2, bg="#121213")
                frame.grid(row=r+1, column=c, padx=20, pady=20)
                frame.pack_propagate(False)
                label = tk.Label(frame, text="", font=("Helvetica", 30, "bold"), bg="#121213", fg="white")
                label.place(relx=0.5, rely=0.5, anchor="center")
                self.cells[r][c] = label
    
    #Creates input area
    def create_input(self):
        self.prompt_label = tk.Label(self.root, text="Put Guess Here:", font=("Helvetica", 10, "bold"), bg="#121213", fg="white")
        self.prompt_label.grid(row=7,column=0, columnspan=5, pady=(10, 0))
        #Games played text
        self.gamesplayed_label = tk.Label(self.root, text="Games Played: ", font=("Helvetica", 10, "bold"), bg="#121213", fg="white")
        self.gamesplayed_label.grid(row=0, column=0, columnspan=1, pady=(10, 0))
            
        self.gamesplayed_labelvar = tk.Label(self.root, textvariable=self.gamesplayed, font=("Helvetica", 10, "bold"), bg="#121213", fg="white") 
        self.gamesplayed_labelvar.grid(row=0, column=0, columnspan=2, pady=(10, 0))
        #Creates type box that you input guess into
        self.entry = tk.Entry(self.root, font=("Helvetica", 20), justify="center", bg="#3a3a3c", fg="white", insertbackground="white", relief="flat", bd=2)
        self.entry.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        self.entry.bind("<Return>", self.process_guess)
        #Creates submit button (not necessary but good to have)
        Submit = tk.Button(self.root, text="Submit", command=self.process_guess, font=("Helvetica", 12, "bold"), bg="#444444", fg="white")
        Submit.grid(row=8, column=3, columnspan=2, padx=10, pady=10, sticky="ew")
        self.entry.focus_set()
    #Goes through checking system
    def process_guess(self, event=None):
        guess = self.entry.get().lower().strip()
        if len(guess) != 5:
            messagebox.showwarning("Wordle", "Word has be 5 letters! \n Please input a 5 letter word instead!")
            return
        
        feedback = self.logic.checkattempt(guess)

        #updates the colors for wordle letters
        for i in range(5):
            color = self.get_color(feedback[i])
            self.cells[self.logic.attempts-1][i].config(text=guess[i], bg=color)
            self.cells[self.logic.attempts-1][i].master.config(bg=color, highlightbackground=color)
        self.entry.delete(0, tk.END)

        if guess == self.logic.chosen_word:
            #Showing that you won
            messagebox.showinfo("Wordle", f'You did it! You Won! You guessed in {self.logic.attempts}')
            #Adds to "Games Played"
            self.gamesplayed.set(self.gamesplayed.get() + 1)
            self.SaveGames()
            self.root.destroy()
        elif self.logic.attempts == self.logic.max_trys:
            messagebox.showinfo("Wordle", f"Game Over! The Chosen Word was: {self.logic.chosen_word}!")
            self.root.destroy()
        
    def get_color(self, color_name):
        #Fetches colors for respective letter correction
        return {"green": "#6aaa64", "yellow": "#c9b458", "gray": "#787c7e"} [color_name]

    def load_games_played(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "games_played.json")
        
        try:
            with open(path, "r") as file:
                data = json.load(file)
                return data.get("games_played", 0)
        except:
            return 0
    def SaveGames(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "games_played.json")

        with open(path, "w") as file:
            json.dump({"games_played": self.gamesplayed.get()}, file)
            

#Main function, called everything
if __name__ == "__main__":
    root = tk.Tk()
    game = WGUI(root)
    root.mainloop()
