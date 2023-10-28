from level1 import Level1 as L1
from level2 import Level2 as L2
from pygame import mixer
import sys
import pygame
from button import Button

pygame.init()
pygame.display.set_caption("Devil May Code")
screen = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

mixer.init()
mixer.music.set_volume(10)

run = True
current_level_id = 1
do_change_level = True
level_command_center = None
user_question = ""
response = "t"
final_question = None
input_active = True
question_submitted = False

gui_font = pygame.font.Font(None,30)

input_rect = pygame.Rect(200,200,140,40)
text_surface = gui_font.render(user_question,True,(255,255,255))


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


buttons = []
button2 = Button(screen, gui_font, 'Submit',200,40,(100,250),5)
button2.command = (lambda: print("Submit question to demon"))
buttons.append(button2)

fight_in_progress = False

while run:
    # switch to a different level
    if do_change_level:
        level_command_center = change_level(current_level_id)
        if level_command_center is None:
            print("Error: level not found")
            break
        play_sound("battletheme.mp3", loop=10)
        do_change_level = False

    if fight_in_progress and fight_stage == 1:
        print("What is the demons name:")
        fight_stage += 1

    if fight_in_progress and fight_stage == 3:
        print("What is the demons name:")
        fight_stage += 1
    
    if question_submitted:
        currentQuestions = level_command_center.getCurrentQuestions()
        maxQuestions = level_command_center.getMaxQuestions()
        response = level_command_center.answer_command(final_question)
        print(f"Demon: {response}")
        print(f"You have {maxQuestions-currentQuestions} questions left")
        print("You: ") if currentQuestions < maxQuestions else print("")
        if currentQuestions >= maxQuestions and fight_in_progress == False:
            level_command_center.init_battle()
            print("You have run out of questions, the time for battle has come!")
            fight_in_progress = True
            fight_stage = 1
        
        if fight_in_progress and fight_stage == 2:
            response = level_command_center.guess_name(final_question)
            fight_stage += 1

        if fight_in_progress and fight_stage == 3:
            response = level_command_center.guess_name(final_question)
            fight_stage += 1
            fight_in_progress = False

        if currentQuestions >= maxQuestions and fight_in_progress == False:
            is_victory = level_command_center.fight_outcome()
            if is_victory:
                play_sound("ffvictory.mp3")
                do_change_level = True
                current_level_id += 1
                print("\n-------------------\nLevel Up!\n-------------------\n")
                question_submitted = False
                continue
            else:
                play_sound("ffvictory.mp3")
                question_submitted = False
                break
        question_submitted = False
    
    for b in buttons:
        b.draw()
    
    demon_text = gui_font.render(response, True, (0, 255, 0), (0, 0, 128))
    demon_textRect = demon_text.get_rect()
    screen.blit(demon_text, demon_textRect)
    
    # game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            user_question = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if question_submitted == False and event.key == pygame.K_RETURN:
                final_question = user_question
                user_question = ""
                question_submitted = True

            elif event.key == pygame.K_BACKSPACE:
                user_question =  user_question[:-1]
            else:
                user_question += event.unicode
    text_surface = gui_font.render(user_question,True,(255,255,255))
    input_rect.w=max(100,text_surface.get_width() + 10)
    
    pygame.display.update()
    screen.blit(background, (0, 0))
    screen.blit(text_surface,(input_rect.x + 5, input_rect.y +5))
    input_rect.w=max(100,text_surface.get_width() + 10)

