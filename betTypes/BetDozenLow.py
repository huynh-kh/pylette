from BetType import BetType


class BetDozenLow(BetType):
    def bet_success(self, number):
        if number == '0' or number == '00':
            return False
        return int(number) < 13

    def multiplier(self):
        return 3