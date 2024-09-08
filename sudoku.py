import random
import json

sudoku = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],]

def isValid(num,row,column):

    if num in sudoku[row]:
        return False
        # checks if num is already in this row
    
    for i in range(9):
        if sudoku[i][column] == num:
            return False
        # checks columns for validity

    rowStart = (row//3) * 3
    rowEnd = rowStart+3

    columnStart = (column//3)*3
    columnEnd = columnStart+3

    for i in range(columnStart,columnEnd):
        for j in range(rowStart,rowEnd):
            if sudoku[j][i] == num:
                return False
    
    return True

def fillSudoku():
    def solve():
        for row in range(9):
            for column in range(9):
                if sudoku[row][column] == 0:
                    options = list(range(1,10))
                    random.shuffle(options)
                    for option in options:
                        if isValid(option,row,column):
                            sudoku[row][column] = option
                            if solve():
                                return True
                            sudoku[row][column] = 0
                    return False
        return True
    solve()


        

fillSudoku()

game = sudoku

def display(game):
    print('  A  B  C  D  E  F  G  H  I ')
    line = ''
    for row in range(9):
        line += str(row+1)
        for i in range(9):
            line+= '['+str(game[row][i])+']'
        print(line)
        line = ''



filename = 'solution.json'
with open(filename,'w') as fObject:
    json.dump(sudoku,fObject)

def removeCharacters(game):
    for row in game:
        blank = list(range(0,9))
        random.shuffle(blank)
        for i in range(5):
            row[blank[i]] = ' '

removeCharacters(game)



def play():
    filename = 'solution.json'
    with open(filename) as f_obj:
        solution = json.load(f_obj)

    letters = ['A','B','C','D','E','F','G','H','I']

    display(game)
    attempt = input("To play sudoku, type in your number then the coordinates of it's cell seperated by a space in the format 9 A 1\n where 9 is your number, A is the letter of your column and 1 is the number of your row \n ")
    
    number= attempt[0]
    rowNumber = int(attempt[4])-1
    columnLettter = attempt[2]
    

    if int(number) == int(solution[rowNumber][letters.index(columnLettter)]):
        game[rowNumber][letters.index(columnLettter)] = number
        play()
    else:
        print(solution[rowNumber][letters.index(columnLettter)])
        print('Your number is wrong')
    
play()








        
    
    

        






