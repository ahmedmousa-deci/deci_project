import function as f


# old lady

def helped_lady(name):
    f.text_animation(
        f"The old lady was a witch in disguise.\nAfter {name} helped her,\n she gave him a magic wand to help him on his journey.")
    f.text_animation("And now You can use it for: ")
    f.text_animation("(1): To open a secret door in the forest.")
    f.text_animation("(2): Keep it for emergencies.")
    f.text_animation("Press 1 or 2 to decide ...")
    return f.choice_input(["You decide to: Open a secret door in the forest.",
                          "You decide to: Keep it for emergencies."], [1, 2])


def not_helped_lady(name):
    f.text_animation(
        f"The old lady was disappointed and left him. \nAs {name} continued walking,\n he found himself in dense fog and lost his way.")
    f.text_animation("And you can do")
    f.text_animation(
        "(1): Try to find his way by listening to the sounds of the forest.")
    f.text_animation("(2): Wait in place until the fog dissipates.")
    f.text_animation("Press 1 or 2 to decide ...")
    return f.choice_input(["You decide to: Try to find his way by listening",
                          "You decide to: Wait in place until the fog dissipates."], [3, 4])


# Animal

def helped_animal(name):
    f.text_animation(
        f"The animal was a magical creature.\n After {name} freed him,\n he led him to a secret passage that led directly to the heart of the Kingdom of Wonders.")
    f.text_animation("And you can decide to: ")
    f.text_animation("(1): Follow the magical creature.")
    f.text_animation("(2): Continued the journey alone.")
    f.text_animation("Press 1 or 2 to decide ...")
    return f.choice_input(["You decide to: Follow the magical creature.",
                          "You decide to: Continued the journey alone."], [5, 6])


def not_helped_animal(name):
    f.text_animation(
        f"When {name} bypasses the animal,\n he encounters a group of enchanted trees that start to close in on him.")
    f.text_animation("And You can: ")
    f.text_animation("(1): Use his wits to try to talk to the trees.")
    f.text_animation("(2): Try to run and escape as fast as he can.")
    f.text_animation("Press 1 or 2 to decide ...")
    return f.choice_input(["You decide to: Use his wits",
                          "You decide to: Try to run and escape"], [7, 8])
