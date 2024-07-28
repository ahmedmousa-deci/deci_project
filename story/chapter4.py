import function as f
import random
import time


def treasure_password_enter(treasure_password):
    while True:
        password = input(
            "\nEnter the password or enter Q to Exit: ").replace(" ", "")
        if password.lower() == "q":
            return False
        elif not password.isdigit():
            f.text_animation("The password must be a number")
        elif len(password) != 4:
            f.text_animation("The password must be 4 digits")
        elif password != treasure_password:
            f.text_animation("Wrong password, try again")
        else:
            return True


def luckily_treasure(name, lucky_thing, treasure_password):

    # describe what is happing
    f.text_animation(
        f"{name} has found the treasure chest with a lock has a secret" +
        " number contains from 4 digits that must be entered" +
        " or another way to open it must be found.")
    f.text_animation("And that is what you can make: ")
    # print the ways

    ways = [
        "Try to enter the password",
        f"Try to open it with {lucky_thing}",
        "Try to break the lock with your hand only",
        "Try to find another way to open it"]

    # remove the password paper from the list

    try:
        ways.remove(
            f"Try to open it with A paper '{treasure_password}' written on it."
        )
    except BaseException:
        pass

    # printing the ways

    for i, w in enumerate(ways):
        f.text_animation(f"{i + 1}.{w}")

    # lucky treasure is random

    lucky_treasure = random.choice(
        [
            f"{name} found a lot of gold and jewelry,\n" +
            " And He became the richest man in his village",
            f"{name} found some very powerful magical weapons" +
            " and armor,\n After he goes to a Magician to train him,\n" +
            " And he became the best magic fighter",
            f"{name} found some magic books,\n After while" +
            " he learned the magic and became the best magician ever"])

    while True:
        # take input
        choice = f.choice_input(ways)

        # if choice is Enter the password
        if choice == "1":
            if treasure_password_enter(treasure_password):
                f.text_animation(
                    f"{name} entered The password" +
                    " correctly and opened the chest")
                time.sleep(0.5)
                f.text_animation(lucky_treasure)
                break

        # if choice is open it with lucky thing
        # check if the contains lucky thing to handel the case when the lucky
        # thing is password paper
        elif choice == "2" and len(ways) == 4:
            f.text_animation(
                f"{name} tries to open the chest with {lucky_thing}," +
                " After many attempts, it is not impossible to open the chest"
            )
            time.sleep(0.5)
            f.text_animation(lucky_treasure)
            break

        # if choice is break the lock with hand

        elif (choice == "2") or (choice == "3" and len(ways) == 4):
            f.text_animation(
                f"{name} tries to break the lock with your hand only")
            # random chance to open the chest by hand is 25%
            if random.choices([True, False], weights=[0.25, 0.75])[0]:
                f.text_animation(
                    f"After of {name} trying to break the lock " +
                    "with your hand only, He finally opened the chest")
                time.sleep(0.5)
                f.text_animation(lucky_treasure)
            else:
                f.text_animation(
                    f"After of {name} trying to break the lock with " +
                    "your hand only, He failed to open the chest")
            break

        # if choice is find another way

        else:
            f.text_animation(f"{name} went to find another way to open it")
            # random tool with chance of 60% to be None
            tool = random.choices(
                [
                    f"A paper '{treasure_password}' written on it.",
                    "Some of lock picks set",
                    "A hammer",
                    "A paper clip",
                    None],
                weights=[
                    0.1,
                    0.1,
                    0.1,
                    0.1,
                    0.6])[0]
            if tool is None:
                f.text_animation(
                    f" After of {name} trying to find another way to open it,"
                    +
                    " He didn't find any tool to open the chest")
                continue
            f.text_animation(
                f" After of {name} trying to find another way to open it," +
                " He finally found {tool} and he used it to open the ")
            time.sleep(0.5)
            f.text_animation(lucky_treasure)
            break


