import random
data = 0
firsttotal = 100
firstbet = 1
bet = firstbet

# print(f'\nyou start with {total}\n')

for games in range(100):

    total = firsttotal

    for i in range(5):
        # print('initial total',total)
        # print('bet', bet)
        total -= bet
        # print('total',total)
        flip = random.randint(0,37)
        # print('roll',flip)
        if flip == 0 or flip == 37:
            bet = 2*bet
            # print('ZERO')
        elif flip%2 == 0:
            # print('EVEN')
            total += 2*bet
            bet = firstbet
        elif flip%2 == 1:
            # print('ODD')
            bet = 2*bet
        else:
            # print('ERROR')
            break
        # print('final total',total,'\n')
        if total < 0:
            # print('You broke son')
            total = 0
            break
    
    # print('final total',total-100,'\n')
    
    # data.append(total)
    data += (total-100)

print(data)
# print(sum(data)/len(data))