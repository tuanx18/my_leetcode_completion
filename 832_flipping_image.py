# [EASY] https://leetcode.com/problems/flipping-an-image
# Completed 2026/03/24
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i].reverse()

            for b in range(len(image[i])):
                # print(b)
                if image[i][b] == 1:
                    image[i][b] = 0 
                else:
                    image[i][b] = 1
        # print(image)
        return image
