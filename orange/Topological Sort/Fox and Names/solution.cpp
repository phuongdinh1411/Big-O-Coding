/*
Problem: Fox and Names
Source: Codeforces
Difficulty: Secret
Time Limit: 2000ms
Memory Limit: 256MB

Fox Ciel is going to publish a paper on FOCS (Foxes Operated Computer Systems, pronounstrce: "Fox").
She heard a rumor: the authors list on the paper is always sorted in the lexicographical order.

After checking some examples, she found out that sometimes it wasn't true. On some papers authors'
names weren't sorted in lexicographical order in normal sense. But it was always true that after some
modification of the order of letters in alphabet, the order of authors becomes lexicographical!

She wants to know, if there exists an order of letters in Latin alphabet such that the names on the
paper she is submitting are following in the lexicographical order. If so, you should find out any
such order.

Lexicographical order is defined in following way. When we compare s and t, first we find the leftmost
position with differing characters: si != ti. If there is no such position (i. e. s is a prefix of t
or vice versa) the shortest string is less. Otherwise, we compare characters si and ti according to
their order in alphabet.

Input Format:
The first line contains an integer n (1 <= n <= 100): number of names.
Each of the following n lines contain one string namei (1 <= |namei| <= 100), the i-th name. Each
name contains only lowercase Latin letters. All names are different.

Output Format:
If there exists such order of letters that the given names are sorted lexicographically, output any
such order as a permutation of characters 'a'-'z' (i. e. first output the first letter of the
modified alphabet, then the second, and so on).

Otherwise output a single word "Impossible" (without quotes).
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> InputNames() {
    int n;
    cin >> n;
    
    string cache;
    getline(cin, cache);

    vector<string> names(n, string());
    for (int i = 0; i < n; ++i) {
        getline(cin, names[i]);
    }
    return names;
}

vector<vector<int>> SetupLexicographical(const vector<string> & names) {
    vector<vector<int>> lexicographical(26, vector<int>());
    vector<vector<bool>> relation(26, vector<bool>(26, false));

    bool flag;

    for (int i = 0; i < names.size() - 1; ++i) {
        flag = false;
        int minSize = names[i].length() < names[i + 1].length() ? names[i].length() : names[i + 1].length();
        for (int j = 0; j < minSize; ++j) {
            if (names[i][j] != names[i + 1][j]) {
                relation[names[i][j] - 97][names[i + 1][j] - 97] = true;
                flag = true;
                break;
            }
        }
        if (!flag && (names[i].length() > names[i + 1].length())) {
            cout << "Impossible";
            exit(0);
        }
    }

    for (int i = 0; i < 26; ++i) {
        for (int j = 0; j < 26; ++j) {
            if (relation[i][j]) {
                lexicographical[i].emplace_back(j);
            }
        }
    }

    return lexicographical;
}

pair<bool, string> TopoSort(vector<vector<int>> & lexicographical) {
    vector<int> inDegrees(26, 0);
    pair<bool, string> result;
    vector<int> zeroInDegree;

    for (int u = 0; u < 26; ++u) {
        vector<int>::iterator it;
        for (it = lexicographical[u].begin(); it != lexicographical[u].end(); ++it) {
            inDegrees[*it]++;
        }
    }

    for (int i = 0; i < 26; ++i) {
        if (inDegrees[i] == 0) {
            zeroInDegree.emplace_back(i);
        }
    }

    while (!zeroInDegree.empty()) {
        int u = zeroInDegree.back();
        zeroInDegree.pop_back();
        result.second.push_back(u + 97);
        vector<int>::iterator it;
        for (it = lexicographical[u].begin(); it != lexicographical[u].end(); ++it) {
            inDegrees[*it]--;
            if (inDegrees[*it] == 0) {
                zeroInDegree.emplace_back(*it);
            }
        }
    }

    for (int i = 0; i < 26; ++i) {
        if (inDegrees[i] != 0) {
            return pair<bool, string>(false, string());
        }
    }

    result.first = true;
    return result;
}

int main() {
    vector<string> names = InputNames();
    vector<vector<int>> lexicographical = SetupLexicographical(names);
    pair<bool, string> result = TopoSort(lexicographical);
    if (!result.first) {
        cout << "Impossible";
    }
    else {
        for (auto & i : result.second) {
            cout << i;
        }
    }
    return 0;
}