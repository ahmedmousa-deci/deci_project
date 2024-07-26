# imports
import os
import sys
import time
import random
import string
# fucntions

# clear console function


def clear_screen():
    # Clear screen for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear screen for macOS/Linux
    else:
        os.system('clear')


# make typeing animation

def text_animation(text="def", delay=0.04, end="\n"):
    # get every letter in the text and print it and wait for a part of second
    for i in range(len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)


# choice key reading function

def choice_input(text, decideVal=[]):
    print("\n")
    list = [str(i + 1) for i in range(len(text))]
    while True:
        choice = input(f"Press {", ".join(list, )} to continue: ").strip()
        if choice in list:
            text_animation(text[int(choice) - 1])
            return decideVal[int(choice) - 1] if len(decideVal) > 0 else choice
        else:
            print("wrong input")


def random_choice_animation(val, end="\n"):
    for i in range(40):
        sys.stdout.write("".join(random.choices(string.ascii_letters, k=7)))
        sys.stdout.flush()
        time.sleep(0.06)
        sys.stdout.write("\b" * 7)
    sys.stdout.write(val + " " * 7)
    sys.stdout.write(end)


def continue_key():
    text_animation("\n\nPress Enter key to continue ...")
    input()
    clear_screen()
