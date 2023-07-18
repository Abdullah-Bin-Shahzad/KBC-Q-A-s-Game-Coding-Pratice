# Code for KBC Game

This code implements a simple "Kaun Banega Crorepati" (KBC) game in Python. It presents the user with multiple-choice questions and checks their answers. The game awards points for correct answers and ends if the user provides an incorrect answer.

## How to Play

1. The code defines multiple questions (`Q1`, `Q2`, `Q3`) along with their corresponding options and answers.
2. The function `displayoptions(options)` takes a list of options as input and displays them to the user.
3. The function `checkAns(RightAnswer, UserAnswer, youwon)` compares the user's answer with the correct answer, updates the price (`youwon`), and provides appropriate feedback.
4. The variable `youwon` keeps track of the price, which starts at 0.
5. The game runs through each question sequentially:
    - It displays the question and options.
    - It prompts the user to enter their answer.
    - The user's answer is converted to lowercase for comparison.
    - The function `checkAns()` is called to evaluate the answer and update the score.
    - If the user provides an incorrect answer, the game ends.
6. The final price is displayed to the user at the end of the game.

Feel free to modify the questions, options, and answers to create your own version of the KBC game.

**Note:** Ensure that you have the required `displayoptions()` and `checkAns()` functions defined before executing the main code.

Have fun playing KBC!
