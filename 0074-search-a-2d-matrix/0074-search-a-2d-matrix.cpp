#include <vector>
using namespace std;

class Solution {
public:
    bool searchValue(vector<int>& row, int target) {
        int st = 0;
        int end = row.size() - 1;

        while (st <= end) {
            int mid = st + (end - st) / 2;

            if (row[mid] < target)
                st = mid + 1;
            else if (row[mid] > target)
                end = mid - 1;
            else
                return true;
        }
        return false;
    }

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty())
            return false;

        int rows = matrix.size();
        int cols = matrix[0].size();

        int st_row = 0;
        int end_row = rows - 1;

        while (st_row <= end_row) {
            int mid = st_row + (end_row - st_row) / 2;

            if (matrix[mid][0] <= target && target <= matrix[mid][cols - 1]) {
                return searchValue(matrix[mid], target);
            }
            else if (matrix[mid][0] > target) {
                end_row = mid - 1;
            }
            else {
                st_row = mid + 1;
            }
        }

        return false;
    }
};
