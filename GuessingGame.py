from random import randint


guessed=False
num_of_gusses=0;
ran_num=randint(1,100)
past_guesses=[]
guessed_once=False
print(ran_num)
print("Welcome to the Guessing Game")
while guessed==False:
    try:
        user_guess = int(input("try to guess our number between 1-100\n"))
    except ValueError:
        print("enter a num please")
        continue

    num_of_gusses+=1
    if user_guess<1 or user_guess>100:
        print("OUT OF BOUNDS")
        break
    if user_guess==ran_num:
        print(f"woho {ran_num} was the number! you did it in {num_of_gusses} Guesses! ")
        print(f"here is your last Guesses {past_guesses}")
        guessed=True
        break

    past_guesses.append(user_guess)

    if num_of_gusses>=2:
        if abs(user_guess)>abs(past_guesses[-2]):
            print("warmer!")
        elif user_guess==past_guesses[-2]:
            print("Same Number!")
        else:
            print("Colder!")
    else:
        if abs(user_guess-ran_num)<=10:
            print("warm")
        else:
            print("cold")





