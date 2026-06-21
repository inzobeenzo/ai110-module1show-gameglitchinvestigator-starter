# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [The purpose of the game is to guess a randomly generated number based on hints of whether the inputted number is higher or lower than the actual number.] 
- [I doubt I found every bug, but the main ones included: reversed hints, the new game button not working, incorrect score tracking, and the failed difficulty change.] 
- [Firstly, the logic of the hints was fixed. Within that same function, there was some strange casting happening when the data should've only been ints so that was sorted. Also, the difficulty was corrected as the hard difficulty was actually easier than the normal one as the range was much smaller. For the new game button, you can just click refresh haha.] 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 40
2. Game returns "Go HIGHER"
3. User enters a guess of 99 → "Go LOWER!"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
tests\test_game_logic.py ......................................... [100%]
=============================================================================== 43 passed in 2.18s 
```

=======
## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
