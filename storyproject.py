start = '''
After a vacation gone wrong, you're seeking a sanctuary from the perils of the
Amazon rainforest. You are faced with a decision.
'''
print(start)
#this is if you win.
print("Decide to go up or down.")
answer = input()
end2= '''
You've reached eternal slumber where you dream about swimming with dolphins. Try again....
'''  #this is if you die.

def restart():
    answer = input('Run again? (y/n): ')
    if answer == 'yes':
        game()
    else:
        print('Goodbye')


def game():
    if answer == "up":
        answer2=input("Your decision to go up, allows you to climb up a vine.....What's this, a panther! Should you fight or run?") # finished the story by writing what happens
    if answer2 == "fight":
        print("You successfully defeated the panther. Congrats!")
        answer3= input("You hear a disturbing sound...prepare to fight what's there, or run.")
        if answer3 == "fight":
            print("It's a giant spider! You're bitten and now poisoned, no antidotes around here.")
            print(end2)
            restart()
        elif answer3 == "run":
            print("You escaped the spider!")
            print("  In the distance, you see a sanctuary...getting closer you identify the sanctuary as a treehouse.")
            restart()
    elif answer2 == "run":
            print("The panther chases you and you stumble on a Titan beetle. The panther wins this round.")
            print(end2)
            restart()

    elif answer == "down":
        print("When you go down you encounter a swamp.") # finished the story writing what happens
        down_answer1= input("Will you swim across or walk across a fallen tree?")
        if down_answer1 =="swim":
            print("A dolphin offers to take you across. You accept its offer and advance.")
            down_answer2= input("Continue?")
            if down_answer2 == "yes":
                print("You ride the dolphin into the sunset, in hopes of starting a new life.")
            if down_answer2 == "no":
                print(end1)
                restart()
        elif down_answer1 =="walk":
            print("Your eyesight isn't what it used to be, you accidentally step on an alligator.")
            down_answer3=input("Will you challenge the alligator or simply jump to the next log?")
            if down_answer3== "challenge alligator":
                print("The alligator is taking you out for dinner, tonight.")
                print(end2)
                restart()
            if down_answer3 == "jump":
                print("You've escaped the alligator! Congrats!")
                print("In the distance, you see a sanctuary...getting closer you identify the sanctuary as a treehouse.)
                restart()

    else:
        print("Incorrect answer, please answer the question.")


game()
exitonclick()
