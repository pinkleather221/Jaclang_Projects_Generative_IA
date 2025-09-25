# guess-the-number-game.jac

import random;

obj Game {
    has attempts: int = 3;
    has won: bool = False;

    def play {
        print("Game started!");
    }
}

obj GuessTheNumberGame (Game) {
    has correct_number: int = random.randint(1, 10);

    override def play {
        print("Welcome to Guess the Number!");
        while self.attempts > 0 {
            guess = input("Enter your guess (1-10): ");
            if guess.isdigit() {
                guess = int(guess);
                if guess == self.correct_number {
                    print("You guessed it!");
                    self.won = True;
                    break;
                } else {
                    print("Wrong guess!");
                    self.attempts -= 1;
                    print(f"Attempts left: {self.attempts}");
                }
            } else {
                print("Invalid input! Please enter a number.");
            }
        }
        if not self.won {
            print(f"Game over! The number was {self.correct_number}");
        }
    }
}

with entry {
    game = GuessTheNumberGame();
    game.play();
}
