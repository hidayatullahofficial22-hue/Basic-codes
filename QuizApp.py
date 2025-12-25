print("Welcome to quiz Application!")

questions = ( "what is the largest bone in the body? ",
           
            "where is the smallest bone in the body? ",

            "Beauty bone in human body? ",

            "Total bones in human body? " )

options = (
        ("A.sternum ","B.Humour ","C.patella ","D.oscus "),

        ("A.ear ","B.face ","C.back ","D.legs "),

        ("A.cervical ","B.sterum ","C.facial ","D.cranium "),

        ("A.205 ","B.206 ","C.208 ","D.211 ")

          )


Answers = ("B","A","A","B")

guesses = []

score = 0

question_num=0



for question in questions:
    
    print("-----------------------------------------------------")

    print(question)

    for option in options[question_num]:
        print(option)
    guess = input("Enter an option (A , B , C , D) ").upper()
    guesses.append(guess)
    if guess == Answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{Answers[question_num]} is the correct answer")
    question_num = question_num + 1
print("----------------------------Final Result------------------------------")
print(f"Your guesses are: {guesses}!")
print(f"Correct Answers are: {Answers} ")
print(f"You get {(score/len(questions))*100}% Marks in your quize.")
