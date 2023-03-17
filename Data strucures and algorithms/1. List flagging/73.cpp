/*
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
*/

/*
Intuition:
Traverse through matrix. If you find a 0, change the 0th index column and row to 0. For toprow have a separate boolean. Once youve traversed, go through the 0th index rows and columns to look for zeroes. 
If there is a zero, change the whole row or column to a zero.
*/

#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bool toprow = false;
        for (int i = 0; i< m; i++){
            for (int j = 0; j<n; j++){
                if(matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    if (i==0) toprow = true;
                    else matrix[i][0] = 0;
                }
            }
        }
        for (int i = 1; i<m; i++){
            if (matrix[i][0] == 0){
                for(int j = 0; j<n; j++) matrix[i][j] = 0;
            }
        }
        for (int j = 0; j<n;j++){
            if(matrix[0][j] == 0){
                for (int i = 0; i<m; i++) matrix[i][j] = 0;
            }
        }
        if(toprow){
            for (int i = 0; i<n; i++) matrix[0][i] = 0;
        }
    }
};

int main(){
    Solution s;
    vector<vector<int>> matrix {{1,1,1},{1,0,1},{1,1,1}};
    s.setZeroes(matrix);

}