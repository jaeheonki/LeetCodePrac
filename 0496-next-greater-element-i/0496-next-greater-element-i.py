class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        greater = {}

        for i in nums2 : 
            while stack and i > stack[-1] :
                prev_num = stack.pop()
                greater[prev_num] = i
            stack.append(i)
        
        while stack :
            prev_num = stack.pop()
            greater[prev_num] = -1
        
        res = []
        for i in nums1 : 
           res.append(greater[i])
        
        return res