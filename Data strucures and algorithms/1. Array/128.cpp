/*
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
*/

/*
Intuition:
Convert vector to set. Iterate through new set. Look for elements that don't have the element -1 in the set. We know this is the beginning of a sequence. Add to this to a vector.
Iterate through the vector and add 1 each time to the beginning vector elements until it doesn't exist in the set. We can then find the largest sequence by checking for max between cache solution and current solution. */

#include <vector>
#include <iostream>
#include<unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        unordered_set<int> s;
        copy(nums.begin(),nums.end(), inserter(s, s.end()));
        vector<int> begin;
        for (int num: s){
            if (s.find(num-1) == s.end()) begin.push_back(num);
        }     
        int sol = 1;
        for (int num: begin){
            int check = 1;
            while(s.find(num+1) != s.end()){
                num+=1;
                check +=1;
                sol = max(check, sol);
            }
        }
        return sol;
    }
};

int main(){
    Solution s;
    vector<int> nums {100,4,200,1,3,2};
    cout<<s.longestConsecutive(nums);
}