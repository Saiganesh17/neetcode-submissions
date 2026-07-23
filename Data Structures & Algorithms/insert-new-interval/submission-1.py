class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge_intervals(interval_list: List[List[int]])->List[List[int]]:
            interval_list.sort()
            merged_result= [interval_list[0]]
            for start, end in interval_list[1:]:
                if merged_result[-1][1]<start:
                    merged_result.append([start, end])
                else:
                    merged_result[-1][1] = max(merged_result[-1][1], end)
          
            return merged_result
      
        # Add the new interval to the existing intervals
        intervals.append(newInterval)
      
        # Merge all intervals and return the result
        return merge_intervals(intervals)
        #Time and space complexity is O(n * logn ) and O(n) respectively
        #pitfall1: Modifying the input list in place
        #pitfall2: Inefficient approach for already sorted intervals
        #pitfall3: Edge case empty intervals list