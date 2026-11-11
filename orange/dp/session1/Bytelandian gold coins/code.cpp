/*
Problem: Bytelandian gold coins
Source: SPOJ
Difficulty: Secret
Time Limit: 1000ms
Memory Limit: 512MB

In Byteland they have a very strange monetary system. Each Bytelandian gold coin has an integer number
written on it. A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4. But these numbers
are all rounded down (the banks have to make a profit). You can also sell Bytelandian coins for American
dollars. The exchange rate is 1 : 1. But you can not buy Bytelandian coins.

You have one gold coin. What is the maximum amount of American dollars you can get for it?

Input Format:
The input will contain several test cases (not more than 10). Each testcase is a single line with a
number n, 0 <= n <= 1000000000. It is the number written on your coin.

Output Format:
For each test case output a single line, containing the maximum amount of American dollars you can make.
*/

#include <bits/stdc++.h>

using namespace std;

long long solve(vector<long long> &dp, long long n)
{
    if (n <= 10)
    {
        return dp[n] = n;
    }

    if (n < 1e7)
    {
        if (!dp[n])
        {
            int tmp = max(n, solve(dp, n / 2) + solve(dp, n / 3) + solve(dp, n / 4));
            dp[n] = tmp;
        }
        else
        {
            return dp[n];
        }
    }

    return max(n, solve(dp, n / 2) + solve(dp, n / 3) + solve(dp, n / 4));
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<long long> dp(1e7, 0);
    long long n;

    while (cin >> n)
    {
        cout << solve(dp, n) << '\n';
    }

    return 0;
}