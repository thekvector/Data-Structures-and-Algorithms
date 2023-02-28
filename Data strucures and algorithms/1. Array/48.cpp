/*
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
*/

/*
Intuition: Have 4 pointers pointing to all four directions to flip. Hold the topleft value in a temporary variable. Flip the values in the matrix and for the last flip, swap with the temporary variable. */

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int l = 0, r = matrix.size()-1;
        while (l<r){
            int top = l, bottom = r;
            for (int i = 0; i<r-l; i++){
                int topleft = matrix[top][l+i];
                matrix[top][l+i] = matrix[bottom-i][l];
                matrix[bottom-i][l] = matrix[bottom][r-i];
                matrix[bottom][r-i] = matrix[top+i][r];
                matrix[top+i][r] = topleft;
            }
            l+=1; 
            r-=1;
        }
    }
};

int main(){
    Solution s;
    vector<vector<int>> matrix {{1,2,3},{4,5,6},{7,8,9}};
    s.rotate(matrix);
}

