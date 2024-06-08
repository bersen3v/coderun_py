

def sort(list: list) -> list:
    if len(list)<2:
        return list
    
    centr = list.pop(0)
    left = []
    right = []

    for i in list:
        if i<=centr: left.append(i)
        else: right.append(i)
    
    return sort(left) + [centr] + sort(right)

input = list(map(int, input().split()))
print(sort(input)[1])