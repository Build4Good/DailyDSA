from collections import defaultdict
rows = defaultdict(set)
cols = defaultdict(set)
boxes = defaultdict(set)

valid = True

input=[
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]

for row in range(0,len(input),1):

    for col in range(0,len(input[0]),1):
        box_idx = (row // 3, col // 3)
        val=input[row][col]
        if val ==".":
            pass
        else:
            if val in rows[row] or val in cols[col] or val in boxes[box_idx]:
                valid = False
                break
            else:
                rows[row].add(val)
                cols[col].add(val)
                boxes[box_idx].add(val)


         
    if not valid:
        break

print(valid)          