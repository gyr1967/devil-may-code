from level1 import Level1 as L1

run = True
current_level_id = 0
do_change_level = True
level_command_center = None

def change_level(level_id):
    match level_id:
        case 0:
            return L1()
        
    # fix to handle error
    return None
 

while run:
    command = input("Bubble bubble, toil and trouble, what should I do: \n")

    # switch to a different level
    if do_change_level:
        level_command_center = change_level(current_level_id)
        if level_command_center is None:
            print("Error: level not found")
            break
        do_change_level = False

    if command.lower() == "exit":
       run = False

    level_command_center.answer_command(command)