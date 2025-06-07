# cook your dish here
#14 games; 2 points for winner, 0 for loser and 1 each if draw 
#total prize = 100x; winner = 60x; loser = 40x
def who_won(results):
    carlsen = 0
    draw = 0 
    chef = 0
    for char in results:
        if char == 'C':
            carlsen+=1 
        elif char == 'N':
            chef += 1 
        else:
            draw += 1 
    
    if carlsen > chef:
        winner = "carlsen"
    elif chef > carlsen:
        winner = "chef"
    else:
        winner = "draw"
    return winner
    
t = int(input())
while t>0:
    x = int(input())
    results = input()
    if who_won(results) == "carlsen":
        prize = 60*x
    elif who_won(results) == "chef":
        prize = 40*x
    elif who_won(results) == "draw":
        prize = 55*x

    print(prize)
    t-=1
