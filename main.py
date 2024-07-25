# imports
import time
import function as f
import story.chapter0 as c0
import story.chapter1 as c1
import story.chapter2 as c2
import story.chapter3 as c3
import story.chapter4 as c4
from story.settings import game_settings
import sys
import io
from termcolor import colored

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')


# clear screen

f.clearScreen()

# welcome massage

print(colored("░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░", "light_red"))
print(colored("░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗", "light_red"))
print(colored("░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║", "light_red"))
print(colored("░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║", "light_red"))
print(colored("░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝", "light_red"))
print(colored("░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░", "light_red"))

print(colored("░█████╗░██╗░░██╗███╗░░░███╗███████╗██████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗", "light_yellow"))
print(colored("██╔══██╗██║░░██║████╗░████║██╔════╝██╔══██╗  ██╔════╝░██╔══██╗████╗░████║██╔════╝", "light_yellow"))
print(colored("███████║███████║██╔████╔██║█████╗░░██║░░██║  ██║░░██╗░███████║██╔████╔██║█████╗░░", "light_yellow"))
print(colored("██╔══██║██╔══██║██║╚██╔╝██║██╔══╝░░██║░░██║  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░", "light_yellow"))
print(colored("██║░░██║██║░░██║██║░╚═╝░██║███████╗██████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗", "light_yellow"))
print(colored("╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝", "light_yellow"))

print("\n\n\n█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   " + colored("▄▀█ █░█ █▀▄▀█ █▀▀ █▀▄   █▀▄▀█ █▀█ █░█ █▀ ▄▀█", "light_cyan"))
print("█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   " + colored("█▀█ █▀█ █░▀░█ ██▄ █▄▀   █░▀░█ █▄█ █▄█ ▄█ █▀█", "light_cyan"))


time.sleep(3)
print("\n\n\nEnter " + colored("Q", "red") + " to exit ...")
time.sleep(0.5)
print("Press " + colored("Enter", "red") + " key to continue ...")

if input("Enter your choice: ").lower() == "q":
    exit()

f.clearScreen()

# game settings

settings = game_settings()
player_name = colored(settings["name"], "light_green")

time.sleep(2)

total_score = 0


