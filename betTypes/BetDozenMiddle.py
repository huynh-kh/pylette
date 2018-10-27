from BetType import BetType


class BetDozenMiddle(BetType):
    def bet_success(self, number):
        if number == '0' or number == '00':
            return False
        return 12 < int(number) < 25

    def multiplier(self):
        return 3

    def description(self):
        return 'The second dozen (13-24)'