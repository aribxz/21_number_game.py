import random

def game():
    print("🎮 Welcome to the 21 Number Game!")
    print("Try not to say 21 — the one who says it loses!")
    
    current = 0
    turn = random.choice(['player', 'computer'])
    print(f"\n👉 {turn.capitalize()} goes first!")

    while current < 21:
        if turn == 'player':
            max_allowed = min(3, 21 - current)
            while True:
                try:
                    count = int(input(f"\nIt's your turn. How many numbers do you want to say? (1-{max_allowed}): "))
                    if count < 1 or count > max_allowed:
                        raise ValueError
                    break
                except ValueError:
                    print(f"Please enter a number between 1 and {max_allowed}.")
            
            numbers = [str(current + i) for i in range(1, count + 1)]
            current += count
            print("You said:", ' '.join(numbers))

            if current >= 21:
                print("😞 You said 21. You lose!")
                break

            turn = 'computer'

        else:
            count = random.randint(1, min(3, 21 - current))
            numbers = [str(current + i) for i in range(1, count + 1)]
            current += count
            print("\nComputer's turn...")
            print("Computer said:", ' '.join(numbers))

            if current >= 21:
                print("🎉 Computer said 21. You win!")
                break

            turn = 'player'

game()
