from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        sorted_elements = sorted(
            counts,
            key=counts.get,
            reverse=True
        )

        return sorted_elements[:k]