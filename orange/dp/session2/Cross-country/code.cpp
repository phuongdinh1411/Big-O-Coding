/*
Problem: Cross-country
Source: SPOJ
Difficulty: Secret
Time Limit: 2000ms
Memory Limit: 512MB

Agnes, a student of computer science, is very keen on cross-country running, and she participates in
races organised every Saturday in a big park. Each of the participants obtains a route card, which
specifies a sequence of checkpoints, which they need to visit in the given order. Agnes is a very
attractive girl, and a number of male runners have asked her for a date. She would like to choose one
of them during the race. Thus she invited all her admirers to the park on Saturday and let the race
decide. The winner would be the one, who scores the maximum number of points. Agnes came up with the
following rules:

- a runner scores one point if he meets Agnes at the checkpoint,
- if a runner scored a point at the checkpoint, then he cannot get another point unless he and Agnes
  move to the next checkpoints specified in their cards.
- route specified by the card may cross the same checkpoint more than once,
- each competitor must strictly follow race instructions written on his card.

Between two consecutive meetings, the girl and the competitors may visit any number of checkpoints.
The boys will be really doing their best, so you may assume, that each of them will be able to visit
any number of checkpoints whilst Agnes runs between two consecutive ones on her route.

You should write a program which for each data set from a sequence of several data sets:
- reads in the contents of Agnes' race card and contents of race cards presented to Tom,
- computes the greatest number of times Tom is able to meet Agnes during the race,
- writes it to output.

Input Format:
There is one integer d in the first line of the input file, 1 <= d <= 10. This is the number of data
sets. The data sets follow. Each data set consists of a number of lines, with the first one specifying
the route in Agnes' race card. Consecutive lines contain routes on cards presented to Tom. At least one
route is presented to Tom. The route is given as a sequence of integers from interval [1, 1000] separated
by single spaces. Number 0 stands for the end of the route, though when it is placed at the beginning of
the line it means the end of data set. There are at least two and at most 2000 checkpoints in a race card.

Output Format:
The i-th line of the output file should contain one integer. That integer should equal the greatest
number of times Tom is able to meet with Agnes for race cards given in the i-th data set.
*/

#include <bits/stdc++.h>

using namespace std;

int solve(vector<int>& agnes, vector<int>& tom){
    vector<vector<int>> dp;

    dp.resize(agnes.size() + 1, vector<int>(tom.size() + 1, 0));

    for(int i = 1; i <= agnes.size(); ++i){
        for(int j = 1; j <= tom.size(); ++j){
            if(agnes[i - 1] == tom[j - 1]){
                dp[i][j] = dp[i - 1][j - 1] + 1;
            }
            else{
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp.back().back();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, tmp;
    int ans = -1e9;
    bool isZero = 0;
    vector<int> agnes;
    vector<vector<int>> tom; 

    cin >> t;
    while(t--){
        ans = -1e9;
        if(!tom.empty()){
            for(auto& v : tom) v.clear();
            tom.clear();
            agnes.clear();
        }

        cin >> tmp;
        while(tmp){
            agnes.push_back(tmp);
            cin >> tmp;
        }
        agnes.push_back(tmp);

        tom.push_back(vector<int>());
        while(cin >> tmp){
            if(!tmp){
                if(isZero) break;
                isZero = 1;
                // tom.back().push_back(tmp);
                tom.push_back(vector<int>());

                continue;
            }
            else{
                isZero = 0;
            }

            tom.back().push_back(tmp);
        }

        for(auto& route : tom){
            ans = max(ans, solve(agnes, route));
        }
        cout << ans << '\n';
    }

    return 0;
}