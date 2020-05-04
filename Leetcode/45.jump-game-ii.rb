# @param {Integer[]} nums
# @return {Integer}
def jump(nums)

    furthest = 0
    jumps = 0
    jump_end = 0

    nums.pop()
    nums.each_with_index do |item, index|
        furthest = [index + item, furthest].max
        if index == jump_end
            jumps+=1
            jump_end = furthest
        end
        
    end
    return jumps
    
end

my_num = [2,1]
puts jump(my_num)