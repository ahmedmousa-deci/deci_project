import function as f
import time
import random
import string

def chapter1(name):
    print("█▀▀ █──█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀█ 　 ▄█─ ")
    print("█── █▀▀█ █▄▄█ █──█ ──█── █▀▀ █▄▄▀ 　 ─█─ ")
    print("▀▀▀ ▀──▀ ▀──▀ █▀▀▀ ──▀── ▀▀▀ ▀─▀▀ 　 ▄█▄")


    f.text_animation(f"{name} decided to start his journey to the Kingdom of Wonders the next morning.")
    f.text_animation("He picked up his small bag and started walking towards the forest.")
    
    f.text_animation(f"At the edge of the forest, {name} faced his first challenge:")
    f.text_animation("(1): Follow the paved road that looks safe but is long.")
    f.text_animation("(2): Take the narrow and bumpy path that delivers to the destination quickly but full of dangers.")

    f.text_animation("Press 1 or 2 to decide ...")


    chapter1_decide = f.choice_input(["You decide to: Follow the paved road.", "You decide to: Take the narrow and bumpy path"], [1,2])
    
    
    f.text_animation("\n\nPress Enter key to continue ...")
    input()
    f.clearScreen()
    time.sleep(1)
    return chapter1_decide

# make random password

treasure_password = "".join(random.choices(string.digits, k=4))


# lucky things

lucky_things = [f"A paper '{treasure_password}' written on it.", "Some of lock picks set", "A hammer", "A paper clip"]

# change probabilities

probabilities = [0.3, 0.3, 0.2, 0.2]


def paved_road_walking(name):
    f.text_animation(f"While walking on the paved road,\n{name} found a chest, He decided to open it.")
    f.text_animation(" After a while of hitting the lock on the chest, he finally succeeded in opening it.")
    f.text_animation(" And He found: ", end="")

    # lucky thing is random
    lucky_thing = random.choices(lucky_things, weights=probabilities, k=1)[0]

    f.random_choice_animation(lucky_thing)
    return {
        "treasure_password": treasure_password,
        "lucky_thing": lucky_thing
    }

def narrow_path_walking(name):
    f.text_animation(f"While walking down the narrow path,\n{name} ")
    f.text_animation(" He found a hole in the wall of the narrow, bumpy road with a rock in it")
    f.text_animation(" After a while of moving the rock, he finally succeeded in open the hole.")
    f.text_animation(" And He found: ", end="")

    # lucky thing is random

    lucky_thing = random.choices(lucky_things, weights=probabilities, k=1)[0]

    f.random_choice_animation(lucky_thing)
    return {
        "treasure_password": treasure_password,
        "lucky_thing": lucky_thing
    }