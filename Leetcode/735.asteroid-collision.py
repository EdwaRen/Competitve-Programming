class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        # Treat question with the same general logic as parenthesis matching
        stack = []

        for rock in asteroids:

            # Initiate while look only when a collision is detected
            while len(stack) >= 1 and stack[-1] >= 0 and rock <= 0:
                prev = stack.pop()
                if abs(rock) < prev:
                    # Re add the positive asteroid back in
                    stack.append(prev)
                    break
                elif abs(rock) == prev:
                    break

            # Add survivor of the collision. No survivor on tie.
            else:
                stack.append(rock)
                    
        return stack 

z = Solution() 
asteroids = [10, 2, -10]
print(z.asteroidCollision(asteroids))