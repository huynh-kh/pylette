import abc

class BetType:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def bet_success(self, number):
        """Should return true if the bet was successful and false otherwise"""
        return

    @abc.abstractmethod
    def multiplier(self):
        """Should return this multiplier for this bet"""
        return

    @abc.abstractmethod
    def description(self):
        """Should return a user-friendly description for this bet"""
        return
