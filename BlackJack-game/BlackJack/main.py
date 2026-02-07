#importing all what we need:
import random, ascii, time


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

while True:

    #function to give user and computer 2 cards each but only 1 is shown for computer!!
    def give_cards():
        print(ascii.logo)
        char = input("Hey, and welcome to my BLACKJACK game. Type 'y' to start \n").lower()
        if char != "y":
            print("You entered a wrong input. Try Again!")
            choice = input("Do you want to retry?(y/n)").lower()
            if choice == "y":
                give_cards()
                user_score()
                computer_score()
                draw()
        user_cards.clear()
        computer_cards.clear()

        for x in range (2):

            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        print("Your cards: ", user_cards)
        print("Computer cards:", [computer_cards[0]])

        if 10 in user_cards and 11 in user_cards:
            print("Blackjack! You win")
            again = input("Do you want to play again?(y/n)?").lower()
            if again == "y":
                give_cards()
                user_score()
                computer_score()
                draw()

        elif 10 in computer_cards and 11 in computer_cards:
            print("Bench wins!")
            again = input("Do you want to play again?(y/n)?").lower()
            if again == "y":
                give_cards()
                user_score()
                computer_score()
                draw()

    #Ace card logic
    def ace_card():
        #user ace card deal
        total = sum(user_cards)
        while total > 21 and 11 in user_cards:
            user_cards[user_cards.index(11)] = 1
            total = sum(user_cards)
        #computer ace card deal
        tot_cmpt = sum(computer_cards)
        while tot_cmpt > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1
            tot_cmpt = sum(computer_cards)

    #looping through the cards and see if user want another one or stop
    def user_score():
        while True:
            user_choice = input("Do you want another card? Type 'y' or 'n'\n").lower()
            if user_choice == 'y':
                user_cards.append(random.choice(cards))
                calculate_total = sum(user_cards)
                print(f"Your cards are: {user_cards}")
                print(f"Your score is: {calculate_total}")

                if sum(user_cards) > 21:
                    print("You busted bro. try again!")
                    choice = input("Do you want to play again?(y/n)").lower()
                    if choice == "y":
                        time.sleep(0.5)
                        give_cards()
                        user_score()
                        computer_score()
                        draw()
                    elif choice == 'n':
                        print("GoodBye then, see you next time!")

            elif user_choice == 'n':
                print("I stand!")
                break

    #loopng through the cards and see if computer want another card
    def computer_score():
        total = sum(computer_cards)
        while total < 17:
            print("Computer picks a card:...")
            time.sleep(1.2)
            computer_cards.append(random.choice(cards))
            total = sum(computer_cards)
        while total > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1
            total = sum(computer_cards)

        user_total = sum(user_cards)
        ace_card()
        print("computer final cards:", computer_cards,"with a total of:", sum(computer_cards))
        print(f"Your final cards:", user_cards, "with a total of:", sum(user_cards))

        if sum(computer_cards) > 21:
            print("computer busted! You Win")
        elif sum(user_cards) > sum(computer_cards):
            print("You Win")
        elif sum(user_cards) < sum(computer_cards):
            print("computer Wins!")
        else:
            print("its a draw! try again!")

        choice = input("Do you want to play another game?(y/n)").lower()
        if choice == "y":
            give_cards()
            user_score()
            computer_score()
            draw()

    #looking if user and computer have the same score
    def draw():
        if sum(user_cards) == sum(computer_cards):
            print("Its a draw!")
            choice = input("Do you want to play another game?(y/n)").lower()
            if choice == "y":
                give_cards()
                user_score()
                computer_score()
                draw()

    break

give_cards()
user_score()
computer_score()
draw()
