class Solution:
    def __init__(self):
        self.res = []
        self.path = []
       
    def trackBack(self, start, nums):
        self.res.append(self.path.copy())
        for i in range(start, len(nums)):
            print("variable i is: ", i)
            self.path.append(nums[i])
            print("path now is: ", self.path)
            self.trackBack(i+1,nums)
            
            self.path.pop()

    def subsets(self, nums):
        self.trackBack(0, nums)
        return self.res

if __name__ == '__main__':
    num = [1, 2, 3]
    result = Solution().subsets(num)
    print(result)
