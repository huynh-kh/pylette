from BetType import BetType


class BetDozenHigh(BetType):
    def bet_success(self, number):
        if number == '0' or number == '00':
            return False
        return int(number) > 24

    def multiplier(self):
        return 3

    def description(self):
        return 'The third dozen (25-36)'