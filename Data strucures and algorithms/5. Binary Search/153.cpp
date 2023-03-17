/*
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.*/

/*
Intuition:
We have to find how many times the array was rotated. Once we find the rotation point, we know that point is going to be the minimum value in the array.
*/

#include <vector>
#include<iostream>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size();
        int sol = 1e9;
        while (l<r){
            int m = (l+r) /2;
            sol = min(sol, nums[m]);
            if (nums[l] < nums[m]){
                if (nums[l] > nums[r-1]) l = m+1;
                else r = m;
            }
            else{
                if (nums[l] > nums[r-1]) r = m;
                else l = m+1;
            }
        }
        return sol;
    }
};

int main(){
    Solution s;
    vector<int> nums {3,4,5,1,2};
    s.findMin(nums);
}