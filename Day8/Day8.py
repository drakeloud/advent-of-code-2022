import numpy as np

def part_one(grid):
    # start with perimeter
    total_visible = (len(grid[0]) * 2) + (len(grid) * 2) - 4

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            curr = grid[i][j]

            # check top
            if curr > max(grid[:i, j]):
                total_visible += 1
            # check bottom
            elif curr > max(grid[i + 1:, j]):
                total_visible += 1

            # check left
            elif curr > max(grid[i, :j]):
                total_visible += 1

            # check right
            elif curr > max(grid[i, j + 1:]):
                total_visible += 1

    print(total_visible)

def part_two(grid):
    scenic_max = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            curr = grid[i][j]

            def get_scenic_val(arr, val):
                if max(arr) >= val:
                    return np.argmax(arr>=val) + 1
                else:
                    return len(arr)
            
            top_scenic = get_scenic_val(np.flip(grid[:i, j]),curr)
            bot_scenic = get_scenic_val(grid[i + 1:, j],curr)
            right_scenic = get_scenic_val(grid[i, j + 1:],curr)
            left_scenic = get_scenic_val(np.flip(grid[i, :j]), curr)
            
            scenic_score = top_scenic * bot_scenic * right_scenic * left_scenic
            scenic_max = max(scenic_max, scenic_score)

    print(scenic_max)

if __name__ == '__main__':
    with open('input.txt') as file:
        file_input = file.read().split('\n')
        grid = []
        for row in file_input:
            grid.append(list(row))
        
        grid = np.asarray(grid)
        part_one(grid)
        part_two(grid)
