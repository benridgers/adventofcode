def main():
    f = open("input.txt", "r")
    lines = f.readlines()

    res = 0
    for i in range(0,len(lines),3):
        b1 = lines[i]
        b2 = lines[i+1]
        b3 = lines[i+2]
        for i in b1:
            if(b2.find(i)!=-1 and b3.find(i)!=-1):
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
