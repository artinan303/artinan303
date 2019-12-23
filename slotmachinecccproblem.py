quarters = int(input("Input the number of quarters Martha has: "))
inputs = "Input the number of times machine "
M1Use = int(input(inputs + "1 has been used:"))
M2Use = int(input(inputs + "2 has been used:"))
M3Use = int(input(inputs + "3 has been used:"))
use = 1
total = 0


class Machine:
    def __init__(self, used, pay, payout):
        self.used = used
        self.pay = pay
        self.payout = payout


M1 = Machine(M1Use, 30, 35)
M2 = Machine(M2Use, 60, 100)
M3 = Machine(M3Use, 9, 10)

while quarters > 0:
    if use == 1:
        print("Martha plays slot 1")
        if M1.used == M1.payout:
            quarters += M1.payout
            M1.used = 0
            print("payout")
        M1.used += 1
        quarters -= 1
        total += 1
    elif use == 2:
        print("Martha plays slot 2")
        if M2.used == M2.payout:
            quarters += M2.payout
            M2.used = 0
            print("payout")
        M2.used += 1
        quarters -= 1
        total += 1
    elif use == 3:
        print("Martha plays slot 3")
        if M3.used == M3.payout:
            quarters += M3.payout
            M3.used = 0
            print("payout")
        M3.used += 1
        quarters -= 1
        total += 1
    use += 1
    if use >= 4:
        use = 1
print("Martha plays " + str(total) + " times before going broke")
