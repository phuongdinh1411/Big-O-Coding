/*
Problem: Beverages
Source: UVA
Difficulty: Secret
Time Limit: 3000ms
Memory Limit: 512MB

Dilbert has just finished college and decided to go out with friends. Dilbert has some strange habits
and thus he decided to celebrate this important moment of his life drinking a lot. He will start
drinking beverages with low alcohol content, like beer, and then will move to a beverage that contains
more alcohol, like wine, until there are no more available beverages. Once Dilbert starts to drink
wine he will not drink beer again, so the alcohol content of the beverages never decreases with the
time.

You should help Dilbert by indicating an order in which he can drink the beverages in the way he wishes.

Input Format:
Each test case starts with 1 <= N <= 100, the number of available beverages. Then will follow N lines,
informing the name of each beverage, a name has less than 51 characters and has no white spaces. Then
there is another line with an integer 0 <= M <= 200 and M lines in the form B1 B2 will follow,
indicating that beverage B2 has more alcohol that beverage B1, so Dilbert should drink beverage B1
before he starts drinking beverage B2. Be sure that this relation is transitive, so if there is also
a relation B2 B3 you should drink B1 before you can drink B3. There is a blank line after each test
case. In the case there is no relation between two beverages Dilbert should start drinking the one
that appears first in the input. The input is terminated by end of file (EOF).

Output Format:
For each test case you must print the message: Case #C: Dilbert should drink beverages in this order:
B1 B2 ... BN, where C is the number of the test case, starting from 1, and B1 B2 ... BN is a list of
the beverages such that the alcohol content of beverage Bi+1 is not less than the alcohol content of
beverage Bi-1. After each test case you must print a blank line.
*/

#include <iostream>
#include <map>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int V, E;

vector<int> topologicalSort(vector<vector<int>> &graph)
{
    vector<int> indegree(V, 0);
    vector<int> result;
    priority_queue<int, vector<int>, greater<int> > zero_indegree;

    for (int u = 0; u<V; u++)
    {
        vector<int>::iterator it;
        for (it = graph[u].begin(); it != graph[u].end(); it++)
            indegree[*it]++;
    }

    for (int i = 0; i < V; i++) {
        if (indegree[i]==0) {
            zero_indegree.push(i);
        }
    }

    while (!zero_indegree.empty())
    {
        int u = zero_indegree.top();
        zero_indegree.pop();

        result.push_back(u);

        vector<int>::iterator it;
        for (it = graph[u].begin(); it != graph[u].end(); it++)
        {
            indegree[*it]--;
            if (indegree[*it]==0) {
                zero_indegree.push(*it);
            }
        }
    }

    return result;
}

int main() {
    ios::sync_with_stdio(false);

    int iTest = 0;
    while (cin >> V) {
        ++iTest;

        vector<string> name(V);
        for(int u = 0; u < V; ++u)
            cin >> name[u];

        map<string, int> id;
        for(int u = 0; u < V; ++u)
            id[name[u]] = u;

        vector<vector<int>> graph;
        graph.assign(V, vector<int>());

        cin >> E;
        for(int i = 0; i < E; ++i) {
            string nameU, nameV;
            cin >> nameU >> nameV;
            int u = id[nameU], v = id[nameV];
            graph[u].push_back(v);
        }

        vector<int> topoOrd = topologicalSort(graph);

        cout << "Case #" << iTest << ": Dilbert should drink beverages in this order:";
        for(int u: topoOrd)
            cout << " " << name[u];
        cout << "." << endl;
        cout << endl;
    }

    return 0;
}