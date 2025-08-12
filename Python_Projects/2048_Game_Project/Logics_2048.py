import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

# to add the new 2 at the random EMPTY pos
def add_new_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    # keep on changing the pos until empty pos is found
    while (mat[r][c] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c] = 2

# if any cell has 2048 -->> return True
def has_won(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return True
    return False

# until there is a {possibility} of the empty pos in mat
def game_not_over(mat):
    # if any ele is 0 
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return True
    
    # if by some movement, it is possible to make an empty slot
    # 1. for every row and col except last row & col
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i+1][j]) or (mat[i][j] == mat[i][j+1]):
                return True

    # 2. for last row (i.e i == 3)
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return True

    # 3. for last col (i.e j == 3)
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return True
        
    return False

# get the current state of the game (won, lost, game not over)
def get_current_state(mat):
    if has_won(mat):
        return "WON"
    elif game_not_over(mat):
        return 'GAME IS NOT OVER'
    else:
        return 'LOST'
    
'''We need to track that whether the compress and merge are doing some changes in the matrix or not, because 
{a new 2 is only added if there is some change by the movements}. 
that's why we need to keep the 'changed' variable in compress and merge'''

# implemented for left move
# sending all non zero nums to the left most part 
def compress(mat):
    changed = False
    comp_mat = []
    for i in range(4):
        comp_mat.append([0]*4)

    for i in range(4):
        pos = 0 # for  tracking position where we need to insert a non zero number in comp_mat
        for j in range(4):
            if mat[i][j] != 0:
                comp_mat[i][pos] = mat[i][j]
                # if pos == j for every ele in a given row, means no compression is there
                if j != pos:
                    changed = True
                pos += 1
    return comp_mat, changed

# merge same ele in the row 
# implemented for left move
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] != 0 and mat[i][j] == mat[i][j+1]:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                changed = True
    return mat, changed
    

# reverse (flip) as  <<<<<-------->>>>>>>
def reverse_mat(mat):
    rev_mat = []
    for i in range(4):
        rev_row = []
        for j in range(4):
            rev_row.append(mat[i][3-j])
        rev_mat.append(rev_row)
    return rev_mat

# transpose of the matrix (i, j) -->>> (j, i)
def transpose_mat(mat):
    tr_mat = []
    for i in range(4):
        l = []
        for j in range(4):
            l.append(mat[j][i])
        tr_mat.append(l)
    return tr_mat


# steps :  compress ->> merge -->> compress
def Move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    return new_grid, changed

# steps: Rev -->> {move_left} -->> Rev
def Move_right(grid):
    rev_grid = reverse_mat(grid)
    new_grid, changed = Move_left(rev_grid)
    final_grid = reverse_mat(new_grid)
    return final_grid, changed

# steps: Transpose -->>> {Move_Left} >>>> Transpose
def Move_up(grid):
    tr_grid = transpose_mat(grid)
    new_grid, changed = Move_left(tr_grid)
    final_grid = transpose_mat(new_grid)
    return final_grid, changed

# steps: Trp -->> Rev -->> {move_left} -->> Rev -->> Trp
def Move_down(grid):
    tr_grid = transpose_mat(grid)
    rev_grid = reverse_mat(tr_grid)
    new_grid, changed = Move_left(rev_grid)
    new_grid = reverse_mat(new_grid)
    final_grid = transpose_mat(new_grid)
    return final_grid, changed