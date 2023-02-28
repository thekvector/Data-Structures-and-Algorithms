/*
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
*/
/*
Intuition:
Do binary search on the rows. Then do binary search on the row that we found where the target should be in between. If not found return -1.
*/

#include<vector>
#include<iostream>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0, r = matrix.size();
        while (l<r){
            int m = (l+r) / 2;
            if (matrix[m][0] == target) return true;
            if (matrix[m][0] > target) r = m;
            else l = m+1;
        }
        int i = l-1;
        l = 0;
        r = matrix[i].size();
        while (l<r){
            int m = (l+r) / 2;
            if (matrix[i][m] == target) return true;
            if (matrix[i][m] > target) r = m;
            else l = m+1;
        }
        return false;
    }
};

int main(){
    Solution s;
    vector<vector<int>> matrix {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    s.searchMatrix(matrix, 0);
}