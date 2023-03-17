/*
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

*/

/*
Intuition:
Tag the index with -1. When you reach an index that is -1, you know that is the repeat.
*/

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size(), sol =-1;
        for (int i = 0; i< n; i++){
            int check = abs(nums[i]);
            if (nums[check]<0){
                sol = check;
                break;
            }
            nums[check]*=-1;
        }     
        return sol;
    }
};

int main(){
    Solution s;
    vector<int> nums {1,3,4,2,2};
    cout<< s.findDuplicate(nums);
}