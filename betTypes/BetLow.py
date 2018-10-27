from BetType import BetType


class BetLow(BetType):
    def multiplier(self):
        return 2

    def bet_success(self, number):
        if number == '0' or number == '00':
            return False
        return int(number) < 19

    def description(self):
        return 'The low numbers (1-18)'