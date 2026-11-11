/*
Problem: K-based Numbers
Source: Timus Online Judge
Difficulty: Secret
Time Limit: 500ms
Memory Limit: 256MB

Let's consider K-based numbers, containing exactly N digits. We define a number to be valid if its
K-based notation doesn't contain two successive zeros. For example:

- 1010230 is a valid 7-digit number;
- 1000198 is not a valid number;
- 0001235 is not a 7-digit number, it is a 4-digit number.

Given two numbers N and K, you are to calculate an amount of valid K based numbers, containing N digits.
You may assume that 2 <= K <= 10; N >= 2; N + K <= 18.

Input Format:
The numbers N and K in decimal notation separated by the line break.

Output Format:
The result in decimal notation.
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
  	ios::sync_with_stdio(false);
  	cin.tie(NULL);
  	cout.tie(NULL);
  
    vector<vector<int>> dp;
    int n, k;

    cin >> n >> k;
    if(n == 1){
        cout << n;

        return 0;
    }

    int curr = 1;

    dp.push_back({1, k - 1});
    while(curr < n - 1){
        dp.push_back({0, 0});
        dp[curr][0] = dp[curr - 1][1];
        dp[curr][1] = (dp[curr - 1][0] + dp[curr - 1][1]) * (k - 1);
        ++curr;
    }

    cout << dp[curr-1][0] * (k - 1) + dp[curr - 1][1] * (k - 1);

    return 0;
}