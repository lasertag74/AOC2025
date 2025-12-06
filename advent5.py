
def main():
    total = 0
    freshList = []
    #intList = []
    #with open("AdventFile1.txt", "r") as f:
      #  for line in f.readlines():
       #    line = line.strip()
            
         #   intList.append(int(line))
    with open("AdventFil3.txt", "r") as g:
        for linem in g.readlines():
            linem = linem.strip()
            dates = [2]
            dates = linem.split("-")
            freshList.append(dates)
    #print(freshList)
    #print(intList)
    #i = 0
    #while(i < len(intList)):
        #print(i)
        #j = 0
        #found=True
        #while(j < len(freshList) and found):
            #if(intList[i] >= int(freshList[j][0]) and intList[i] <= int(freshList[j][1])):
                #print(intList[i])
                #j+=1

                #total+=1
                #found = False       
            #j+=1
        #found = True
        #i+=1
    #print(total)
    i = 0
    while(i<len(freshList)):
        ints = []
        ints.append(int(freshList[i][0]))
        ints.append(int(freshList[i][1]))
        freshList[i] = ints
        i+=1
    print(freshList)
    freshList = sorted(freshList, key=lambda x: x[0])
    print(freshList)
    i = 0
    while(i<len(freshList)):
        if(i<len(freshList)-1 and freshList[i][1] >= freshList[i+1][0]):
            if(freshList[i][1] < freshList[i+1][1]):
                freshList[i][1] = freshList[i+1][1]
            del freshList[i+1]
            print("deleted")
        else:        
            i+=1
    print(len(freshList))
    i = 0
    print(freshList)
    while(i<len(freshList)):
        total += (freshList[i][1]+1)-freshList[i][0]
        i+=1
    print(total)

main()