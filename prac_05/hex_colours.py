COLOUR_TO_HEXADECIMAL_COLOUR = {"AliceBlue": "#f0f8ff", "BabyBlue": "#89cff0", "Camel": "#c19a6b",
                                "DarkGreen": "#006400", "Ebony": "#555d50", "Flamingo Pink": "#fc8eac",
                                "GoldenBrown": "#996515", "HanBlue": "#446ccf", "Inchworm": "#b2ec5d",
                                "Jasmine": "#f8de7e", "KeyLime:": "#e8f48c", "Lavender": "#e6e6fa",
                                "Magenta": "#ff00ff"}

colour_name = input("Which colour are you looking for?: ")
while colour_name != "":
    try:
        print(f"The colour is {COLOUR_TO_HEXADECIMAL_COLOUR[colour_name]}")
    except KeyError:
        print("Sorry, we do not have that color")
    colour_name = input("Which colour are you looking for?: ")
