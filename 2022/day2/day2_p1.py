import fileinput

def main():
    with open('input.txt') as f:
        lines = f.readlines()
    res = 0
    for line in lines:
        #A,X = Rock
        #B,Y = Paper
        #C,Z = Scissors
        p1 = line[0]
        p2 = line[2]
        res += points(p1,p2)
    print(res)

def points(p1, p2):
    if(p1=="A"):
        if(p2=="X"):
            return 3+1
        elif(p2=="Y"):
            return 6+2
        else:
            return 0+3
    elif(p1=="B"):
        if(p2=="X"):
            return 0+1
        elif(p2=="Y"):
            return 3+2
        else:#C
            return 6+3
    elif(p1=="C"):
        if(p2=="X"):
            return 6+1
        elif(p2=="Y"):
            return 0+2
        else:
            return 3+3
    return 0

if __name__ == "__main__":
    main()
