class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Handle edge cases
        if n < 1:
            return 0
        
        # Digit rotation mapping
        rotation_map = {
            '0': '0', '1': '1', '2': '5', '5': '2',
            '6': '9', '8': '8', '9': '6'
        }
        valid_digits = set(rotation_map.keys())
        
        count = 0
        for x in range(1, n + 1):
            # Convert number to string for digit processing
            x_str = str(x)
            # Check if all digits are valid
            if not all(d in valid_digits for d in x_str):
                continue
            
            # Rotate each digit
            rotated = ''
            for d in x_str:
                rotated += rotation_map[d]
            
            # Check if rotated number is valid and different
            if rotated[0] != '0' or rotated == '0':  # Valid number (no leading zero unless 0)
                rotated_num = int(rotated)
                if rotated_num != x:  # Different from original
                    count += 1
        
        return count
                
            