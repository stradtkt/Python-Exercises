import math
def make_change(cents):
    change = [
        ["Dollar", 100],
        ["Half-Dollar", 50],
        ["Quarter", 25],
        ["Dime", 10],
        ["Nickel", 5],
        ["Penny", 1]
    ]

    coins = {}
    for i in range(len(change)):
        coins[change[i][0]] = math.floor(cents/change[i][1])
        cents %= change[i][1]
    for coin in coins:
        print str(coin) + ": " + str(coins[coin])

make_change(1234)