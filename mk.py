import tkinter as tk
from random import choice

bot_name = 'Wumpus'

cinema_check = ["Cinema"]
netflix_check = ["netflix", "home", "house"]
m_actions = [
    "Transformers: Rise of the Beasts", "Polis Evo 3", "The Roundup: No Way Out",
    "Fast X", "Fast X", "Red Line", "Guardians of Galaxy Volume 3",
    "The Dark Knight", "Inception"
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
###############################################################################################################################

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
genra_s = ["action", "superhero", "romance", "comedy", "horror", "fantasy", "historical", "adventure", "thriller"]

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

Netflix = {
    "action": choice(n_action),
    "romance": choice(n_romance),
    "mystery": choice(n_mystery),
    "crime": choice(n_crime),
}
####################################################################################################################################
greeting_check = ['belo', 'hallo', 'halo', 'konichiwa']
greeting_list = ['halo, how can I help you?', 'hello, how may I assist you?']

farewell_check = ["bye", "got to go"]
farewell_list = ["Goodbye!", "Have a great time!", "See you next time!", "Please come again!"]

watch_request = ["What are you in the mood for?", "Which movie would you like to watch?"]

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

        user_inputs = user_input.lower().split()
        self.greetings(user_inputs)
        self.farewell(user_inputs)
        self.cinema_movie(user_inputs)
        self.netflix_movie(user_inputs)
        self.not_in(user_inputs)
        
    def greetings(self, user_input):
        for inputs in user_input:
            if inputs in greeting_check:
                self.display_message(bot_name + ": " + choice(greeting_list))

    def farewell(self, user_input):
        for inputs in user_input:
            if inputs in farewell_check:
                self.display_message(bot_name + ": " + choice(farewell_list))
                self.goodbye_flag = True
        self.quit()

    def cinema_movie(self, user_input):
        for inputs in user_input:
            if inputs in cinema_check:
                self.display_message(bot_name + ": " + choice(watch_request))
                user_input = self.get_user_input()
                user_input = user_input.lower().split()
        for inputs in user_input:
            if inputs in genra_s:
                self.display_message(bot_name + ": " + "cinema: " + Cinema[inputs])

    def netflix_movie(self, user_input):
        for inputs in user_input:
            if inputs in netflix_check:
                self.display_message(bot_name + ": " + choice(watch_request))
                user_input = self.get_user_input()
                user_input = user_input.lower().split()
        for inputs in user_input:
            if inputs in genra_s:
                self.display_message(bot_name + ": " + "netflix: " + Netflix[inputs])

    def not_in(self, user_input):
        for inputs in user_input:
            if inputs in (netflix_check or cinema_check or greeting_check or farewell_check):
                self.display_message(bot_name + ": Invalid input!")

    # def check_movie(self, user_input):
    #     for inputs in user_input:
    #         if inputs in cinema_check:
    #             self.display_message(bot_name + ": " + choice(watch_request))
    #             user_input = self.get_user_input()
    #             user_input = user_input.lower().split()
    #             self.display_message(bot_name + ": " + "Cinema:" + Cinema[inputs])

    #         if inputs in netflix_check:
    #             self.display_message(bot_name + ": " + choice(watch_request))
    #             user_input = self.get_user_input()
    #             user_input = user_input.lower().split()
    #             self.display_message(bot_name + ": " + "netflix:" + Netflix[inputs])

    #         if inputs in (netflix_check or cinema_check or greeting_check or farewell_check):
    #                 self.display_message(bot_name + ": Invalid input!")

    def get_user_input(self):
        return self.entry.get()


if __name__ == "__main__":
    app = ChatBotApp()
    while not app.goodbye_flag:
        app.update()
    app.destroy()
