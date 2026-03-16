import random


def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player, computer):
    """Return 'player', 'computer', or 'tie' based on choices."""
    if player == computer:
        return "tie"
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return "player" if wins[player] == computer else "computer"


def display_score(stats):
    """Print the current score."""
    total = sum(stats.values())
    print(
        f"Score → Wins: {stats['wins']} | "
        f"Losses: {stats['losses']} | "
        f"Ties: {stats['ties']} | "
        f"Total: {total}\n"
    )


def play_game():
    """Main game loop."""
    stats = {"wins": 0, "losses": 0, "ties": 0}
    valid_choices = ["rock", "paper", "scissors"]

    print("=" * 35)
    print("      🎮 Rock Paper Scissors!")
    print("=" * 35)
    print("Type 'quit' to exit\n")

    while True:
        player = input("Your choice (rock/paper/scissors): ").lower().strip()

        if player == "quit":
            break

        if player not in valid_choices:
            print("❗ Invalid choice! Please enter rock, paper, or scissors.\n")
            continue

        computer = get_computer_choice()
        result = determine_winner(player, computer)

        print(f"\nYou chose:      {player}")
        print(f"Computer chose: {computer}")

        if result == "player":
            print("✅ You win!")
            stats["wins"] += 1
        elif result == "computer":
            print("❌ Computer wins!")
            stats["losses"] += 1
        else:
            print("🤝 It's a tie!")
            stats["ties"] += 1

        display_score(stats)

    print("=" * 35)
    print("         Thanks for playing!")
    print(f"  Final: {stats['wins']}W / {stats['losses']}L / {stats['ties']}T")
    print("=" * 35)


if __name__ == "__main__":
    play_game()
