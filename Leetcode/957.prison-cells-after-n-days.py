class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """

        # There are only 2^6 = 64 possible combinations, thus we can store all states in a list
        all_cells = []

        # Hold index for each state 
        cell_indexes = {}
        cur_cells = cells 

        # Create next cell state
        def next_cells(cells):
            return [0] + [ (cells[i-1] ^ cells[i+1]) ^ 1 for i in range(1, 7)] + [0]
           
        # Keep adding states to all_states until we encounter a loop
        total_loop = 0
        while cur_cells not in all_cells:
            cell_indexes[str(cur_cells)] = total_loop
            all_cells.append(cur_cells)
            cur_cells = next_cells(cur_cells)
            total_loop += 1

        # Get size of the loop, and preloop if it takes more than 1 transition to get into a loop
        # cur_cells is still the start of the state
        loop_size = total_loop - cell_indexes[str(cur_cells)]
        pre_loop = cell_indexes[str(cur_cells)]

        # Mod N by the loop_size and return the precalculated state at that index
        state = (N - pre_loop) % loop_size
        if N < len(all_cells):
            return all_cells[N]
        return all_cells[cell_indexes[str(cur_cells)] + state]

z = Solution()
cells = [1,0,0,1,0,0,1,0]
N = 1000000000
print(z.prisonAfterNDays(cells, N))

        
