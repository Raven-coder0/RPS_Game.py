import random # we import random module to use the "random" function in code later.

def greetings():         # here we will greet the player when the game starts to run.
    name = input("enter your name:")
    print("-"*100)
    print(f"\t\t\t\tHello 👋, {name} ")
    print()
    return "/////////////////////////////let`s start the game ^_^ /////////////////////////////"

def get_choices():
        print("-"*100)
        player = input("enter your choice frome (rock,paper,scissors):\t")
        print()
        options = ["rock","paper","scissors"]
        computer = random.choice(options)  # the random function select a random item from the "option list" .
        choices = {"player":player, "computer":computer}
        return choices

def check_win(player,computer): # Here we will compare the results of player & computer to announce who is the winner.
        print(f"you chose {player}, computer chose {computer}")
        print()
        if player == computer:
                return "its a tie"
        elif player == "rock":
                if computer == "scissors":
                        return """rock smashes scissors 
                            
                            !!!YOU WIN🎉🎉!!!"""
                else:
                        return """paper covers rock 
                            
                            !!!YOU LOSE💀💀!!!"""
        elif player == "paper":
                if computer == "rock":
                        return """paper covers rock
                            
                            !!!YOU WIN🎉🎉!!!"""
                else:
                        return """scissors cuts paper
                           
                            !!!YOU LOSE💀💀!!!"""
        elif player == "scissors":
                if computer == "paper":
                        return """scissors cuts paper
                            
                            !!!YOU WIN🎉🎉!!!"""
                else:
                        return """rock smashes scissors
                            
                            !!!YOU LOSE💀💀!!!"""
print(greetings())                
choices = get_choices()                # Here we are calling "get_choices()" to know the optins that are selected.
result = check_win(choices["player"],choices["computer"])      # here we are tranfering the "player & computer" data to "check_win()".
print(result)
print()


        

        