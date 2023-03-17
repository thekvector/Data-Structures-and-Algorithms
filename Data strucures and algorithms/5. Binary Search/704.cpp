/*Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
*/

/*
Intuition:
Have a pointer pointing to the start and end of the array. Find the mid point of the start and end and check if that index equals target. If it does, return the index. If the element is less than target, we can remove the first half of the array.
Else, remove the second half.
*/

#include<vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        while (l<r){
            int mid = (l+r) /2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) l = mid+1;
            else r = mid;
        }
        return -1;
    }
};
int main(){
    Solution s;
    vector<int> nums{-1,0,3,5,9,12};
    cout<<s.search(nums, 9);
}