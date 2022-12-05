import re

def main():
    f = open("input.txt", "r")
    lines = f.readlines()

    res = 0
    for line in lines:
        pairs = re.split(',|-|\n',line)[:4]
        res += overlap(int(pairs[0]),int(pairs[1]),int(pairs[2]),int(pairs[3]))
    print(res)

def overlap(a0,a1,b0,b1):
    if(a0>=b0 and a1<=b1) or (b0>=a0 and b1<=a1):
        return 1
    return 0

if __name__=="__main__":
    main()
