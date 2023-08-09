class Solution:
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        
        # sort all intervals by start value in ascending order
        intervals.sort(key=lambda x: x[0])

        updated_intervals = list()
        first_interval    = intervals[0]

        for curr_interval in intervals[1:]:
            curr_start, curr_end   = curr_interval
            first_start, first_end = first_interval

            # when first interval belong to the left side of the current interval
            if first_end < curr_start:
                updated_intervals.append(first_interval)
                first_interval = curr_interval
            # when first interval belong to the right side of the current interval
            elif first_start > curr_end:
                updated_intervals.append(curr_interval)
            # when first and current interval overlapps
            else:
                first_interval = [min(first_start, curr_start), max(first_end, curr_end)]
        
        updated_intervals.append(first_interval)

        return updated_intervals


sol = Solution()
print(sol.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))