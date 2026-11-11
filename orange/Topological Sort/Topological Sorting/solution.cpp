/*
Problem: Topological Sorting
Source: SPOJ
Difficulty: Secret
Time Limit: 1000ms
Memory Limit: 1024MB

Sandro is a well organised person. Every day he makes a list of things which need to be done and
enumerates them from 1 to n. However, some things need to be done before others. In this task you have
to find out whether Sandro can solve all his duties and if so, print the correct order.

Input Format:
In the first line you are given an integer n and m (1 <= n <= 10000, 1 <= m <= 1000000). On the next m
lines there are two distinct integers x and y, (1 <= x, y <= n) describing that job x needs to be done
before job y.

Output Format:
Print Sandro fails. if Sandro cannot complete all his duties on the list. If there is a solution print
the correct ordering, the jobs to be done separated by a whitespace. If there are multiple solutions
print the one, whose first number is smallest, if there are still multiple solutions, print the one
whose second number is smallest, and so on.
*/

#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

vector<int> topoSort(vector< vector<int> > &adj, vector<int> &indegree){
    int n = indegree.size();
    priority_queue<int, vector<int>, greater<int> > zero_indegree;
    vector<int> topoSorted;
    // vector<bool> avail(n, true);

    for (int i = 0; i < indegree.size(); i++)
        if (indegree[i] == 0){
            zero_indegree.push(i);
            // avail[i] = false;
        }


    while (!zero_indegree.empty()){
        int u = zero_indegree.top();
        zero_indegree.pop();

        topoSorted.push_back(u);

        for (int i = 0;i < adj[u].size(); i++){
            int v = adj[u][i];
            indegree[v] --;
            if (indegree[v] == 0){
                zero_indegree.push(v);
            }
        }
    }

    
    return topoSorted;
}

int main(){
    // n: number of vertices
    // m: number of edges
    int n, m, u, v;
    vector< vector<int> > adj;
    vector<int> indegree;
    scanf("%d %d", &n, &m);
    adj.resize(n);
    indegree.assign(n, 0);
    for (int i = 0; i < m; i++){
        scanf("%d %d", &u, &v);
        adj[u - 1].push_back(v - 1);
        indegree[v - 1] ++;
    }
    
    vector<int> res = topoSort(adj, indegree);
    if (res.size() < n){
        printf("Sandro fails.\n");
        return 0;
    }

    for (int i = 0; i < res.size(); i++)
        printf("%d ", res[i] + 1);
    printf("\n");

    return 0;
}