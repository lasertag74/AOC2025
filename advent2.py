
def main():
    text="1061119-1154492,3-23,5180469-5306947,21571-38630,1054-2693,141-277,2818561476-2818661701,21177468-21246892,40-114,782642-950030,376322779-376410708,9936250-10074071,761705028-761825622,77648376-77727819,2954-10213,49589608-49781516,9797966713-9797988709,4353854-4515174,3794829-3861584,7709002-7854055,7877419320-7877566799,953065-1022091,104188-122245,25-39,125490-144195,931903328-931946237,341512-578341,262197-334859,39518-96428,653264-676258,304-842,167882-252124,11748-19561"
    final =0
    CurrRange = text.split(",")
    for twoNum in CurrRange:
        balsy = twoNum.split("-")
        print(twoNum)
        final += Range(int(balsy[0]),int(balsy[1]))
    print(final)


def Range(a, b):
    total = 0
    debug = 0
    while (a <= b):
        currInt = str(a)
        if(all_equal(list(currInt)) and a > 9):
                print(a)
                total += a
        elif(len(currInt) == (6) or (len(currInt)) == 9):
            third1, third2, third3 = currInt[:len(currInt)//3],currInt[len(currInt)//3:2* len(currInt)//3],currInt[2* len(currInt)//3:]
            if(int(third1) == int(third2) and int(third1) == int(third3)):
                print(a)
                total += a        
        elif(len(currInt) == (8)):
            fourth1, fourth2, fourth3, fourth4 = currInt[:2],currInt[2:4],currInt[4:6],currInt[6:]
            if(int(fourth1) == int(fourth2) and int(fourth3) == int(fourth1) and int(fourth1) == int(fourth4)):
                print(a)
                total += a
            else:
                half1, half2 = currInt[:len(currInt)//2 + len(currInt)%2], currInt[len(currInt)//2 + len(currInt)%2:]
                if (a > 9) and (int(half1) == int(half2)):
                    print(a)
                    total += a
        elif(len(currInt) == (10)):
            fifth1, fifth2, fifth3, fifth4, fifth5 = currInt[:2],currInt[2:4],currInt[4:6],currInt[6:8],currInt[8:]
            if(int(fifth1) == int(fifth2) and int(fifth3) == int(fifth1) and int(fifth1) == int(fifth4)and int(fifth1) == int(fifth5)):
                print(a)
                total += a
            else:
                half1, half2 = currInt[:len(currInt)//2 + len(currInt)%2], currInt[len(currInt)//2 + len(currInt)%2:]
                if (a > 9) and (int(half1) == int(half2)):
                    print(a)
                    total += a        
        else:
            half1, half2 = currInt[:len(currInt)//2 + len(currInt)%2], currInt[len(currInt)//2 + len(currInt)%2:]
            if (a > 9) and (int(half1) == int(half2)):
                print(a)
                total += a
        
        a += 1
    print(debug)
    return total

# Source - https://stackoverflow.com/a
# Posted by kennytm, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-02, License - CC BY-SA 4.0

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)

    

main()