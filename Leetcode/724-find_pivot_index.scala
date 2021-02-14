object Solution {
    def pivotIndex(nums: Array[Int]): Int = {
        def pivotLoop(i: Int, leftSum: Int, numSum: Int): Int = 
            if (i == nums.length) return -1
            else if (leftSum == numSum - leftSum - nums(i)) return i
            pivotLoop(i+1, leftSum + nums(i), numSum)
        
        pivotLoop(0, 0, nums.sum)
    }
}


