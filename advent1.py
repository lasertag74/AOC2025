import re
def main():
    total = 50
    final = 0
    lines = 0
    with open("AdventFile1.txt", "r") as f:
        for line in f:
            lines += 1
            match = re.match(r"([A-Za-z])(\d+)", line)
            leftRight = match.group(1)
            value = int(match.group(2))
            print(leftRight, value)
            curr = total
            if leftRight == "L":
                final += differenceP(curr,-1*value, lines)
                total -= value   
            elif leftRight == "R":
                final += differenceP(curr,value, lines)
                total += value
             
            

            total = total % 100
               
    print(final)



def differenceP(a, b, c):
    print(a+b)
    if (a+b >= 100):
        print(c)
        return (a+b)//100
    
    elif(a+b<0):
        b=abs(b)
        if(a!=0):
            a=100-a
        print(c)
        return (a+b)//100
    else:
        if (a+b == 0):
            print(c)
            return 1
            
        else:
            
            return 0
    

main()