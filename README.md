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
- If you type **Exit**, it saves all unguessed districts to:

`failed_to_guess.csv`

---

## 📁 Project Structure
```
know_your_nepal/
│
├── main.py
├── 77_districts.csv
├── blank_districts_img.gif
├── failed_to_guess.csv # generated after typing "Exit"
├── .gitignore
└── README.md
```
---
## Gameplay

<img width="2199" height="1231" alt="Screenshot (184)" src="https://github.com/user-attachments/assets/9df6a74b-bf0e-4332-9b99-2bb4ee817ed6" />

---
## ⚙️ Requirements

- Python 3.7 or +
- pandas

Install pandas using:

```bash
pip install pandas
```
---

## 🎮 Controls / Gameplay

Enter a state name in the input box

Correct answers will appear on the map

To give up and learn the missed districts:

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

- Keep asking until all 77 are guessed

- Prevent duplicate guesses

- Show incorrect guess feedback

- Add timer or scoring system

---

## 🎉 Enjoy the Game!

`Have fun exploring the beautiful Nepal map, test your geography skills, and keep on learning!`
