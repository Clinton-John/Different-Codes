class Game():
    # def __init__(self):
    #     # self.user1_choice = user1_choice
    #     self.default_choice = 0

    def play_game(self , user_choice1, user_choice2):
        
        game_options = {
            1 : "rock",
            2 : "Paper",
            3 : "Sciccors"
        }
        print(f"User one selected {game_options[user_choice1]}")
        print(f"User two selected {game_options[user_choice2]}")

        # if (user_choice1 == 1 and user_choice2 == 1) or (user_choice1 == 2 and user_choice2 == 2) or (user_choice1 == 3 and user_choice2 == 3) :
        #     print(f"There is a tie of both users selecting {game_options[user_choice1]}")
        # elif (user_choice1 == 1 and user_choice2 == 2) :
        #     print(f"User2 wins the game with {game_options[user_choice2]} beating {game_options[user_choice1]} ")
        # elif (user_choice1 == 1 and user_choice2 == 3)  :
        #     print(f"User1 wins the game with {game_options[user_choice1]} beating {game_options[user_choice2]} ")
        # elif (user_choice1 == 2 and user_choice2 == 1):
        #     print(f"User1 wins the game with {game_options[user_choice1]} beating {game_options[user_choice2]} ")
        # elif (user_choice1 == 2 and user_choice2 == 3):
        #     print(f"User2 wins the game with {game_options[user_choice2]} beating {game_options[user_choice1]} ")
        # elif (user_choice1 == 3 and user_choice2 == 1):
        #     print(f"User2 wins the game with {game_options[user_choice2]} beating {game_options[user_choice1]} ")
        # elif (user_choice1 == 3 and user_choice2 == 2):
        #     print(f"User1 wins the game with {game_options[user_choice1]} beating {game_options[user_choice2]} ")


        ##Instead of using the above loop, we can use a dictionary to map the outcomes then check on them
        outcomes = {
            (1, 1): "It's a tie! Both selected Rock.",
            (1, 2): "User2 wins with Paper beating Rock.",
            (1, 3): "User1 wins with Rock beating Scissors.",
            (2, 1): "User1 wins with Paper beating Rock.",
            (2, 2): "It's a tie! Both selected Paper.",
            (2, 3): "User2 wins with Scissors beating Paper.",
            (3, 1): "User2 wins with Rock beating Scissors.",
            (3, 2): "User1 wins with Scissors beating Paper.",
            (3, 3): "It's a tie! Both selected Scissors."
        }

        # Determine the result using the outcomes dictionary
        result = outcomes[(user_choice1, user_choice2)]
        print(result)
 

    def get_choices(self):
        print("Select a choice below \n1.Rock  \n2.Paper  \n3. Scissors")
        self.user1_choice = int(input("Enter your choice User1 : "))
        self.user2_choice = int(input("Enter your choice User2 : "))
        return self.user1_choice, self.user2_choice

def main():
    newgame = Game()
    user_choices = newgame.get_choices()
    user_choice1 = user_choices[0]
    user_choice2 = user_choices[1]

    newgame.play_game(user_choice1, user_choice2)

if __name__ == '__main__':
    main()