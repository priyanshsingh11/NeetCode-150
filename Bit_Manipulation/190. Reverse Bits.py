class Solution(object):
    def reverseBits(self, n):
        # Step 1: convert to binary string and remove '0b'
        num = bin(n)[2:]
        
        # Step 2: make it 32 bits (add leading zeros)
        num = num.zfill(32)
        
        # Step 3: reverse string
        reversed_num = num[::-1]
        
        # Step 4: convert back to integer
        return int(reversed_num, 2)
