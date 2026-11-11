/*
Problem: Answer the boss!
Source: SPOJ
Difficulty: Secret
Time Limit: 1000ms
Memory Limit: 1024MB

Eloy is a hard worker man, however, he is constantly bullied by his superiors, molested by this, one
day he was wondering in what "rank" you are, so you can bully the people with lower ranks, also to
discover who can really bully Eloy!.

Now, given the number of employees and the number of relations between them, Eloy need you to output
the "rank" which employee is in, being 1 the "boss" (not bullied by anybody) and the employee who are
in these ranks.

Input Format:
There will be an integer T denoting the test cases, then, T test cases will follow, each test case
starts with two integers N and R, the number of employees and the number of relations between them,
the next R lines consists in two integers R1 and R2, meaning that "employee R1 is lower than employee
R2's rank".

CONSTRAINTS: 1 <= N <= 1000, 1 <= R <= 10000

Output Format:
You will output for each test case the string "Scenario #i:" where i is the test case you are analyzing,
after that, you will print N lines, for each line you will output the rank of the employee and the
employee itself, if there is the same rank for several employees, then output them lexicographically
ordered (the first is the lower)
*/

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Employee {
    int index;
    int rank;

    Employee(int index, int rank) : index(index), rank(rank) {}
};

void dfs(int u, vector<vector<int>>& adj, vector<int>& visited, vector<int>& topoOrder) {
    visited[u] = 1;

    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v, adj, visited, topoOrder);
        }
    }

    topoOrder.push_back(u);
}

vector<int> topoSort(vector<vector<int>>& adj) {
    vector<int> topoOrder;
    int n = adj.size();
    vector<int> visited(n, 0);

    for (int u = 0; u < n; u++) {
        if (!visited[u]) {
            dfs(u, adj, visited, topoOrder);
        }
    }

    reverse(topoOrder.begin(), topoOrder.end());

    return topoOrder;
}

void solveTest(int testNumber) {
    int n, r;
    cin >> n >> r;

    vector<vector<int>> adj(n, vector<int>());
    vector<int> inDeg(n, 0);

    for (int i = 0; i < r; i++) {
        int u, v;
        cin >> u >> v;
        adj[v].push_back(u);
        ++inDeg[u];
    }

    vector<int> topoOrder = topoSort(adj);
    vector<int> rank(n);

    for (int u  : topoOrder) {
        if (inDeg[u] == 0) {
            rank[u] = 1;
        }
        for (int v : adj[u]) {
            rank[v] = max(rank[v], rank[u] + 1);
        }
    }

    vector<Employee> employees;

    for (int u = 0; u < n; u++) {
        employees.push_back(Employee(u, rank[u]));
    }

    sort(employees.begin(), employees.end(), [](const Employee& e1, const Employee& e2) {
        if (e1.rank == e2.rank) {
            return e1.index < e2.index;
        }
        return e1.rank < e2.rank;
    });
    
    cout << "Scenario #" << testNumber << ":\n";

    for (Employee& e : employees) {
        cout << e.rank << ' ' << e.index << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    for (int testNumber = 1; testNumber <= t; testNumber++) {
        solveTest(testNumber);
    }    

    return 0;
}