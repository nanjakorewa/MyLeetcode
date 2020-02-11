class Solution:
    def maxArea(self, height) -> int:
        maxArea = 0
        i, j, N = 0, 1, len(height)

        while i+j<N:
            if height[i] <= height[N-j]:
                area = (N-i-j)*height[i]
                i += 1
            elif height[i] > height[N-j]:
                area = (N-i-j)*height[N-j]
                j += 1

            if area > maxArea:
                maxArea = area

        return maxArea