
counter = 0
def search(yMax: int, xMax: int, yPos : int = 0, xPos: int = 0):
    if xPos>=xMax or yPos>=yMax:
        return
    if xPos == xMax-1 and yPos == yMax-1:
        global counter
        counter += 1
        return
    
    search(xPos=xPos+1, yPos=yPos+2, yMax=yMax, xMax=xMax)
    search(xPos=xPos+2, yPos=yPos+1, yMax=yMax, xMax=xMax)
        
# yMax, xMax = list(map(int, input().split()))
yMax, xMax = 6,8
search(yMax=yMax, xMax=xMax)
print(counter)