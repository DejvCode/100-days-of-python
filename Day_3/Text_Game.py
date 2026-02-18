def start_game():

    print("\n--- New Journey Begins ---")
    print("You are in a dark forest, you see two paths. Do you want to go left or right?")
    path = input("Type 'left' or 'right': ").lower().strip()

    if path == "left":
        print("You encounter a wild bear! Do you want to fight or run?")
        action = input("Type 'fight' or 'run': ").lower().strip()
        if action == "fight":
            print("You fought bravely but the bear was too strong. You lost.")
        elif action == "run":
            print("You ran away safely and found a hidden treasure! You win!")
        else:
            print("Invalid action. The bear got you while you were confused.")

    elif path == "right":
        print("You found a peaceful village. Do you want to explore or rest?")
        action = input("Type 'explore' or 'rest': ").lower().strip()
        if action == "explore":
            print("You explored the village and found a hidden treasure! You win!")
        elif action == "rest":
            print("You rested and were attacked by bandits. You lost.")
        else:
            print("Invalid action. Game over.")
    else:
        print("Invalid path. You got lost in the woods forever.")

if __name__ == "__main__":
    print("Welcome to the treasure hunting game!")
    
    choice = input("Do you wanna start your journey? [Y/N]\n").upper().strip()
    
    if choice == "Y":
        while True:
            start_game()
            
            restart = input("\nDo you want to play again? [Y/N]\n").upper().strip()
            if restart != "Y":
                print("Thanks for playing! Goodbye!")
                break
    else:
        print("Maybe next time! Goodbye!")