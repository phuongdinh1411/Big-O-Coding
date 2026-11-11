/*
Problem: Hierarchy
Source: SPOJ
Difficulty: Secret
Time Limit: 1500ms
Memory Limit: 1024MB

A group of graduated students decided to establish a company; however, they don't agree on who is
going to be who's boss.

Generally, one of the students will be the main boss, and each of the other students will have exactly
one boss (and that boss, if he is not the main boss, will have a boss of his own too). Every boss will
have a strictly greater salary than all of his subordinates - therefore, there are no cycles. Therefore,
the hierarchy of the company can be represented as a rooted tree.

In order to agree on who is going to be who's boss, they've chosen K most successful students, and each
of them has given a statement: I want to be the superior of him, him, and him (they could be successful
or unsuccessful). And what does it mean to be a superior? It means to be the boss, or to be one of the
boss' superiors (therefore, a superior of a student is not necessary his direct boss).

Help this immature company and create a hierarchy that will satisfy all of the successful students'
wishes. A solution, not necessary unique, will exist in all of the test data.

Input Format:
In the first line of input, read positive integers N (N <= 100000), total number of students, and K
(K < N), the number of successful students. All students are numbered 1..N, while the successful ones
are numbered 1..K. Then follow K lines. In A-th of these lines, first read an integer W (the number of
wishes of the student A, 1 <= W <= 10), and then W integers from the range [1, N] which denote students
which student A wants to be superior to.

Output Format:
Output N integers. The A-th of these integers should be 0 if student A is the main boss, and else it
should represent the boss of the student A.
*/

#include <bits/stdc++.h>
using namespace std;

void dfs(int u, const vector<vector<int>> &graph, vector<bool> &visited, vector<int> &result) {
    visited[u] = true;
    for (int i = 0; i < graph[u].size(); i++) {
        int v = graph[u][i];
        if (!visited[v]) {
            dfs(v, graph, visited, result);
        }
    }
    result.push_back(u);
}

vector<int> topologicalSort(const vector<vector<int>> &graph) {
    int V = graph.size();
    vector<int> result;
    result.reserve(V);
    vector<bool> visited(V, false);

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfs(i, graph, visited, result);
        }
    }
    std::reverse(result.begin(), result.end());
    return result;
}

int main() {
    int n, k;
    scanf("%d%d", &n, &k);
    vector<vector<int>> graph(n);
    for (int u = 0; u < k; ++u) {
        int w, v;
        scanf("%d", &w);
        while (w--) {
            scanf("%d", &v);
            graph[u].push_back(v - 1);
        }
    }

    auto topo_order = topologicalSort(graph);
    vector<int> boss(n);
    boss[topo_order[0]] = -1;
    for (int i = 1; i < n; ++i) {
        boss[topo_order[i]] = topo_order[i - 1];
    }
    
    for (int i = 0; i < n; ++i) {
        printf("%d\n", boss[i] + 1);
    }
}