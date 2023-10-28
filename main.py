from level1 import Level1 as L1
from level2 import Level2 as L2
from pygame import mixer
mixer.init()
mixer.music.set_volume(10)

run = True
current_level_id = 1
do_change_level = True
level_command_center = None

def change_level(level_id):
    if level_id == 1:
        return L1()
    elif level_id == 2:
        return L2()
    return None
 
def play_sound(path, loop=1):
    mixer.music.fadeout(1)
    mixer.music.load(path) 
    mixer.music.play(loops=loop)

while run:
    # switch to a different level
    if do_change_level:
        level_command_center = change_level(current_level_id)
        if level_command_center is None:
            print("Error: level not found")
            break
        play_sound("battletheme.mp3", loop=10)
        do_change_level = False
    
    command = input()


    if command.lower() == "exit":
       run = False
    currentQuestions = level_command_center.getCurrentQuestions()
    maxQuestions = level_command_center.getMaxQuestions()
    response = level_command_center.answer_command(command)
    print(f"Demon: {response}")
    print(f"You have {maxQuestions-currentQuestions} questions left")
    print("You: ") if currentQuestions < maxQuestions else print("")
    if currentQuestions >= maxQuestions:
        print("You have run out of questions, the time for battle has come!")
        is_victory = level_command_center.init_battle()
        if is_victory:
            play_sound("ffvictory.mp3")
            do_change_level = True
            current_level_id += 1
            print("\n-------------------\n-------------------\n")
            print("Level up!")
            continue
        else:
            play_sound("ffvictory.mp3")
            break