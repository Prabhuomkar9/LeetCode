class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml, mh = 0, len(matrix) - 1

        while ml <= mh:
            mm = (ml + mh) // 2

            if matrix[mm][0] < target:
                ml = mm + 1
            elif matrix[mm][0] > target:
                mh = mm - 1
            else:
                return True

        nl, nh = 0, len(matrix[0]) - 1

        while nl <= nh:
            nm = (nl + nh) // 2

            if matrix[mh][nm] < target:
                nl = nm + 1
            elif matrix[mh][nm] > target:
                nh = nm - 1
            else:
                return True

        return False
