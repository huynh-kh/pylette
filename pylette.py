#!/usr/bin/env python3

import os
from random import choice

# Define Statics
from betTypes.BetBlack import BetBlack
from betTypes.BetCombination import BetCombination
from betTypes.BetDozenHigh import BetDozenHigh
from betTypes.BetDozenLow import BetDozenLow
from betTypes.BetDozenMiddle import BetDozenMiddle
from betTypes.BetEven import BetEven
from betTypes.BetHigh import BetHigh
from betTypes.BetLow import BetLow
from betTypes.BetOdd import BetOdd
from betTypes.BetRed import BetRed
from betTypes.BetSingleNumber import BetSingleNumber
from betTypes.BetZero import BetZero

RULES = {}
RULES['RED'] = [1, 3, 5, 7, 9, 12,
                        14, 16, 18, 19, 21, 23,
                        25, 27, 30, 32, 34, 36]

RULES['BLACK'] = [2, 4, 6, 8, 10, 11,
                          13, 15, 17, 20, 22, 24,
                          26, 28, 29, 31, 33, 35]

RULES['ZERO'] = ['0', '00']
RULES['ANY'] = RULES['RED'] + RULES['BLACK'] + ['0'] + ['00']

NO = {'no','n', 'NO', 'No', 'nO', 'N'}

BETS = ['any', 'com', '1', '13', '25', 'even', 'odd', 'red', 'black', 'low', 'high', '0', '00']

# Bet multipliers, they can be changed depending on which rules you want to play with.

MULTIPLIER = {
    "even_or_odd":2,
    "low_or_high":2,
    "any":36,
    "combination":36, # divided later by the amount of nrs chosen
    "dozen": 3,
    "red_or_black":2,
    "zeros":18
}

"""

Rules:
- Description                           - var name
 'Dozen' = (1-12 / 13 - 24 / 25 - 36)   (dozen)
 'Even/Odd'                             (even_or_odd)
 'Low/High' = L:1-18 H:19-36            (low_or_high)
 'Any Number' = 1-36                    (any)
 'Combination of numbers'               (combination)
 'Red or black'                         (red_or_black)
 '0 or 00'                              (zeros)
"""

class Roulette:
    amount_of_players = 0
    turn = 0
    currency = '$'

    def __init__(self, nickname='Default Player', money=1000):
        self.nickname = str(nickname)
        self.money = money
        self.history = {}
        self.winnings_last_turn = 0
        self.total_winnings = 0
        self.bets = {}
        self.turn_list = []

        Roulette.amount_of_players += 1

    @staticmethod
    def spin():

        Roulette.turn += 1

        return choice(RULES['ANY'])

    @staticmethod
    def show_outcome(turn_outcome):
        pass


    def add_bet(self, bet_type, bet_amount):

        # Save in dict so it can be viewed later

        save_bet = {}

        save_bet['bet_type'] = bet_type
        save_bet['bet_amount'] = bet_amount

        self.turn_list.append(save_bet)

    def bet_outcome(self, turn_outcome):

        # Now let's have a look at what a player has won. (or lost xd)

        for bet in self.turn_list:
            bet['bet_amount'] = int(bet['bet_amount'])
            betType = bet['bet_type']
            if betType.bet_success(turn_outcome):
                bet['bet_winning'] = bet['bet_amount'] * betType.multiplier()
            else:
                bet['bet_winning'] = 0

        for bet in self.turn_list:
            self.total_winnings = self.total_winnings + bet['bet_winning']
            self.money = self.money + bet['bet_winning']

        # Let's append the turn array to the bets.

        self.bets[Roulette.turn] = self.turn_list

    def clear_list(self):
        self.turn_list.clear()


# Tests if user input is no
def read_yes_no():
    if input('[Yes]/[No] ') in NO:
        return False
    else:
        return True

# Function that checks if input from user is a valid roulette number
def test_between(low, high, number):
    try:
        low = int(low)
        high = int(high)
        number = int(number)
        if low <= number and number <= high:
            return True
    except:
        pass

    return False

print('Welcome to a game of roulette.')
nicknames = {}

