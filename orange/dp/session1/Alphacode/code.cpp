/*
Problem: Alphacode
Source: SPOJ
Difficulty: Secret
Time Limit: 2000ms
Memory Limit: 512MB

Alice and Bob need to send secret messages to each other and are discussing ways to encode their messages:

Alice: "Let's just use a very simple code: We'll assign A the code word 1, B will be 2, and so on down
to Z being assigned 26."

Bob: "That's a stupid code, Alice. Suppose I send you the word BEAN encoded as 25114. You could decode
that in many different ways!"

Alice: "Sure you could, but what words would you get? Other than BEAN, you'd get BEAAD, YAAD, YAN, YKD
and BEKD. I think you would be able to figure out the correct decoding. And why would you send me the
word BEAN anyway?"

Bob: "OK, maybe that's a bad example, but I bet you that if you got a string of length 5000 there would
be tons of different decodings and with that many you would find at least two different ones that would
make sense."

Alice: "How many different decodings?"
Bob: "Jillions!"

For some reason, Alice is still unconvinced by Bob's argument, so she requires a program that will
determine how many decodings there can be for a given string using her code.

Input Format:
Input will consist of multiple input sets. Each set will consist of a single line of at most 5000 digits
representing a valid encryption (for example, no line will begin with a 0). There will be no spaces
between the digits. An input line of 0 will terminate the input and should not be processed.

Output Format:
For each input set, output the number of possible decodings for the input string. All answers will be
within the range of a 64 bit signed integer.
*/

#include <bits/stdc++.h>

using namespace std;

long long solve(string& n){
    vector<long long> dp(n.length() + 1, 0);
    long long temp = 0;
    int tmp = 0;

    dp[0] = dp[1] = 1;
    for(int i = 2; i <= n.length(); ++i){
        tmp = (n[i - 2] - '0') * 10 + (n[i - 1] - '0');
        if(n[i - 1] != '0') dp[i] = dp[i - 1];
        if(tmp <= 26 && tmp >= 10) dp[i] += dp[i - 2];
    }

    return dp.back();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string n;

    while(cin >> n){
        if(n == "0") break;
        cout << solve(n) << '\n';
    }

    return 0;
}