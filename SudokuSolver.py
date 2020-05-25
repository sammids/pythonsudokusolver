
#Sudoku Solver
#current stage- uses backtracking to solve 
#next stage- allow options for other (possibly quicker) methods of solving, and compare time complexity of each algorithm


#backtracking algorithm functions
def findNext(arr, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if arr[x][y] == 0:
                return x,y
    for x in range(0,9):
        for y in range(0,9):
            if arr[x][y] == 0:
                return x,y
    return -1,-1



def checkValid(arr, i, j,p):
    rowDone = all([p != arr[i][x] for x in range(9)])
    if rowDone:
        columnDone = all([p != arr[x][j] for x in range(9)])
        if columnDone:
            # finding the i,j cell
            findI = 3 *(i//3)
            findJ = 3 *(j//3) 
            for x in range(findI, findI+3):
                for y in range(findJ, findJ+3):
                    if arr[x][y] == p:
                        return False
            return True
    return False


def solve(arr, i=0,j=0):
    i,j = findNext(arr,i,j)
    if i == -1:
        return True
    for p in range(1,10):
        if checkValid(arr,i,j,p):
            arr[i][j] = p
            if solve(arr,i,j):
                return True
            arr[i][j] = 0

    return False


def enterSU():
    print("Please enter the Sudoku line by line, with spaces separating each number. Use a zero represent a blank square")
    print("Enter the first line:")
    su =[]
    x = [int(i) for i in input().split()]
    su.append(x)
    i=0
    while i< 8:
        print("Enter Next line: ")
        x = [int(i) for i in input().split()]
        su.append(x)
        i+=1

    m = solve(su)
    return m

def main():
    print("Welcome to Sudoku Solver!")
    
    run = True
    while run:
        
        choice = input("Would you like to use the default Sudoku(input Y), or enter your own(input N)? ")
        
        if choice == 'Y':
            default= [[0,0,0,1,0,5,0,6,8],[0,0,0,0,0,0,7,0,1],[9,0,1,0,0,0,0,3,0],[0,0,7,0,2,6,0,0,0],[5,0,0,0,0,0,0,0,3],[0,0,0,8,7,0,4,0,0],[0,3,0,0,0,0,8,0,5],[1,0,5,0,0,0,0,0,0],[7,9,0,4,0,1,0,0,0]]
            print("Unsolved default Sudoku: ")
            print(default)
            print("solving sudoku...")
            m = solve(default)
        else:
            print("solving sudoku...")
            m = enterSU()
       
        
        
        if m:
            print("Sudoku has been solved")
            print(default)
        else:
            print("Sudoku has not been solved")
            print(default)


        cont =input("If you would like to solve another Sudoku, please enter Y: ")
        if cont != 'Y':
            run = False
        else:
            run = True

    
main()



