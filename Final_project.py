import random

# -------------------- CLASS --------------------
class GameRecord:
    def __init__(self, name, attempts, difficulty, result):
        self.name = name
        self.attempts = attempts
        self.difficulty = difficulty
        self.result = result

    def __str__(self):
        return f"Attempts: {self.attempts} | Difficulty: {self.difficulty} | Result: {self.result}"


# -------------------- FILE HANDLING --------------------
def save_record(name, attempts, difficulty, result):
    with open("records.txt", "a") as file:
        file.write(f"{name},{attempts},{difficulty},{result}\n")


def view_records():
    try:
        records = {}

        with open("records.txt", "r") as file:
            for line in file:
                name, attempts, difficulty, result = line.strip().split(",")

                if name not in records:
                    records[name] = []

                # Use GameRecord class here
                record = GameRecord(name, int(attempts), difficulty, result)
                records[name].append(record)

        print("\n--- Player Records ---")

        for name, games in records.items():
            wins = sum(1 for g in games if g.result == "Win")
            losses = len(games) - wins

            print(f"\n{name} (Wins: {wins}, Losses: {losses}):")
            for i, game in enumerate(games, 1):
                print(f"  Game {i} | {game}")

    except FileNotFoundError:
        print("No records found yet.")


# -------------------- GAME LOGIC --------------------
def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1-50, unlimited attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")
    
    while True:
        choice = input("Enter choice (1/2/3): ")
        
        if choice == "1":
            return 1, 50, None, "Easy"
        elif choice == "2":
            return 1, 100, 10, "Medium"
        elif choice == "3":
            return 1, 200, 7, "Hard"
        else:
            print("Invalid choice. Try again.")


def get_valid_guess(low, high):
    while True:
        try:
            guess = int(input(f"Enter your guess ({low}-{high}): "))
            if low <= guess <= high:
                return guess
            else:
                print("Out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    name = input("\nEnter your name: ")
    low, high, max_attempts, difficulty = choose_difficulty()
    number = random.randint(low, high)
    attempts = 0

    print(f"\nI have selected a number between {low} and {high}.")

    while True:
        guess = get_valid_guess(low, high)
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            save_record(name, attempts, difficulty, "Win")
            break

        # Show remaining attempts
        if max_attempts:
            remaining = max_attempts - attempts
            print(f"Attempts left: {remaining}")

        if max_attempts and attempts >= max_attempts:
            print(f"❌ Out of attempts! The number was {number}.")
            save_record(name, attempts, difficulty, "Loss")
            break


# -------------------- MAIN MENU --------------------
def main():
    print("🎯 Welcome to the Number Guessing Game!")

    while True:
        print("\n1. Play Game")
        print("2. View Records")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()