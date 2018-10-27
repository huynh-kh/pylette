from BetType import BetType

class BetRed(BetType):
    redNumbers = [1, 3, 5, 7, 9, 12,
                  14, 16, 18, 19, 21, 23,
                  25, 27, 30, 32, 34, 36]

    def bet_success(self, number):
        return int(number) in self.redNumbers

    def multiplier(self):
        return 2
