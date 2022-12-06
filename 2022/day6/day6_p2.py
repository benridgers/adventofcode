import re

def main():
    f = open("input.txt", "r")
    line = f.readlines()[0]
    
    for i in range(14,len(line)):
        if(allDifferent(line[i-14:i])):
            print(i)
            break
            
def allDifferent(s):
    chars = ""
    for c in s:
        if chars.find(c)!=-1:
            return False
        else:
            chars=chars+c
    return True

if __name__=="__main__":
    main()
