from level1 import Level1 as L1
from level2 import Level2 as L2

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
 
while run:
    # switch to a different level
    if do_change_level:
        level_command_center = change_level(current_level_id)
        if level_command_center is None:
            print("Error: level not found")
            break
        do_change_level = False
    
    command = input()


    if command.lower() == "exit":
       run = False
    if level_command_center.getCurrentQuestions() >= level_command_center.getMaxQuestions():
        print("You have run out of questions, the time for battle has come!")
        is_victory = level_command_center.init_battle()
        if is_victory:
           do_change_level = True
           current_level_id += 1
           continue
        else:
            break
    response = level_command_center.answer_command(command)
    print(f"Demon: {response}")
    print("You: ")