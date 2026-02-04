import turtle
import pandas

screen = turtle.Screen()
screen.title("Nepal Game")
image = "blank_districts_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("77_districts.csv")
all_districts = data.district.to_list()

guessed_districts = []

while len(guessed_districts) < 77:
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/77 District Correct", prompt="What's the district name?")
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
    if answer_district in all_districts:
        guessed_districts.append(answer_district)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.district == answer_district]
        t.goto(district_data.x.item(), district_data.y.item())
        t.write(answer_district)



# Safely extract coordinates as floats
#         x_pos = float(district_data.x.iloc[0])
#         y_pos = float(district_data.y.iloc[0])
#
# -----------------------------------------------
# used to get the points of the districts

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

