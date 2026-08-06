class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [diff]: number

        map = defaultdict(int)

        for i, n in enumerate(nums):
            if n in map:
                return [map[n],i]

            diff = target - n
            map[diff] = i