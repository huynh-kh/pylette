from BetType import BetType


class BetCombination(BetType):
    def __init(self, numbers):
        self.numbers = numbers

    def bet_success(self, number):
        return int(number) in self.numbers

    def multiplier(self):
        return 36 / len(self.numbers)