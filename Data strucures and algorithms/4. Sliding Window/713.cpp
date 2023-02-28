/*
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
*/

/*
Intuition:
Have a left and right pointer. Have a running product variable. Make the right pointer iterate through the array. Multiply the right pointer into the running product.
Any time the running product is greater than the target 'k', we know every perumation of the subarray from left to right is a valid subarray. So we add the right-left+1 value into our solution.*/


#include <vector>
#include<iostream>
using namespace std;
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k<=1) return 0;
        int sol = 0, prod = 1, j = 0;
        for (int i = 0; i< nums.size(); i++){
            prod *= nums[i];
            while (prod>= k){
                prod /= nums[j];
                j+=1;
            }
            sol += i-j+1;
        }
        return sol;
    }
};

int main(){
    Solution s;
    vector <int> nums {10,5,2,6};
    s.numSubarrayProductLessThanK(nums, 100);
}