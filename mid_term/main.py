# Trivia Challenge
# Trivia game that reads a plain text file
# Daniel Lehman

# imports
import sys
from datetime import datetime

# change this variable to the test you are taking
test_file = "midterm_test.txt"

# functions
def open_file(file_name, mode):
    """open and return a file with the given permissions,
    if there is any errors the error will be sent to a seprate file."""
    try:
        file = open("assets/test_files/" + file_name, mode)
    except IOError as e:
        print("Invalid name for file", file_name, "Ending the program.", e)
        try:
            time = datetime.now()
            error_time = time.strftime("%m/%d/%y %H:%M:%S")
            error = open("assets/error_log/error_log.txt", "a")
            error.write(str(e) + " " + str(error_time)+"\n")
            input("\n\nPress enter to exit ")
            sys.exit()
        except:
            sys.exit()

    return file

def get_name():
    """gets a good name from the user and start date and time for the test"""
    time = datetime.now()
    test_time = time.strftime("%m/%d %H:%M")
    while True:
        name = input("Enter your first and last name: ")
        if len(name) >= 3 and " " in name and not name.isnumeric():
            name = name.title()
            return name, test_time
        else:
            print("Not a good name")

def next_line(file):
    """replaces the / with a next line character and moves to the next line"""
    try:
        line = file.readline()
        line = line.replace("/", "\n")
        return line
    except:
        print("Something went wrong while replacing a line in the file.")
        sys.exit()

def question_block(file):
    """gets the extire question block from the file"""
    category = next_line(file)
    question = next_line(file)
    choices = []
    for i in range(4):
        choices.append(next_line(file))
    correct = next_line(file)
    if correct:
        correct = correct[0]
    explanation = next_line(file)

    return category, question, choices, correct, explanation

def welcome(name, title, time):
    """Tells the user what is going on, welcoming the player to the game"""
    print("Welcome " + name + " to your Mid-Term\n")
    print("Your test was created by " + title)
    print("Your test wsa started at " + time, "\n")

def create_report_card(name, score, total_questions, start_time, end_time):
    """generates the report card for the user"""
    # opens the file under the user's name
    report = open("assets/report_cards/" + name + ".txt", "w")
    percent = score / total_questions * 100
    # gets the letter grade from the percent
    if percent > 90:
        letter_grade = "A"
    elif percent > 85:
        letter_grade = "B"
    elif percent > 75:
        letter_grade = "C"
    elif percent > 65:
        letter_grade = "D"
    else:
        letter_grade = "F"
    # formats all of the data on the report card
    percent = str(int(percent))
    report.write("Name = " + name + "\nStart time = " + start_time + "\nTotal correct = " + str(score) + "\nTotal questions = " + str(total_questions) \
                 + "\nPercent: " + percent + "%" + "\nLetter Grade = " + letter_grade + "\nEnd time = " + end_time)


def main(test_file):
    score = 0
    total_que = 0
    # gets a good name and time
    name, time = get_name()
    # file being used for test
    file = open_file(test_file, "r")
    title = next_line(file)
    welcome(name, title, time)
    # gets the first question
    category, question, choices, correct, explanation = question_block(file)
    # starts game loop
    while category:
        total_que += 1
        print("Category:", category, "\n")
        print("\t", question)
        for i in range(len(choices)):
            print(str.format("\t{}:  {}", i + 1, choices[i]))
        answer = input("What is your answer?: ")
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong!", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
        category, question, choices, correct, explanation = question_block(file)
    # closing the file
    end_time = datetime.now()
    end_time_f = end_time.strftime("%m/%d %H:%M")
    file.close()
    # finishing up
    print("That was the final quesition!")
    print("Your final score is", score)
    print("Your report card ws created at the following location")
    print("assets/report_cards/" + name + ".txt")
    create_report_card(name, score, total_que, time, end_time_f)



# main
main(test_file)
