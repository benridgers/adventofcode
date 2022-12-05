import re

def main():
    f = open("input.txt", "r")
    lines = f.readlines()

    crates=[]
    for i in range (0,len(lines[0])//4):
        crates.append([])

    for line in lines:
        if(line[0]!='m'):
            c=0
            for i in range(1,len(line),4):
                if(line[i]!=None and line[i].isupper()):
                    crates[c].append(line[i])
                c+=1
        else:
            test = [i for i in re.split(' |\n',line) if i.isdigit()]
            n = int(test[0])
            s1 = int(test[1])-1
            s2 = int(test[2])-1
            for i in range(0,n):
                crates[s2].insert(0,crates[s1].pop(0)) 

    print(crates)
    for c in crates:
        print(c[0])
            

if __name__=="__main__":
    main()
