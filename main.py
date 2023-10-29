import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer
from level1 import Level1 as L1
from level2 import Level2 as L2
from level3 import Level3 as L3
from level4 import Level4 as L4
from level5 import Level5 as L5

# Create the main application window
root = tk.Tk()
root.title("Image, Text Entry, and Text Box")

mixer.init()
mixer.music.set_volume(10)
mixer.music.load("battletheme.mp3") 
mixer.music.play(loops=10)

class Game:
    def __init__(self):
        self.run = True
        self.current_level_id = 1
        self.current_level = L1()
        self.game_state = "Questioning"
        self.current_question = 0
        self.max_questions = 2
        self.battle_outcome = None

    def progress_level(self):
        self.current_level_id += 1
        if self.current_level_id == 1:
            self.current_level = L1()
        elif self.current_level_id == 2:
            self.current_level = L2()
        elif self.current_level_id == 3:
            self.current_level = L3()
        elif self.current_level_id == 4:
            self.current_level = L4()
        elif self.current_level_id == 5:
            self.current_level = L5()
        else:
            return False
        return True
    
    def get_output(self, text):
        if self.game_state == "Questioning":
            response = self.current_level.answer_command(text)
            response += self.increment_question()
        elif self.game_state == "name_guessing":
            response = self.current_level.guess_name(text)
            response += "\n What is the demon's weakness:"
            self.game_state = "weakness_guessing"
        elif self.game_state == "weakness_guessing":
            response = self.current_level.guess_weakness(text)
            self.battle_outcome = self.current_level.fight_outcome()
            response += f"\n{'You won' if self.battle_outcome else 'You lost'}"
            response += self.change_level()
        else:
            print("ruh roh raggy!")
            return None
        return response
    
    def change_level(self):
        if self.battle_outcome:
            continue_game = self.progress_level()
            if continue_game:
                self.game_state = "Questioning"
                self.current_question = 0
                self.progress_image()
                return "\nYou enter the next room. A new demon is standing in front of you."
            self.game_state = "won"
            return "\nYou escaped"
        self.game_state = "died"
        return "\nGame Over"
        
    
    def get_current_level(self):
        return self.current_level
    
    def get_current_level_id(self):
        return self.current_level_id
    
    def set_current_level_id(self, level_id):
        self.current_level_id = level_id
        self.progress_level()
        
    def get_run(self):
        return self.run
    
    def set_run(self, run):
        self.run = run

    def get_game_state(self):
        return self.game_state

    def increment_question(self):
        self.current_question += 1
        self.update_question_counter_box()
        if self.current_question >= self.max_questions:
            self.game_state = "name_guessing"
            return "\n<<You have run out of questions. The battle has begun.>>\nWhat is the demon's name:"
        return ""
        
    def fight_on (self):
        self.game_state = "name_guessing"
        text_box.delete(1.0, "end")  
        text_box.insert("insert", f"What is the demon's name:")
        return "\nThe battle has begun.\nWhat is the demon's name:"
    
    def progress_image(self):
        if self.current_level_id == 1:
            image = Image.open("abaddon.png")
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)
            image_label.configure(image=image)
            image_label.image = image
        elif self.current_level_id == 2:
            image = Image.open("kirito.png")
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)
            image_label.configure(image=image)
            image_label.image = image
        elif self.current_level_id == 3:
            image = Image.open("kefka.png")
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)
            image_label.configure(image=image)
            image_label.image = image
        elif self.current_level_id == 4:
            image = Image.open("fazbear.png")
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)
            image_label.configure(image=image)
            image_label.image = image
        elif self.current_level_id == 5:
            image = Image.open("trickster.png")
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)
            image_label.configure(image=image)
            image_label.image = image
        else:
            return False
        return True
    
    def update_question_counter_box(self):
        if self.current_question+1 >= self.max_questions:
            question_counter.configure(text=f"Question {self.current_question+1} of {self.max_questions}")

game = Game()

# Create a function to update the text box
def update_text():
    text = entry.get()
    entry.delete(0, "end")  # Clear the existing text
    text_box.delete(1.0, "end")  # Clear the existing text
    response = game.get_output(text)
    text_box.insert("insert", f"{response}")

# Load the image
image = Image.open("abaddon.png")
image = image.resize((200, 200))
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = ttk.Label(root, image=image)
image_label.pack()

# Create a text entry box
entry = ttk.Entry(root)
entry.pack()

# Create a text box
text_box = tk.Text(root, height=10, width=40)
text_box.pack()
text_box.insert("insert", f"""You enter a spooky demon mansion. You see a demon in front of you. You must ask it questions to find out its name and weakness.""")

#  create a counter that keeps track of the number of questions asked
question_counter = ttk.Label(root, text=f"Question {game.current_question+1} of {game.max_questions}")
question_counter.pack()

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=update_text)
submit_button.pack()

#Create a fight button
fight_button = ttk.Button(root, text="Fight", command=game.fight_on)
fight_button.pack()


# Start the tkinter main loop
root.mainloop()
