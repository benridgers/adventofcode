import fileinput

def main():
    results = [];
    res = 0;
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        if(line=='\n'):
            results.append(res)
            res = 0
        else:
            res += int(line)
    results.sort()
    print(results[-3:])

if __name__ == "__main__":
    main()
