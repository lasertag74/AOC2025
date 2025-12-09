import math
import re
def main():
    final = 0
    lines = 0
    ArrayBase = []
    AllBase = []  
    with open("AdventFil3.txt", "r") as f:
        for line in f.readlines():
            
            AllBase.append(list(line))
            line = line.strip()
            currLine = re.split(r'\s+', line)
            ArrayBase.append(currLine)
            
            lines += 1
    
    index = 0
    h = 0
    while (h < len(ArrayBase[0])):
        k = 0
        max = 0
        while(k < len(ArrayBase) - 1):
            if(max < len(ArrayBase[k][h])):
                max = len(ArrayBase[k][h])
            
            k+=1
        
        CurrBase = [row[index:index+max] for row in AllBase[0:4]] 
        print(CurrBase)
        nums = []
        p = len(CurrBase[0])-1
        while(p > - 1):
             num = ""
             q = 0
             while(q < len(CurrBase)):
                 num += CurrBase[q][p]
                 q+=1
             nums.append(int(num))
             p-=1
        print(nums)
        
        if(ArrayBase[4][h] == "+"):
            final += sum(nums)
        elif(ArrayBase[4][h] == "*"):
            final += math.prod(nums)    




        index+=(max+1)
        h+=1
    print(final)
    
main()
