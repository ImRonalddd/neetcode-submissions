class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = {}, {}
        pre[0] = nums[0]
        post[len(nums)-1] = nums[-1]
        for i in range(1, len(nums)):
            pre[i] = nums[i] * pre[i-1]
        for i in range(len(nums)-2, 0, -1):
            post[i] = nums[i] * post[i+1]
        answer = []
        answer.append(post[1])
        for i in range(1, len(nums)-1):
            answer.append(pre[i-1]*post[i+1])
        answer.append(pre[len(nums)-2])
        return answer