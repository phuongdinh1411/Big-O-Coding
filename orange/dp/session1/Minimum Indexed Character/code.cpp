/*
Problem: Minimum Indexed Character
Source: Geeksforgeeks
Difficulty: Secret
Time Limit: 1000ms
Memory Limit: 512MB

Given a string str and another string patt. Find the character in patt that is present at the minimum
index in str. If no character of patt is present in str then print 'No character present'.

Input Format:
The first line of input contains an integer T denoting the number of test cases. Then the description
of T test cases follow. Each test case contains two strings str and patt respectively.

1 <= T <= 10^5
The total length of two strings in all testcase is not larger than 2 * 10^5.

Output Format:
Output the character in patt that is present at the minimum index in str. Print "No character present"
(without quotes) if no character of patt is present in str.
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    string patt;
    string str;
    string ans = "No character present";
    unordered_set<char> counting;

    cin >> t;
    while(t--){
        if(!counting.empty()) counting.clear();
        cin >> patt >> str;
        ans = "No character present";
        for(auto& c : str){
            counting.insert(c);
        }
        for(auto& c : patt){
            if(counting.find(c) != counting.end()){
                ans = c;
                break;
            }
        }
        cout << ans << '\n';
    }

    return 0;
}