class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Define state transitions
        DIGIT = 'digit'
        LETTER = 'letter'
        DECIMAL = 'decimal'
        BLANK = 'blank'
        OP = 'op'
        NONE = 'none'

        # Possible ending states
        ends = ['num1', 'num2', 'num3', 'blank2', 'decimal2']

        # Create DFA
        states = {
            'blank1': {DIGIT: 'num1', BLANK: 'blank1', OP: 'op1', DECIMAL: 'decimal1'},
            'decimal1': {DIGIT: 'num2'},
            'decimal2': {DIGIT: 'num2', LETTER: 'alp1', BLANK: 'blank2'},
            'op1': {DIGIT: 'num1', DECIMAL: 'decimal1'},
            'num1': {DIGIT: 'num1', DECIMAL: 'decimal2', LETTER: 'alp1', BLANK: 'blank2'},
            'num2': {DIGIT: 'num2', LETTER: 'alp1', BLANK: 'blank2'},
            'alp1': {DIGIT: 'num3', OP: 'op2'},
            'op2': {DIGIT: 'num3'},
            'num3': {DIGIT: 'num3', BLANK: 'blank2'},
            'blank2': {BLANK: 'blank2'}
        }

        # Transition states based on input
        current_state = 'blank1'
        for character in s:
            next_char = NONE 
            if character.isdigit():
                next_char = DIGIT 
            elif character == 'e':
                next_char = LETTER 
            elif character in ['+', '-']:
                next_char = OP 
            elif character == '.':
                next_char = DECIMAL
            elif character in [' ', '\n']:
                next_char = BLANK

            # Next state
            if next_char not in states[current_state]:
                return False 
            else:
                current_state = states[current_state][next_char]
        
        # Check if in accepting state
        if current_state in ends:
            return True 
        return False

z = Solution()
s = '-5.'
print(z.isNumber(s))

        
