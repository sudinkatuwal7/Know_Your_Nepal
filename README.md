# 🇳🇵 Know Your Nepal Game

An interactive Nepal Districts guessing game built using **Python Turtle** and **Pandas**.  
Type district names to label them on the Nepal map. If you exit early, the program generates a CSV file containing the districts you missed so you can learn them later.

---

## ✨ Features

- 🗺️ Displays a blank map of Nepal using Turtle graphics
- ⌨️ User inputs district names through a popup text box
- ✅ Correct guesses are written at the correct location on the map
- 📊 Uses Pandas to read district coordinates from `77_districts.csv`
- 🚪 Type `Exit` anytime to generate a CSV of unguessed districts

---

## 🧠 How It Works

- The program reads all district names + coordinates from `77_districts.csv`
- Each time you guess a correct district, it gets added to `guessed_districts`
- A turtle writes the district name on the map at its `(x, y)` position
- Duplicate guesses are ignored
- Clicking Cancel safely exits the game without crashing
- If you type **Exit**, it saves all unguessed districts to:
```
`failed_to_guess.csv`
```
---

## 📁 Project Structure
```
know_your_nepal/
│
├── main.py
├── 77_districts.csv
├── blank_districts_img.gif
├── cr7.gif                 # victory image shown after guessing all districts
├── failed_to_guess.csv     # generated after typing "Exit"
├── .gitignore
└── README.md
```
---
## Gameplay
**Starting phase of the Game**
<img width="2199" height="1231" alt="Screenshot (184)" src="https://github.com/user-attachments/assets/9df6a74b-bf0e-4332-9b99-2bb4ee817ed6" />

**After guessing all districts**
**Proud moment! Cheers🏆!**
<img width="2560" height="1440" alt="image" src="https://github.com/user-attachments/assets/d113f369-934c-49da-8f64-6ffb78f83933" />

---
## ⚙️ Requirements

- Python 3.7 or +
- pandas

Install pandas using:

```bash
pip install pandas
```
---
## ▶️ How to Run

Clone or download this repository,
```bash
https://github.com/sudinkatuwal7/Know_Your_Nepal.git
```
**Run the game:**
```bash
python main.py
```
Make sure all .gif and .csv files are in the same folder as main.py

---

## 🎮 Controls / Gameplay

- Enter a state name in the input box.

- Duplicate guesses are ignored.

- Correct answers will appear on the map.

- To give up and learn the missed districts:

**Type:**
```
Exit
```
---

## 📝 Output File

If you exit before guessing all 77 districts, the program generates:
```
failed_to_guess.csv
```
This file contains the states you missed, so you can practice them later.

---

## 🚀 Future Improvements

- Display feedback for incorrect guesses

- Add a timer or scoring system

- Save high scores

- Improve UI animations

- Add sound effects

---

## 🎉 Enjoy the Game!

`Have fun exploring the beautiful Nepal map, test your geography skills, and keep on learning!`

`                                      Jay Nepal                                              `                                  
