
def main():
    final = 0
    lines = 0
    joltSize = 12
    with open("AdventFile1.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            lines += 1
            currLine = list(line)
            i = 0
            while i < len(currLine):
                currLine[i] = int(currLine[i])
                i += 1

            jolt = [1] * joltSize
            
            
            
            j = 0
            fl = len(currLine)
            
            while j < fl:
                
                k = joltSize-1
                while k >= 0:
                    
                    if (currLine[j] > jolt[k] and (fl - j) > joltSize - (1+k)):
                        
                        jolt[k] = currLine[j]
                        if k < joltSize - 1:
                            cleaner = k + 1
                            while(cleaner < joltSize):
                                
                                jolt[cleaner] = 1
                                cleaner += 1     
                    k-=1
                j += 1
            
            l = 0
            currJolt = 0
            while (l < joltSize):
                currJolt += (jolt[l] * 10**(joltSize - (1+l)))
                l += 1
            
            final += currJolt
    print(final)        





main()
