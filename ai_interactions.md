# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
|Decimals|"I want to ensure the logic of the game holds for extreme cases. i've already tested negative numbers. i want to see if decimal numbers work. if you can create other edge cases that may have been overlooked do so. generate a suite of pytest cases that verify your game handles these inputs gracefully." | test_decimal_truncates_down(), test_decimal_exactly_half(), test_decimal_close_to_boundary(), test_decimal_negative()|Yes |Although this is mostly on the user to follow the rules of the game, these situations should still be handled properly (eg. rounded properly, correct hint given, etc.)|
|invalid inputs |same|section in test_game_logic.py: # parse_guess — invalid / malformed inputs |Yes |Similar reasoning as before, but a little more broad as there may be a misinput or an input that is handled improperly based on its data type.|
|Extreme inputs (very large/small)|same|section in test_game_logic.py: # parse_guess — boundary and extreme integers |Yes |Same reasoning as decimals as you would hope the user follows the rules of the game, but just in case they don't, that situation is handled properly.|

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
