from typing import List, Tuple
import sys

class Solution:
    def longestCommonSubsequence(self, nums1: List[int], nums2: List[int]) -> Tuple[int, List[int]]:
        if len(nums1) < len(nums2):
            return self.LCS(nums1, nums2)
        return self.LCS(nums2, nums1)

    def LCS(self, nums1: List[int], nums2: List[int]) -> Tuple[int, List[int]]:
        m = len(nums1)
        n = len(nums2)
        M = [[0] * (m + 1) for _ in range(2)]
        prev_indices = [[None] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            M[i % 2][0] = 0
            for j in range(1, m + 1):
                if nums1[j - 1] == nums2[i - 1]:
                    M[i % 2][j] = M[(i - 1) % 2][j - 1] + 1
                    prev_indices[i][j] = (i - 1, j - 1)
                else:
                    if M[(i - 1) % 2][j] > M[i % 2][j - 1]:
                        M[i % 2][j] = M[(i - 1) % 2][j]
                        prev_indices[i][j] = (i - 1, j)
                    else:
                        M[i % 2][j] = M[i % 2][j - 1]
                        prev_indices[i][j] = (i, j - 1)

        # Retrieve the common subsequence
        common_subsequence = []
        i, j = n, m
        while i > 0 and j > 0:
            if nums1[j - 1] == nums2[i - 1]:
                common_subsequence.append(nums1[j - 1])
            i, j = prev_indices[i][j]

        return M[n % 2][m], common_subsequence[::-1]

if __name__ == "__main__":
    num_pair = int(sys.stdin.readline())
    for _ in range(num_pair):
        print("Case #", _+1, ": ", sep='', end='')
        a = [int(s) for s in sys.stdin.readline().split()]
        b = [int(s) for s in sys.stdin.readline().split()]
        _ = Solution()
        print(_.longestCommonSubsequence(a, b))
        print()