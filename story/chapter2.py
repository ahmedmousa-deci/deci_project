import function as f

# decide 1


def paved_road(name):
    f.text_animation(f"{name} started walking on the paved road,\n and after a short while he met an old lady asking for help carrying her basket")
    f.text_animation("And You can decide what to do: ")
    f.text_animation("(1): Help the old lady.")
    f.text_animation("(2): Apologize and move on.")
    f.text_animation("Press 1 or 2 to decide ...")

    return  f.choice_input(["You decide to: Help the old lady.", "You decide to: Apologize and move on."], [1,2])




# decide 2

def narrow_path(name):
    f.text_animation(f"While walking down the narrow path,\n{name} found a small animal trapped in a trap.\n The animal seems to want to help.")        
    f.text_animation("And you can ...")
    f.text_animation("(1): Try to free the animal.")
    f.text_animation("(2): Avoid the animal and keep walking.")
    f.text_animation("Press 1 or 2 to decide ...")
    
    return f.choice_input(["Try to free the animal.", "Avoid the animal and keep walking."], [3,4])


