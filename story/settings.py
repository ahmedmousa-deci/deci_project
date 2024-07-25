from termcolor import colored
import function as f
import time
import random


def character_printer(hair_color = None, eye_color = None, scarf_color = None, pants_color = None):
    """
    Print a character representation with different colors.

    Args:
        hair_color (str, optional): The color of the hair. Defaults to None.
        eye_color (str, optional): The color of the eyes. Defaults to None.
        scarf_color (str, optional): The color of the scarf. Defaults to None.
        pants_color (str, optional): The color of the pants. Defaults to None.

    Returns:
        None
    """
    print(colored("    ██████████████", hair_color))
    print(colored("  ██████████████████", hair_color))
    print(colored("  ████████████████████", hair_color))
    print(colored("██████████████████████", hair_color))
    print(colored("████████", hair_color) + colored("██", eye_color) + "░░░░" + colored("██", eye_color) + "░░" + colored("████", hair_color))
    print(colored("██████", hair_color) + "░░" + colored("██", eye_color) + "░░░░" + colored("██", eye_color) + "░░" + colored("████", hair_color))
    print(colored("  ████", hair_color) + "░░░░░░░░░░░░" + colored("██", hair_color))
    print(colored("  ██", hair_color) + "░░░░░░░░░░░░░░" + colored("██", hair_color))
    print(colored("    ██", hair_color) + "░░░░░░░░░░" + colored("████", hair_color))
    print("  ██▒▒" + colored("██████████", scarf_color) + "▒▒▒▒██")
    print("  ██▒▒" + colored("██▓▓▓▓██▓▓", scarf_color) + "▒▒▒▒██")
    print("  ██▒▒" + colored("██", scarf_color) + "▒▒▒▒" + colored("██", scarf_color) + "▒▒▒▒▒▒██")
    print("  ██▒▒" + colored("██", scarf_color) + "▒▒▒▒" + colored("██", scarf_color) + "▒▒▒▒▒▒██")
    print("    ██▒▒▒▒▒▒" + colored("██", scarf_color) + "▒▒▒▒██")
    print("    ██▒▒▒▒" + colored("██", scarf_color) + "▒▒▒▒▒▒██")
    print(colored("      ████████████", pants_color))
    print(colored("      ████████████", pants_color))
    print(colored("      ████    ████", pants_color))
    print(colored("      ████    ████", pants_color))
    print(colored("      ████    ████", pants_color))


def color_choosing(part ,hair, eye, scarf, pants):
    
    # create color var to save it for return
    color = None

    # create list of color choices

    color_list = ["white", "blue", "cyan", "magenta", "green", "yellow", "red"]

    # while loop to keep asking until a valid color is entered

    while True:
        f.clearScreen()
        # if condition for check the part will be printed with the color
        if part == 1:
            character_printer(color, eye, scarf, pants)

        elif part == 2:
            character_printer(hair, color, scarf, pants)

        elif part == 3:
            character_printer(hair, eye, color, pants)

        else:
            character_printer(hair, eye, scarf, color)

        # print color choices

        for i, c in enumerate(color_list):
            print(f"{i + 1}. {c.title()}")
        print("8.Random")
        time.sleep(0.2)
        print("If you are done, Enter")
        time.sleep(0.2)

        # ask for user choice

        while True:
            choice = input("Enter you choice: ").strip()

            if choice == "":
                return color

            if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                color = color_list + [random.choice(color_list)]
                color = color[int(choice) - 1]
                break
            else:
                print("Wrong choice, Try again ...")
                time.sleep(0.5)           



def print_banner():
    """
    print game settings banner
    """
    print("█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀ █▀▀ ▀█▀ ▀█▀ █ █▄░█ █▀▀ █▀")
    print("█▄█ █▀█ █░▀░█ ██▄   ▄█ ██▄ ░█░ ░█░ █ █░▀█ █▄█ ▄█")



def get_player_name():
    """
    Prompts the user to enter their name and validates the input.

    Returns:
        str: The validated name entered by the user.

    Raises:
        None.
    """
    f.text_animation("First, You should enter you name ...")
    name = input("Enter you name: ").strip()
    while True:
        if name == "":
            f.text_animation("Empty Name")
            name = input("Enter you name: ")
        else :
            f.text_animation(f"Ok your name is {name}")
            break
    return name


def game_settings():
    """
    A function to handle game settings and customization of character attributes.
    """
    print_banner()

    player_name = get_player_name()

    time.sleep(2)

    f.clearScreen()

    time.sleep(0.5)


    print_banner()

    f.text_animation("Second, You should customize you character ...")


    hair_color = None
    eye_color = None
    scarf_color = None
    pants_color = None

    while True:
        # print character with colors
        character_printer(hair_color, eye_color, scarf_color, pants_color)


        # print parts choices


        f.text_animation("Choose character Style")
        time.sleep(0.5)
        print("1.Hair")
        time.sleep(0.2)
        print("2.Eye")
        time.sleep(0.2)
        print("3.Scarf")
        time.sleep(0.2)
        print("4.Pants")
        time.sleep(0.2)
        print("5.Random")
        time.sleep(0.2)
        print("If you are done, Enter")
        time.sleep(0.2)

        # ask for user choice and return the chosen attributes


        while True:
            choice = input("Enter 1,2,3,4,5 or Enter: ").strip()
            
            if choice == "":
                return {
                    "name": player_name,
                    "hair": hair_color,
                    "eye": eye_color,
                    "scarf": scarf_color,
                    "pants": pants_color,
                }
            
            if choice == "1":
                hair_color = color_choosing(1, hair_color, eye_color, scarf_color, pants_color)
                break
            
            elif choice == "2":
                eye_color = color_choosing(2, hair_color, eye_color, scarf_color, pants_color)
                break
            
            elif choice == "3":
                scarf_color = color_choosing(3, hair_color, eye_color, scarf_color, pants_color)
                break
            
            elif choice == "4":
                pants_color = color_choosing(4, hair_color, eye_color, scarf_color, pants_color)
                break
            
            elif choice == "5":
                color_list = ["white", "blue", "cyan", "magenta", "green", "yellow", "red"]
                hair_color = random.choice(color_list)
                eye_color = random.choice(color_list)
                scarf_color = random.choice(color_list)
                pants_color = random.choice(color_list)
                print("choosed color : ",colored(hair_color, hair_color), colored(eye_color, eye_color), colored(scarf_color, scarf_color), colored(pants_color, pants_color))
                break

            else:
                print("Wrong choice, Try again ...")
                time.sleep(0.5)

        f.clearScreen()