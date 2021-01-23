# @param {Integer[][]} grid
# @return {Integer}
def max_area_of_island(grid)
    queue = []
    cur_max = 0
    land = 1

    grid.each_with_index do |row, r|
        row.each_with_index do |col, c|

            # DFS on every landmass seen
            if grid[r][c] == land
                cur = dfs_search(grid, r, c, land)
                cur_max = [cur, cur_max].max

            end
        end
    end
    return cur_max
end

def dfs_search(grid, row, col, land)
    island_size = 0
    size_rows = grid.length()
    size_cols = grid[0].length()

    if (row >= 0 && row < size_rows && col >= 0 && col < size_cols && grid[row][col] == land)
        grid[row][col] = 0

        # Dfs search in 4 cardinal directions
        island_size += 1 
        island_size += dfs_search(grid, row+1, col, land)
        island_size += dfs_search(grid, row-1, col, land)
        island_size += dfs_search(grid, row, col+1, land)
        island_size += dfs_search(grid, row, col-1, land)
    end
    island_size
end

grid = [
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

puts max_area_of_island(grid)