def print_victory():
    print("────────────────────────────────────────────────────────" +
          "──────────────────────────────────────────────────────")
    print("─██████──██████─██████████─██████████████─██████████████" +
          "─██████████████─████████████████───████████──████████─")
    print("─██░░██──██░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██" +
          "─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░██──██░░░░██─")
    print("─██░░██──██░░██─████░░████─██░░██████████─██████░░██████" +
          "─██░░██████░░██─██░░████████░░██───████░░██──██░░████─")
    print("─██░░██──██░░██───██░░██───██░░██─────────────██░░██────" +
          "─██░░██──██░░██─██░░██────██░░██─────██░░░░██░░░░██───")
    print("─██░░██──██░░██───██░░██───██░░██─────────────██░░██────" +
          "─██░░██──██░░██─██░░████████░░██─────████░░░░░░████───")
    print("─██░░██──██░░██───██░░██───██░░██─────────────██░░██────" +
          "─██░░██──██░░██─██░░░░░░░░░░░░██───────████░░████─────")
    print("─██░░██──██░░██───██░░██───██░░██─────────────██░░██────" +
          "─██░░██──██░░██─██░░██████░░████─────────██░░██───────")
    print("─██░░░░██░░░░██───██░░██───██░░██─────────────██░░██────" +
          "─██░░██──██░░██─██░░██──██░░██───────────██░░██───────")
    print("─████░░░░░░████─████░░████─██░░██████████─────██░░██────" +
          "─██░░██████░░██─██░░██──██░░██████───────██░░██───────")
    print("───████░░████───██░░░░░░██─██░░░░░░░░░░██─────██░░██────" +
          "─██░░░░░░░░░░██─██░░██──██░░░░░░██───────██░░██───────")
    print("─────██████─────██████████─██████████████─────██████────" +
          "─██████████████─██████──██████████───────██████───────")
    print("────────────────────────────────────────────────────────" +
          "──────────────────────────────────────────────────────")


def print_lost():
    print("─────────────────────────────────────────────────" +
          "────────────────────────────────────────────────────────────────")
    print("─████████──████████─██████████████─██████──██████" +
          "────██████─────────██████████████─██████████████─██████████████─")
    print("─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░██──██░░██" +
          "────██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─")
    print("─████░░██──██░░████─██░░██████░░██─██░░██──██░░██" +
          "────██░░██─────────██░░██████░░██─██░░██████████─██░░██████████─")
    print("───██░░░░██░░░░██───██░░██──██░░██─██░░██──██░░██" +
          "────██░░██─────────██░░██──██░░██─██░░██─────────██░░██─────────")
    print("───████░░░░░░████───██░░██──██░░██─██░░██──██░░██" +
          "────██░░██─────────██░░██──██░░██─██░░██████████─██░░██████████─")
    print("─────████░░████─────██░░██──██░░██─██░░██──██░░██" +
          "────██░░██─────────██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─")
    print("───────██░░██───────██░░██──██░░██─██░░██──██░░██" +
          "────██░░██─────────██░░██──██░░██─██████████░░██─██░░██████████─")
    print("───────██░░██───────██░░██──██░░██─██░░██──██░░██" +
          "────██░░██─────────██░░██──██░░██─────────██░░██─██░░██─────────")
    print("───────██░░██───────██░░██████░░██─██░░██████░░██" +
          "────██░░██████████─██░░██████░░██─██████████░░██─██░░██████████─")
    print("───────██░░██───────██░░░░░░░░░░██─██░░░░░░░░░░██" +
          "────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─")
    print("───────██████───────██████████████─██████████████" +
          "────██████████████─██████████████─██████████████─██████████████─")
    print("─────────────────────────────────────────────────" +
          "────────────────────────────────────────────────────────────────")


def using_magic_wand(name, lucky_thing, treasure_password):
    f.text_animation(
        f"{name} uses the magic wand to open the secret door," +
        " he finds the Kingdom of Wonders and its hidden treasure.")
    luckily_treasure(name, lucky_thing, treasure_password)
    f.continue_key()
    print_victory()


def keeping_magic_wand(name):
    f.text_animation(
        f"{name} keeps the wand for emergencies, he faces a group " +
        "of monsters on his way, and the wand turns out to be useless.")
    f.continue_key()
    print_lost()


def trying_to_find_way(name):
    f.text_animation(
        f"{name} tries to find his way by listening to the sounds" +
        " of the forest, he ends up in a cave full of traps.")
    f.continue_key()
    print_lost()


def wait_the_fog(name, lucky_thing, treasure_password):
    f.text_animation(
        f"{name} waits in place until the fog clears, " +
        "he finds his way to the Kingdom of Wonders once the fog lifts.")
    luckily_treasure(name, lucky_thing, treasure_password)
    f.continue_key()
    print_victory()


def follow_animal(name, lucky_thing, treasure_password):
    f.text_animation(
        f"{name} follows the magical creature," +
        " he reaches the Kingdom of Wonders and finds the treasure.")
    luckily_treasure(name, lucky_thing, treasure_password)
    f.continue_key()
    print_victory()


def continue_alone(name):
    f.text_animation(
        f"If {name} continues on his journey alone," +
        " he finds himself at a dead end and gets lost in the forest.")
    f.continue_key()
    print_lost()


def talking_trees(name, lucky_thing, treasure_password):
    f.text_animation(
        f"{name} tries to talk to the trees, a wise tree appears" +
        " and helps him find the right path to the Kingdom of Wonders.")
    luckily_treasure(name, lucky_thing, treasure_password)
    f.continue_key()
    print_victory()


def running_away(name):
    f.text_animation(
        f"{name} tries to run and escape, he falls into a deep pit.")
    f.continue_key()
    print_lost()
