import re

def main():
    f = open("input.txt", "r")
    lines = f.readlines()

    res = 0
    for line in lines:
        pairs = re.split(',|-|\n',line)[:4]
        if overlap(int(pairs[0]),int(pairs[1]),int(pairs[2]),int(pairs[3])):
            res+=1
    print(res)

def overlap(a0,a1,b0,b1):
    if(a0>=b0 and a1<=b1) or (b0>=a0 and b1<=a1):
        return True
    return False

if __name__=="__main__":
    main()
