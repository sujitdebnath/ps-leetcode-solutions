class Solution:
    def merge(self, nums1, m, nums2, n):
        curr_ind_n1 = 0
        curr_ind_n2 = 0

        while curr_ind_n1 < m and curr_ind_n2 < n:
            if nums1[curr_ind_n1] < nums2[curr_ind_n2]:
                curr_ind_n1 += 1
            else:
                nums1.insert(curr_ind_n1, nums2[curr_ind_n2])
                nums1.pop()
                curr_ind_n1 += 1
                curr_ind_n2 += 1
                m += 1
        
        if curr_ind_n2 < n:
            while curr_ind_n2 < n:
                nums1.insert(curr_ind_n1, nums2[curr_ind_n2])
                nums1.pop()
                curr_ind_n1 += 1
                curr_ind_n2 += 1


nums1 = [2,0]
nums2 = [1]
m, n = 1, 1

sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)