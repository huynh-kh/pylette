from BetType import BetType


class BetZero(BetType):
    def bet_success(self, number):
        return number == '0' or number == '00'

    def multiplier(self):
        return 18

    def description(self):
        return 'Zero or double zero'