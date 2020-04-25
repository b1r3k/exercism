# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guessed = []

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError(self.status)
        if char not in self.word or char in self.guessed:
            self.remaining_guesses -= 1
        else:
            self.guessed.append(char)

    def get_masked_word(self):
        masked = []
        for c in self.word:
            if c in self.guessed:
                masked.append(c)
            else:
                masked.append('_')
        return ''.join(masked)

    def get_status(self):
        if self.remaining_guesses < 1:
            self.status = STATUS_LOSE
        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN
        return self.status
