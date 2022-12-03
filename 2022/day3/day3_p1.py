def main():
    f = open("input.txt", "r")
    lines = f.readlines()

    res = 0
    for line in lines:
        l = len(line)
        c1 = line[:l//2]
        c2 = line[l//2:]
        for i in c1:
            if(c2.find(i)!=-1):
                res+=priority(i)
                break
    print(res)

def priority(i):
    if(i.islower()):
        return(ord(i)-96)
    if(i.isupper()):
        return(ord(i)-38) 

if __name__=="__main__":
    main()
