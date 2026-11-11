/*
Problem: Ingenuous Cubrency
Source: UVA
Difficulty: Secret
Time Limit: 1000ms
Memory Limit: 512MB

People in Cubeland use cubic coins. Not only the unit of currency is called a cube but also the coins
are shaped like cubes and their values are cubes. Coins with values of all cubic numbers up to
9261 (= 21^3), i.e., coins with the denominations of 1, 8, 27, ..., up to 9261 cubes, are available
in Cubeland.

Your task is to count the number of ways to pay a given amount using cubic coins of Cubeland. For
example, there are 3 ways to pay 21 cubes: twenty one 1 cube coins, or one 8 cube coin and thirteen
1 cube coins, or two 8 cube coin and five 1 cube coins.

Input Format:
Input consists of lines each containing an integer amount to be paid. You may assume that all the
amounts are positive and less than 10000.

Output Format:
For each of the given amounts to be paid output one line containing a single integer representing
the number of ways to pay the given amount using the coins available in Cubeland.
*/

#include <bits/stdc++.h>

using namespace std;

long long solve(int total, int coins[], int n){
    vector<long long> dp(total + 1);

    dp[0] = 1;
    for(int i = 0; i < n; ++i){
        for(int j = coins[i]; j <= total; ++j){
            dp[j] += dp[j - coins[i]];
        }
    }

    return dp[total];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    int coins[21];

    for(int i = 0; i < 21; ++i){
        coins[i] = pow(i + 1, 3);
    }

    while(cin >> n){
        cout << solve(n, coins, 21) << '\n';
    }

    return 0;
}