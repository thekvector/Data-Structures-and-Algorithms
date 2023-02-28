/*
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
*/

/*
Intution:
Traverse through the array and tag the indices of all of the numbers in the array by multiplying by -1. Traverse through again. Whatever index is greater than 0, we know it doesn't exist in the array.
*/

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (int i = 0; i<nums.size(); i++){
            int check = abs(nums[i]);
            int index = check -1;
            if(nums[index]>0) nums[index] *=-1;
        }     
        vector<int> sol;
        for (int i = 0; i<nums.size(); i++){
            if(nums[i] >0) sol.push_back(i+1);
        }
        return sol;
    }
};

int main(){
    Solution s;
    vector<int> nums {4,3,2,7,8,2,3,1};
    s.findDisappearedNumbers(nums);
}