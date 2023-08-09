class Solution:
    def insert(self, intervals, newInterval):
        updated_intervals = list()

        for curr_interval in intervals:
            curr_start, curr_end = curr_interval
            new_start, new_end   = newInterval[0], newInterval[1]

            # when new interval belong to the left side of the current interval
            if new_end < curr_start:
                updated_intervals.append(newInterval)
                newInterval = curr_interval
            # when new interval belong to the right side of the current interval
            elif new_start > curr_end:
                updated_intervals.append(curr_interval)
            # when new and current interval overlapps
            else:
                newInterval = [min(curr_start, new_start), max(curr_end, new_end)]
        
        updated_intervals.append(newInterval)
        
        return updated_intervals


intervals   = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
sol         = Solution()
print(sol.insert(intervals, newInterval))