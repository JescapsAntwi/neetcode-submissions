class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0
        # shift the bits of n to the right by i positions and masking all the other bits leaving only the ith bit
        for i in range(32):
            bit = (n >> i) & 1


        # shift the extracted bit to its new position in the reversed number 
            res += (bit << (31 - i))

        # sum up the values of each bit in its new position 
        return res 