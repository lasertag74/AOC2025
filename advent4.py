
def main():
    final = 0
    lines = 0
    ArrayBase = [] 
    with open("AdventFile1.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            currLine = list(line)
            ArrayBase.append(currLine)
            lines += 1
    
    print(len(ArrayBase[2]))

    running = True
    while(running):
        goAgain = False
        y ,x = 0, 0
        while(y < len(ArrayBase)):
            while(x < len(ArrayBase[y])):
                if(ArrayBase[y][x]== "@" and checker(ArrayBase,y,x,len(ArrayBase), len(ArrayBase[y]))):
                    goAgain = True
                    final+=1
                    ArrayBase[y][x] = "."

                x+=1
            x = 0    
            y+=1
        print(ArrayBase)
        running = goAgain
    print(final)   
def checker(matrix,y,x,length,width):
    total = 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  
        (0, -1),           (0, 1),  
        (1, -1),  (1, 0),  (1, 1)    
    ]
    for dr, dc in directions:
        n_row, n_col = y + dr, x + dc
        
        if 0 <= n_row < width and 0 <= n_col < length and matrix[n_row][n_col] == "@":
            total += 1
    if total >= 4:
        return False
    else:
        return True   
    

          
main()
