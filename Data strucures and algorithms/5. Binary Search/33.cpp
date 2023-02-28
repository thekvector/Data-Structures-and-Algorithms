/*
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
*/
/*
Intuition:
Look for where the array has been rotated. Once we know where the rotatoin point is we can remove half of the array until the element is found. If not found, return -1.
*/
#include<vector> 
#include<iostream>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0,r= nums.size();
        while (l<r){
            int m = (l+r) /2;
            if (nums[m] == target) return m;
            if (nums[l] < nums[m]){
                if (target> nums[m] or target< nums[l]) l = m+1;
                else r = m;
            }
            else{
                if(target < nums[m] or target> nums[r-1]) r = m;
                else l = m+1;
            }
        }
        return -1;
    }
};

int main(){
    Solution s; 
    vector<int> nums {4,5,6,7,0,1,2};
    cout<< s.search(nums, 0);
}