#autosolver for sudoku

from itertools import count

app_sq=[    #appearance inside squares
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}] 
app_line=[    #appearance on the line
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}] 
app_col=[    #appearance on the colomn
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0},
{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}] 
sq_mapping=[    #a matrix that shows tells the square number for each slot
[0, 0, 0, 1, 1, 1, 2, 2, 2],
[0, 0, 0, 1, 1, 1, 2, 2, 2],
[0, 0, 0, 1, 1, 1, 2, 2, 2],
[3, 3, 3, 4, 4, 4, 5, 5, 5],
[3, 3, 3, 4, 4, 4, 5, 5, 5],
[3, 3, 3, 4, 4, 4, 5, 5, 5],
[6, 6, 6, 7, 7, 7, 8, 8, 8],
[6, 6, 6, 7, 7, 7, 8, 8, 8],
[6, 6, 6, 7, 7, 7, 8, 8, 8]]
options=[   #a 3D matrix with options
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]],
[[],[],[],[],[],[],[],[],[]]]

def print_sudoku(sudoku):
    for i in range(9):
        print(sudoku[i][:])

def check_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                return False
    return True

# You can add the sudoku to be solved below and comment out the file reading part
# sudoku=[
# [4, 0, 6, 5, 0, 2, 8, 0, 9],
# [0, 0, 0, 0, 4, 0, 0, 3, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 5],
# [6, 0, 0, 8, 0, 0, 1, 0, 0],
# [5, 0, 0, 0, 7, 0, 0, 8, 0],
# [3, 0, 2, 9, 0, 4, 0, 6, 0],
# [0, 2, 0, 6, 0, 0, 0, 0, 1],
# [0, 0, 0, 0, 5, 3, 9, 4, 0],
# [8, 3, 0, 0, 9, 0, 0, 0, 2]]

sudoku=[[],[],[],[],[],[],[],[],[],[]]
file=open('sudoku.txt','r')
for i in range(9):
    line=file.readline()
    for char in line:
        if ord(char)>=48 and ord(char)<=57:
            sudoku[i].append(int(char))
file.close()

for i in range(9):
    for j in range(9):
        if sudoku[i][j]>0:
            app_line[i][sudoku[i][j]]=1
            app_col[j][sudoku[i][j]]=1
            app_sq[sq_mapping[i][j]][sudoku[i][j]]=1

for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            for k,v in app_sq[sq_mapping[i][j]].items():
                if v==0 and app_line[i][k]==0 and app_col[j][k]==0:
                    options[i][j].append(k)

for iteration in count(1):
    for i in range(9):
        for j in range(9):
            if len(options[i][j])==1:
                sudoku[i][j]=options[i][j][0]
                sq_index=sq_mapping[i][j]
                for k in range(9):
                    try:
                        options[i][k].remove(sudoku[i][j])
                    except:
                        None
                    try:
                        options[k][j].remove(sudoku[i][j])
                    except:
                        None
                for k in range(9):
                    for l in range(9):
                        if sq_mapping[k][l]==sq_index:
                            try:
                                options[k][l].remove(sudoku[i][j])
                            except:
                                None
    if check_sudoku(sudoku):
        break

print_sudoku(sudoku)

file=open('sudoku-done.txt','w')
for i in range(9):
    file.write(str(sudoku[i][:]))
    file.write('\n')
file.close()

  
print(f'Nomber of cycles completed: {iteration}')
  