while True:
    f.clearScreen()
    f.text_animation("Press Enter key to start ...")
    input()
    f.clearScreen()

    
    # story title

    print("░█▀▀█ █▀▀▄ ▀█░█▀ █▀▀ █▀▀▄ ▀▀█▀▀ █░░█ █▀▀█ █▀▀ 　 ░▀░ █▀▀▄ 　 ▀▀█▀▀ █░░█ █▀▀ 　 ▒█░▄▀ ░▀░ █▀▀▄ █▀▀▀ █▀▀▄ █▀▀█ █▀▄▀█ ")
    print("▒█▄▄█ █░░█ ░█▄█░ █▀▀ █░░█ ░░█░░ █░░█ █▄▄▀ █▀▀ 　 ▀█▀ █░░█ 　 ░░█░░ █▀▀█ █▀▀ 　 ▒█▀▄░ ▀█▀ █░░█ █░▀█ █░░█ █░░█ █░▀░█ ")
    print("▒█░▒█ ▀▀▀░ ░░▀░░ ▀▀▀ ▀░░▀ ░░▀░░ ░▀▀▀ ▀░▀▀ ▀▀▀ 　 ▀▀▀ ▀░░▀ 　 ░░▀░░ ▀░░▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▀░░▀ ▀▀▀▀ ▀▀▀░ ▀▀▀▀ ▀░░░▀ \n")
    print("█▀▀█ █▀▀ 　 ▒█░░▒█ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ █▀▀ ")
    print("█░░█ █▀▀ 　 ▒█▒█▒█ █░░█ █░░█ █░░█ █▀▀ █▄▄▀ ▀▀█ ")
    print("▀▀▀▀ ▀░░ 　 ▒█▄▀▄█ ▀▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀ ▀▀▀")


    c0.chapter0(player_name)
    # chapter 1

    chapter1_decide = c1.chapter1(player_name)
    

    # chapter 2


    
    print("░█▀▀█ █──█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀█ 　 █▀█ ")
    print("░█─── █▀▀█ █▄▄█ █──█ ──█── █▀▀ █▄▄▀ 　 ─▄▀ ")
    print("░█▄▄█ ▀──▀ ▀──▀ █▀▀▀ ──▀── ▀▀▀ ▀─▀▀ 　 █▄▄")
    time.sleep(1)


    # decide 1

    chapter2_decide = 0
    treasure_password = None
    lucky_thing = None
    luck = None
    # if player decide to take the paved road

    if chapter1_decide == 1:
        luck = c1.paved_road_walking(player_name)
        f.continue_key()
        chapter2_decide = c2.paved_road(player_name)
        total_score += 200 

    # if player decide to take the narrow and bumpy path`` 

    else:
        luck = c1.narrow_path_walking(player_name)
        f.continue_key()
        chapter1_decide = c2.narrow_path(player_name)
        total_score += 100

    treasure_password = luck["treasure_password"]
    lucky_thing = luck["lucky_thing"]

    f.continue_key()

    print("█▀▀ █──█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀█ 　 █▀▀█")
    print("█── █▀▀█ █▄▄█ █──█ ──█── █▀▀ █▄▄▀ 　 ──▀▄")
    print("▀▀▀ ▀──▀ ▀──▀ █▀▀▀ ──▀── ▀▀▀ ▀─▀▀ 　 █▄▄█")

    time.sleep(1)

    # chapter 3

    chapter3_decide = 0

    # if player decide to help old lady

    if chapter2_decide == 1:
        chapter3_decide = c3.helpedLady(player_name)
        total_score += 200

    # if player decide to not help old lady

    elif chapter2_decide == 2:
        chapter3_decide = c3.nHelpedLady(player_name)
        total_score -= 50
    
    # if player decide to help animal

    elif chapter2_decide == 3:
        chapter3_decide = c3.helpdAnimal(player_name)
        total_score += 100
    # if player decide to not help animal

    else :
        chapter3_decide = c3.nHelpedAnimal(player_name)
        total_score -= 50

    f.text_animation("\n\nPress Enter key to continue ...")
    input()
    f.clearScreen()



    print("█▀▀ █──█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀█ 　 ─█▀█─")
    print("█── █▀▀█ █▄▄█ █──█ ──█── █▀▀ █▄▄▀ 　 █▄▄█▄")
    print("▀▀▀ ▀──▀ ▀──▀ █▀▀▀ ──▀── ▀▀▀ ▀─▀▀ 　 ───█─")

    time.sleep(1)

    # if player used the magic wand

    if chapter3_decide == 1:
        c4.using_magic_wand(player_name, lucky_thing, treasure_password)
        total_score += 100

    # if player kept the magic wand

    elif chapter3_decide == 2:
        c4.keeping_magic_wand(player_name)
        total_score += 10

    # if player choose to try to find his way using listing

    elif chapter3_decide == 3:
        c4.trying_to_find_way(player_name)
        total_score -= 30

    # if player decide to wait until fog disappears

    elif chapter3_decide == 4:
        c4.wait_the_fog(player_name, lucky_thing, treasure_password)
        total_score += 65

    # if player wants to follow the animal

    elif chapter3_decide == 5:
        c4.follow_animal(player_name, lucky_thing, treasure_password)
        total_score += 100

    # if player decide to continue alone

    elif chapter3_decide == 6:
        c4.continue_alone(player_name)
        total_score -= 50

    # if player wants to talk to the trees

    elif chapter3_decide == 7:
        c4.talking_trees(player_name, lucky_thing, treasure_password)
        total_score += 30

    # if player runs away

    elif chapter3_decide == 8:
        c4.running_away(player_name)
        total_score += 25

    f.text_animation("Your score is : " + str(total_score))

    time.sleep(2)

    f.text_animation("Wanna play again ?")

    while True:
        inp = input("y/n: ").lower().strip()
        if inp == "y":
            f.clearScreen()
            break
        elif inp == "n":
            exit()
        else:
            print("Please enter valid input")