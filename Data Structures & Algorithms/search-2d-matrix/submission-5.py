class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = len(matrix)
        y = len(matrix[0])

        s,e = 0, x*y - 1

        while s <= e:
            i = s + (e-s)//2
            xi = i // y
            yi = i % y
            elt= matrix[xi][yi]

            if elt == target:
                return True
            elif elt > target:
                e = i - 1
            else:
                s = i + 1
        return False