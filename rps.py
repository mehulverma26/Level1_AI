def game():
    from bolna import speak
    from take_command import TC
    import random

    d = "yes"
    a = 0
    while "yes" in d or "Yes" in d:
        print("you can choose between rock , paper or scissors")
        speak("you can choose between rock , paper or scissors")
        print("and your choice is?")
        speak("and your choice is?")
        query = TC()
        choice = ""
        if "rock" in query or "Rock" in query:
            choice = "rock"
        elif "paper" in query or "Paper" in query:
            choice = "paper"
        elif "scissors" in query or "Scissors" in query:
            choice = "scissors"
        print("player's choice:", choice)
        computer_choice = random.randint(1, 3)
        if computer_choice == 1:
            computer_choice = "rock"
        elif computer_choice == 2:
            computer_choice = "paper"
        elif computer_choice == 3:
            computer_choice = "scissors"
        comp = "Computer's choice is", computer_choice
        speak(comp)
        if choice == "rock":
            if computer_choice == "rock":
                print("It is a tie")
                b = "tie"
            elif computer_choice == "paper":
                print("You lose, sorry :( ")
                b = "lost"
            elif computer_choice == "scissors":
                print("You win!!!! congrats :) ")
                b = "win"
        elif choice == "paper":
            if computer_choice == "paper":
                print("It is a tie")
                b = "tie"
            elif computer_choice == "rock":
                print("You win!!!! congrats :) ")
                b = "win"
            elif computer_choice == "scissors":
                print("You lose, sorry :( ")
                b = "lost"
        elif choice == "scissors":
            if computer_choice == "scissors":
                print("It is a tie")
                b = "tie"
            elif computer_choice == "rock":
                print("You lose, sorry :( ")
                b = "lost"
            elif computer_choice == "paper":
                print("You win!!!! congrats :) ")
                b = "win"
        if b == "win":
            a = a + 1
        elif b == "tie":
            a = a + 0
        elif b == "lost":
            a = a - 1
        print("your current score is", a)
        speak("do you want to play again?")
        d = TC()
    if "no" in d or "No" in d:
        print("Thanks for playing!!!")
        final_score = "your final score is", a
        speak(final_score)
