# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The game page appeared the way I would assume it should. However, when I began to test some input, things were clearly not implemented the way they should've been. For example, I couldn't figure out the pattern for my score as it was fluctuating each iteration.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    The hints were reversed, the new game button didn't work, the difficulty wouldn't properly adjust, and I could enter numbers < 0 or > 100 (the last one isn't really a bug, but more so a functionality thing) However, I feel the other 2 are bugs. 
    
    (These bugs were found way later):
    Line 36 — update_score win formula off-by-one
    100 - 10 * (attempt_number + 1) should be 100 - 10 * attempt_number. On attempt 1 you score 80 instead of 90.

    Lines 41–44 — asymmetric scoring bug
    "Too High" gives +5 on even attempts, −5 on odd. "Too Low" always gives −5. There's no reason "Too High" should ever reward points — both should penalize equally.

    Line 120 — new game ignores difficulty range
    random.randint(1, 100) hardcodes Easy/Hard range instead of using get_range_for_difficulty(difficulty).

    Line 94 — hint text hardcoded
    "Guess a number between 1 and 100." ignores the actual low/high from the selected difficulty.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|1|Go HIGHER!|Go LOWER!|None|
|-1|Only numbers 1-100|Go LOWER!|None|
|Hard|Range: 1-200|1-50|None|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    I used Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    The AI suggestion was correct in the sense of logic errors for the check_guess function. It correctly identified the reversed logic of the guess being too high or low based on the secret. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    I asked it to look at the entire function, which this also could be an error on my end, but I was expecting it to also address the try/exception block and it didn't even acknowledge it at all. Only when I highlighted it and asked it to contexualize it did it realize that it was an error. If I had only pushed the first correction, the function would've still been wrong.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I walked through the logic myself to ensure that it agreed with my initial thoughts. After verifying that the logic seemed sound, running the pytest or assert code and seeing it on the actual website solidified my confidence that the logic was correct.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    The test that was run was just ensuring that the correct message was relayed based on the guess. For example, for check_guess(60,50), the logic should be that the output is "Too High" and the message relayed should be "Go LOWER". The assert block ensured that at least that part of the game was running correctly.
- Did AI help you design or understand any tests? How?
    Yes. It helped create the assert blocks themselves as I had the logic, but didn't know how to insert it directly in the file. It helped with syntax more than it did with the functionality.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    A rerun is like an entire application restarting and all of the work that was done is forgotten, while a session state is more so like a checkpoint in your program so you don't have to start from scratch each time and can use saved variables. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
    Probably comments. It's super simple, but for a large program where logic can get hard to follow, I think using comments and putting things in a way that makes sense to you would lead to better production and understanding. Also, I need to be better at giving the correct context so that I don't have to talk about multiple fixes for the same function.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
    I would say that I need to use it much more often. Parsing through the code itself is a job that I feel should be through the actual programmer rather than the AI, but if I ever get stuck, instead of spending dozens of minutes on it, I can just prompt the AI which not only would clarify things but could also reveal things I overlooked.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    I think that AI is great at building on top of existing ideas, but has trouble thinking about specific edge cases or its implications on the rest of the program. That was seen very clearly when I tried using Claude to fix my function as it overlooked the whole other half of the function. It reminds me of the doorman fallacy. 