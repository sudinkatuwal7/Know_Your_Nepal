import turtle
import pandas
import time
import random

screen = turtle.Screen()
screen.title("Nepal Game")
image = "blank_districts_img.gif"
screen.addshape(image)
turtle.shape(image)

# Add your victory image (make sure it's a .gif file)
victory_image = "cr7.gif"  # Replace with your image filename
screen.addshape(victory_image)

data = pandas.read_csv("77_districts.csv")
all_districts = data.district.to_list()
guessed_districts = []

# guessed_districts = ["dummy"] * 77  # Creates a list with 77 items

turtle.colormode(255)

while len(guessed_districts) < 77:
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/77 District Correct",
                                       prompt="What's the district name?")

    # Crucial fix: handles "Cancel" button to prevent crash
    if answer_district is None:
        break

    answer_district = answer_district.title()

    if answer_district == "Exit":
        to_be_guessed = []
        for district in all_districts:
            if district not in guessed_districts:
                to_be_guessed.append(district)
        df = pandas.DataFrame(to_be_guessed)
        print(df)
        df.to_csv("failed_to_guess.csv")
        break

    # cause here we answer all of the district names
    # Added 'and answer_district not in guessed_districts' so you can't guess the same one twice
    if answer_district in all_districts and answer_district not in guessed_districts:
        guessed_districts.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.district == answer_district]
        # Wrapped in int() to ensure Turtle can read the coordinates correctly
        t.goto(int(district_data.x.item()), int(district_data.y.item()))
        t.write(answer_district)

# Check if all districts were guessed
if len(guessed_districts) == 77:
    turtle.shape(victory_image)

    victory_text = turtle.Turtle()
    victory_text.hideturtle()
    victory_text.penup()

    turtle.colormode(255)  # Enable RGB colors

    while True:  # infinite animation
        victory_text.clear()

        # Generate a random color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        victory_text.color(r, g, b)

        # First line
        victory_text.goto(0, 250)
        victory_text.write(
            "Google hanera milako hera, laaj pacheko",
            align="center",
            font=("Helvetica", 24, "bold")
        )

        # Second line
        victory_text.goto(0, 210)
        victory_text.write(
            "Ali batho huna paro desh ko jilla thachhaina lata",
            align="center",
            font=("Helvetica", 24, "bold")
        )

        time.sleep(0.1)
turtle.mainloop()
