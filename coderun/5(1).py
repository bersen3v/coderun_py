import random


variants : dict[int, list[dict]] = {}

# primer = {
#     10: [{'spend': 10, 'coupons': 0, 'spendCoupons':[]},
#          {'spend': 10, 'coupons': 0, 'spendCoupons':[]},]
# }

def createTest():
    n = 10
    mas = []
    for i in range(n):
        mas.append(1)
    return n,mas

def buyForMoney(money: int):
    global variants
    last = variants[list(variants.keys())[-1]]
    answer = []
    coupons = 0
    if costOfLunch>100:
        coupons=1
    for lastVar in last:
        answer.append(
            {
                'spend': money + lastVar['spend'],
                'coupons': lastVar['coupons'] + coupons,
                'spendCoupons' : lastVar['spendCoupons'],
            }
        )
    return answer

def buyForCoupon():
    global variants
    last = variants[list(variants.keys())[-1]]
    answer = []
    for lastVar in last:
        if lastVar['coupons'] > 0:
            answer.append(
                {
                    'spend': lastVar['spend'],
                    'coupons': lastVar['coupons'] - 1,
                    'spendCoupons': lastVar['spendCoupons'] + [len(list(variants.keys()))+1],
                }
            )
    return answer


n, mas = createTest()
counter = 0
for i in range(n):
    counter+=1
    costOfLunch = mas[i]

    if list(variants.keys()) == []:
        coupons = 0
        if costOfLunch>100:
            coupons=1
        variants[costOfLunch] = [{
            'spend': costOfLunch,
            'coupons': coupons,
            'spendCoupons':[]
        }]
    else:
        variants[counter] = buyForMoney(costOfLunch) + buyForCoupon()

print(variants)
if variants!={}:
    bestVar = 0
    minSpend = variants[list(variants.keys())[-1]][0]['spend']

    for variant in variants[list(variants.keys())[-1]]:
        if variant['spend'] <= minSpend:
            bestVar = variant
            minSpend = variant['spend']
    
    if bestVar!=0:
        print(bestVar['spend'])
        print(bestVar['coupons'], len(bestVar['spendCoupons']))
        for date in bestVar['spendCoupons']:
            print(date)
    else:
        print(0)
        print(0, 0)

else:
    print(0)
    print(0, 0)
        
print()
    