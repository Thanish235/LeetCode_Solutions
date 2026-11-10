class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        def get_next(i, direction):
            if (nums[i] > 0) != direction:
                return -1
            j = (i + nums[i]) % n
            if j == i:
                return -1
            return j
        for start in range(n):
            direction = nums[start] > 0
            slow = start
            fast = start
            while True:
                slow = get_next(slow, direction)
                if slow == -1:
                    break
                fast = get_next(fast, direction)
                if fast == -1:
                    break
                fast = get_next(fast, direction)
                if fast == -1:
                    break
                if slow == fast:
                    return True
        return False
