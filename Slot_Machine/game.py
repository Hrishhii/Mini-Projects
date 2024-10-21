import random

symbols = [['🍒', '🔔', '🍒', '🌟', '🔔', '🍒'],
           ['🍒', '🔔', '🍒', '🌟', '🔔', '🍒'],
           ['🍒', '🔔', '🍒', '🌟', '🔔', '🍒']]

def spin(symbols, depo, b):
    three = [random.choice(i) for i in symbols]
    print(f"{three[0]}   {three[1]}   {three[2]}")
    if three[0] == three[1] == three[2] == '🍒':
        depo += b * 1.5
    
    elif three[0] == three[1] == three[2] == '🔔':
        depo += b * 2
    
    elif three[0] == three[1] == three[2] == '🌟':
        depo += b * 3
    
    else:
        depo -= b
    return depo
        

def deposit():
    while True:
        try:
            depo = int(input("Enter amount to deposit: $"))
            if depo <= 0:
                print("Deposit amount must be positive.")
            else:
                break
        except ValueError:
            print("Invalid input amount.")
    return depo
            
def bet(depo):
    while True:
        try:
            b = int(input("How much would you like to bet: $"))
            if b > depo:
                print("bet exceeds deposit amount.")
            elif b <= 0:
                print("bet amount must be positive.")
            else:
                break
        except ValueError:
            print("Enter valid amount")
    
    return b
    

def main():
    depo = deposit()
    while input("Press enter to play (q to quit): ") != 'q':
        b = bet(depo)
        print(f"Bet amount: ${b}")
        depo = spin(symbols, depo, b)
        print(f"Current balence: ${depo}")
        if depo == 0:
            print("No money left to bet.")
            break

if __name__ == "__main__":
    main()