# Function to display the options
def displayoptions(options):
    for each in options:
        print(f"Your options are: {each}")
    return

# Function to check the answer
def checkAns(RightAnswer,UserAnswer,youwon):

    print(RightAnswer, UserAnswer)
    if RightAnswer==UserAnswer:
        youwon=youwon+2000
        print(f"Your answer is right: {UserAnswer}, You won Rs.{youwon}\n")
        return youwon
    else:
        print(f"Game Over - Your answer is wrong, The right answer is {RightAnswer}, You won Rs.{youwon}\n")

        return youwon

# List of questions

Questions=['Q1','Q2','Q3','Q4','Q5','Q6']

# Variable to track price
youwon=0

# Loop through each question
for q in Questions:
    if q=='Q1':
        print("Queston no 1. Which of the following planets is known as the \"Red Planet\"?")
        optionslist=['Mercury','Venus','Mars','Jupiter']
        displayoptions(optionslist)
        UserAnswer=input("Enter the option value only: ").lower()
        rightAnswer="Mars".lower()
        youwon= checkAns(rightAnswer,UserAnswer,youwon)
    elif q=='Q2':
        print("Queston no 2. Who is the author of the Harry Potter book series?")
        optionslist = ['J.K. Rowling', 'Stephen King', 'George R.R. Martin', 'Dan Brown']
        displayoptions(optionslist)
        UserAnswer=input("Enter the option value only: ").lower()
        rightAnswer = "J.K. Rowling".lower()
        youwon= checkAns(rightAnswer,UserAnswer, youwon)

    elif q=='Q3':
        print("Queston no 3. Which programming language is widely used for web development?")
        optionslist = ['Python', 'JavaScript', 'C++', 'Ruby']
        displayoptions(optionslist)
        UserAnswer=input("Enter the option value only: ").lower()
        rightAnswer = "JavaScript".lower()
        youwon= checkAns(rightAnswer,UserAnswer,youwon)
    elif q == 'Q4':
        print("Question 4. What is the capital city of France?")
        optionslist = ['Paris', 'London', 'Rome', 'Berlin']
        displayoptions(optionslist)
        UserAnswer = input("Enter the option value only: ").lower()
        rightAnswer = "Paris".lower()
        youwon = checkAns(rightAnswer, UserAnswer, youwon)

    elif q == 'Q5':
        print("Question 5. Who painted the Mona Lisa?")
        optionslist = ['Pablo Picasso', 'Leonardo da Vinci', 'Vincent van Gogh', 'Michelangelo']
        displayoptions(optionslist)
        UserAnswer = input("Enter the option value only: ").lower()
        rightAnswer = "Leonardo da Vinci".lower()
        youwon = checkAns(rightAnswer, UserAnswer, youwon)

    elif q == 'Q6':
        print("Question 6. What is the largest ocean in the world?")
        optionslist = ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean']
        displayoptions(optionslist)
        UserAnswer = input("Enter the option value only: ").lower()
        rightAnswer = "Pacific Ocean".lower()
        youwon = checkAns(rightAnswer, UserAnswer, youwon)


    # If the user's answer is incorrect, break the loop
    if rightAnswer!=UserAnswer:
        break




# Print the final price
print("Your final price is Rs.", youwon)
