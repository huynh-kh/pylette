from BetType import BetType


class BetCombination(BetType):
    def __init__(self, numbers):
        self.numbers = numbers

    def bet_success(self, number):
        return int(number) in self.numbers

    def multiplier(self):
        return 36 / len(self.numbers)

    def description(self):
        return "Any of the following numbers: " + ','.join(str(e) for e in self.numbers)