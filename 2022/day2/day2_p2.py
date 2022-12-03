import fileinput

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    res = 0
    for line in lines:
        #A,X = Rock
        #B,Y = Paper
        #C,Z = Scissors
        #X = LOSE
        #Y = DRAW
        #Z = WIN
        p1 = line[0]
        p2 = line[2]
        res += points(p1,p2)
    print(res)

def points(p1, p2):
    if(p1=="A"):
        if(p2=="X"):#C
            return 0+3
        elif(p2=="Y"):#A
            return 3+1
        else: #B
            return 6+2
    elif(p1=="B"):
        if(p2=="X"):#A
            return 0+1
        elif(p2=="Y"):#B
            return 3+2
        else:#C
            return 6+3
    elif(p1=="C"):
        if(p2=="X"):#B
            return 0+2
        elif(p2=="Y"):#C
            return 3+3
        else:#A
            return 6+1
    return 0

if __name__ == "__main__":
    main()
