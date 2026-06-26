from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Early outs for tiny inputs
        n = len(s)
        if n <= 1:
            return n

        # frequency of each uppercase letter in the window
        counts = [0] * 26
        left = 0 # left bound of sliding window
        max_count = 0 # count of the most frequent letter seen in the current window
        best = 0 # best window length found so far

        # helper to map char to index 0 - 25
        to_idx = lambda ch: ord(ch) - ord('A')

        # expand the window by moving right pointer
        for right in range(n):
            r_idx = to_idx(s[right])
            counts[r_idx] += 1
            # track the running maximum freq in the window
            if counts[r_idx] > max_count:
                max_count = counts[r_idx]

            # if replacements needed exceed k shrink from left
            while (right - left + 1) - max_count > k:
                l_idx = to_idx(s[left])
                counts[l_idx] -= 1
                left += 1

            # record the best valid window length
            window_len = right - left + 1
            if window_len > best:
                best = window_len
        return best