while True:
    while True:
        nick_input = input('Enter nickname: ')
        if not nick_input:
            nick_input = 'Default Player'
        if nick_input in nicknames:
            print('That nickname already exists')
        else:
            nicknames[nick_input] = Roulette(nick_input)
            break

    print("List of players:")

    for key in nicknames:
        print(f' - {key} ( {nicknames[key].money}{Roulette.currency} )')

    print('\nWould you like to add another player?')
    if not read_yes_no():
        break

# Players are created. Objects are initialized.





def play():
    turn_outcome = Roulette.spin()
    additional_bet = 1
    for key in nicknames:


        # Because a player can do additional bets in 1 turn, inf loop
        while True:

            print(f"Turn: {Roulette.turn}, bet #{additional_bet}")
            print('---------------')
            print(f'Player: {nicknames[key].nickname} needs to place a bet')
            print(f'You have {nicknames[key].money}{Roulette.currency}')
            print('---------------')

            while True:
                bet = input('''Do you want to bet [any] number, [com]bination of numbers (up to 6) [1]-12, [13]-24, [25]-36,   
                     [even], [odd], [red], [black], [low], [high], [0], [00]
                      Enter choice : ''')
                if bet in BETS:
                    break
                print('Invalid choice. Please try again.')

            # Handle combination logic

            if bet == 'com' or bet == 'Com' or bet == 'COM':
                invalid = True
                while invalid:
                    nr = input('Enter up to six numbers, seperated by a comma (,)  : ')
                    if nr.count(',') < 1 or nr.count(',') >= 7:
                        print('Please pick 2-6 choices')
                    else:
                        bet_choice = []
                        bet_choice = nr.split(',')
                        for choice in bet_choice:
                            if not test_between(1, 36, choice):
                                print('Invalid input, example: 2,8,32')
                                invalid = True
                                break
                            invalid = False
                        if not invalid:
                            nr = None
                            bet_type = BetCombination(list(map(int, bet_choice)))
                            break

            # Handle 'any' logic
            if bet == 'any' or bet == 'Any' or bet == 'ANY':
                while True:
                    bet_choice = input('Which number would you like to bet on? [1-36]: ')
                    # Test if input is a number
                    valid = test_between(1, 36, bet_choice)
                    if valid:
                        bet_type = BetSingleNumber(bet_choice)
                        break
                    else:
                        print('Please enter a value between 1-36')

            # Handle dozen logic
            if bet == '1':
                bet_type = BetDozenLow()

            if bet == '13':
                bet_type = BetDozenMiddle()
            if bet == '25':
                bet_type = BetDozenHigh()

            if bet == 'red':
                bet_type = BetRed()

            if bet == 'black':
                bet_type = BetBlack()

            if bet == 'even':
                bet_type = BetEven()

            if bet == 'odd':
                bet_type = BetOdd()

            if bet == 'low':
                bet_type = BetLow()

            if bet == 'high':
                bet_type = BetHigh()

            if bet == '00' or bet == '0':
                bet_type = BetZero()

            while True:
                bet_amount = input(f'How much would you like to bet? [1-{nicknames[key].money}] ')
                # Test if input is a number
                if test_between(1, nicknames[key].money, bet_amount):
                    break
                else:
                    print('Invalid input')

            nicknames[key].add_bet(bet_type, bet_amount)

            nicknames[key].money = nicknames[key].money - int(bet_amount)

            additional_bet += 1

            del bet_type, bet_amount

            # Check if user wants another bet
            if nicknames[key].money > 0:
                print('Make another bet?')
                if not read_yes_no():
                    additional_bet = 1
                    break
            else:
                print('You went all in! You can\'t make another bet!')
                break


        nicknames[key].bet_outcome(turn_outcome)

    print(f"""
    ------
    End of turn {Roulette.turn}
    Chosen number: {turn_outcome}
    -------
    """)
    for key in nicknames:
        print(f'Player: {nicknames[key].nickname}')
        for i in range(len(nicknames[key].turn_list)):
            print(f"""
             -> Chosen: {nicknames[key].turn_list[i]['bet_type'].description()}
             -> Bet amount: {nicknames[key].turn_list[i]['bet_amount']}
             -> Winnings: {nicknames[key].turn_list[i]['bet_winning']}
             -> Money after round: {nicknames[key].money}
            """)

        nicknames[key].clear_list()
playing = True

while playing:
    for key in nicknames:
        if nicknames[key].money < 1:
            print(f'Player: {nicknames[key].nickname} is broke, you lost!')
            playing = False
            break
        else:
            play()
