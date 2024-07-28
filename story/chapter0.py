import function as f


def chapter_0(player_name):
    f.text_animation(
        "In a small village surrounded by forests full of secrets.")
    f.text_animation(f"There was a brave boy named {player_name}.")
    f.text_animation(
        "One day, a mysterious wizard arrived in the village and told " +
        f"{player_name} about the kingdom of" +
        " wonders hiding deep in the forest.")
    f.text_animation(
        "The magician told him that there was" +
        " a valuable treasure waiting for him.")
    f.text_animation(
        f"But he warned {player_name} that the path was full of dangers and" +
        " that he would have to make wise decisions to reach the treasure.")

    f.continue_key()
