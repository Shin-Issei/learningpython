# NONONONONONONONONONONONONONONONONONONONO


def askUser():
    print("Hey. How are you feeling about the furture?")
    userAnswer = input()
    return userAnswer

def checkAnswer(providedAnsewer):
    correctAnswer = "My 30s will not be like my 20s"
    if (correctAnswer == providedAnsewer):
        print("That is wonderful news! :D")
    else:
        print("Oh...that isn't what I expected...")


checkAnswer(askUser())