from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter= Counter(nums)
        most_common_elements= frequency_counter.most_common(k)
        result= [element for element, count in most_common_elements]
        return result
        #Time complexity is O(n+ m*(logk))
        #Space complexity is O(m)
        #Pitfall1: Assuming the input array is sorted or elemets are unique
        #Pitfall2: Using sorting on the entire frequency map
        #Pitfall3: Incorrect Heap Implementation