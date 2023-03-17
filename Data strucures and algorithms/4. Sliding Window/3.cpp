/*
Given a string s, find the length of the longest 
substring
without repeating characters.
*/

/*
Intuition:
Create a set. Have a left and right pointer. Iterate the right pointer through the array. If the right pointer is in the check set already, iterate through the set until the right element is not
in the set anymore. Add the right element into the set. Once you add the set, take the max of the current right - left or what was the max solution before.
*/

#include<string>
#include<unordered_set>
#include<iostream>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int sol = 0, left = 0;
        unordered_set<char> check;
        for (int right = 0; right< s.length(); right++){
            while (check.find(s[right])!= check.end()){
                check.erase(s[left]);
                left+=1;
            }
            check.insert(s[right]);
            sol = max(sol, right-left+1);
        }     
        return sol;
    }
};

int main(){
    Solution s;
    string str = "abcabcbb";
    cout<< s.lengthOfLongestSubstring(str);
}