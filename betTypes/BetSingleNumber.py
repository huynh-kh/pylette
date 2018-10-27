from BetType import BetType


class BetSingleNumber(BetType):
    def __init__(self, number):
        self.number = number

    def bet_success(self, number):
        return int(number) == int(self.number)

    def multiplier(self):
        return 36