import tkinter as tk
from time import sleep
from random import choice

bot_name = 'Wumpus'

m_actions = [
    "Transformers: Rise of the Beasts", "Polis Evo 3", "The Roundup: No Way Out",
    "Fast X", "Red Line", "Guardians of Galaxy Volume 3", "The Dark Knight", 
    "Inception"
]
m_superheroes = [
    "The Flash", "Spiderman Across the Spider-Verse"
]
m_romance = [
    "Elemental", "My Precious", "No Hard Feelings", "Friend Zone",
    "Love Destiny the Movie"
]
m_comedy = [
    "Elemental", "No Hard Feelings", "Rise", "The Innocent ",
    "Sue-On", "The Super Mario Bros. Movie"
]
m_horror = [
    "Jemputan Ke Neraka", "Tasbih Kosong", "The Boogeyman",
    "Haunted Universities 2nd Semester", "The Conjuring 2",
    "Talk to Me", "Sue-On"
]
m_fantasy = [
    "The Little Mermaid", "Takkar"
]
m_historical = [
    "Father & Soldier"
]
m_adventure = [
    "The Three Musketeers: Dartagnan",
    "Indiana Jones And The Dial of Destiny",
    "The Super Mario Bros. Movie"
]
m_thriller = [
    "Faces the Anne", "Talk to Me"
]

n_action = [
    "Extraction 2", "Interceptor", "The Big 4",
    "The Mother"
]
n_romance = [
    "No Limit", "20th Century Girl", "Your Place of Mind",
    "365 Days"
]
n_mystery = [
    "Last Seen Alive", "Unlocked", "The Pale Blue Eye",
    "Luckiest Girl Alive"
]
n_crime = [
    "The Guilty", "Blackout", "The Good Nurse",
    "The Takeover"
]

genra_m = ["action", "superhero", "romance", "comedy", "horror", "fantasy", "historical", "adventure", "thriller"]

Cinema = {
    "action": choice(m_actions),
    "superhero": choice(m_superheroes),
    "romance": choice(m_romance),
    "comedy": choice(m_comedy),
    "horror": choice(m_horror),
    "fantasy": choice(m_fantasy),
    "historical": choice(m_historical),
    "adventure": choice(m_adventure),
    "thriller": choice(m_thriller),
}

genra_n = ["action", "romance", "mystery", "crime"]

Netflix = {
    "action": choice(n_action),
    "romance": choice(n_romance),
    "mystery": choice(n_mystery),
    "crime": choice(n_crime),
}

cinema_check = ["cinema"]
netflix_check = ["netflix", "home", "house"]

greeting_check = ['belo', 'hallo', 'halo', 'konichiwa']
greeting_list = ['halo, how can I help you?', 'hello, how may I assist you?', 'belo, how can I help you?']

watch_request = ["What are you in the mood for?", "Which movie would you like to watch?"]

farewell_check = ["bye", "got to go"]
farewell_list = ["Goodbye!", "Have a great time!", "See you next time!", "Please come again!"]

class ChatBotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wumpus")
        self.geometry("400x400")

        self.ans_box = tk.Text(self, height=20, width=50)
        self.ans_box.pack(pady=10)

        self.enter = tk.Entry(self, width=50)
        self.enter.pack(pady=5)
        self.enter.bind("<Return>", self.process_input)

        self.goodbye_flag = False

    def display_message(self, message):
        self.ans_box.insert(tk.END, message + "\n")
        self.ans_box.see(tk.END)

    def process_input(self, event):
        user_input = self.enter.get()
        self.enter.delete(0, tk.END)

        self.display_message("User: " + user_input)
        user_inputs = user_input.lower().split()
        self.process_user_input(user_inputs)


    def process_user_input(self, user_input):
        for inputs in user_input:
            if inputs in greeting_check:
                self.display_message(bot_name + ": " + choice(greeting_list))

            elif inputs in cinema_check:
                self.display_message(bot_name + ": " + choice(watch_request))
                
                if inputs in genra_m:
                    self.display_message(bot_name + ": "+ Cinema[inputs])

            elif inputs in netflix_check:
                self.display_message(bot_name + ": " + choice(watch_request))

                if inputs in genra_n:
                    self.display_message(bot_name + ": " + Netflix[inputs])

            elif inputs in farewell_check:
                self.display_message(bot_name + ": " + choice(farewell_list))
                self.goodbye_flag = True
                self.quit()

            elif inputs == "":
                self.display_message(bot_name + ": GG invalid input!")

    def get_user_input(self):
        return self.enter.get()

if __name__ == "__main__":
    app = ChatBotApp()
    while not app.goodbye_flag:
        app.update()
    sleep(2)
    app.destroy()
