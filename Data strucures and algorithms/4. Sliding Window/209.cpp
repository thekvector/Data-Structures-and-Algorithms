/*
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
*/

/*
Intuition:
Have a left pointer starting and index 0. Have a right pointer iterating through the list. Subtract the element at index right from target. If the target value ever is less than or equal to zero, check how long the right - left is.
Add 1 to the left pointer until the target is greater than 0 again.*/

#include<vector>
#include<iostream>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0, sol = 1e9;
        for (int right = 0; right<nums.size(); right++){
            target -= nums[right];
            while (target<=0){
                sol = min(right-left+1, sol);
                target += nums[left];
                left++;
            }
        }
        if (sol == 1e9) return 0;
        return sol;
    }
};

int main(){
    Solution s;
    vector<int> nums {2,3,1,2,4,3};
    cout<<s.minSubArrayLen(7, nums);
}