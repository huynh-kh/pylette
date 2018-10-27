from BetType import BetType

class BetBlack(BetType):
    blackNumbers = [2, 4, 6, 8, 10, 11,
                      13, 15, 17, 20, 22, 24,
                      26, 28, 29, 31, 33, 35]

    def bet_success(self, number):
        return int(number) in self.blackNumbers

    def multiplier(self):
        return 2

    def description(self):
        return "Black numbers"