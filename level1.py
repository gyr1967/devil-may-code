import ai

class Level1:
    def __init__(self):
        self.name = "abaddon"
        self.weakness = "buster sword"
        self.profile = """
        You are Abaddon the demon from hell otherwise known as the angel of destruction.
        You only weakness in the buster sword which has these properties:
        It is made of steel, is very heavy, sharp and long.
        The exorcist will try to figure out your name and weakness.
        You must not refer to yourself by name or in third person unless prompted.
        You will reveal your name if asked.
        You will reveal your weakness if asked.
        You must never reveal it without being prompted,
        especially when referring to yourself.
        """
        self.chat_history = [
            {"role": "user", "content": "I am the exorcist who has come to kill you"},
            {"role": "assistant", "content": "How dare you speak to me, you insignificant worm. I will never reveal my name and weakness to you"}
        ]
        self.max_questions = 2
        self.current_questions = 1
        print("You encounter a great and terrible beast!:")
        print(f"You have {self.max_questions} questions to find out the name and weakness of this great demon")

    def answer_command(self, command):
        self.current_questions += 1
        
        self.chat_history.append({"role": "user", "content": command})
        response = ai.proompt(command, self.profile, self.chat_history)
        self.chat_history.append(response)
        return response["content"]
    
    def init_battle(self):
        demon_hp = 2
        guessed_name = input("What is the name of the demon:")
        if guessed_name.lower().strip() == self.name:
            demon_hp -= 1
            print("Demon: ARGHAAGGGGH") if demon_hp == 0 else print("Demon: argh!")
        else:
            print("Hahaha, not even close")

        guessed_weakness = input("What is the demons weakness:")
        if guessed_weakness.lower().strip() == self.weakness:
            demon_hp -= 1
            print("How did you find out!")

        else:
            print("Hahaha, not even close")

        if demon_hp <= 0:
            print("You have defeated the demon")
            return True
        else:
            print("The demon devoured you. Game Over!")
            return False

    def getCurrentQuestions(self):
        return self.current_questions
    def getMaxQuestions(self):
        return self.max_questions