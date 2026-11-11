/*
Problem: Book of Evil
Source: Codeforces
Difficulty: Secret
Time Limit: 2000ms
Memory Limit: 256MB

Paladin Manao caught the trail of the ancient Book of Evil in a swampy area. This area contains n
settlements numbered from 1 to n. Moving through the swamp is very difficult, so people tramped
exactly n - 1 paths. Each of these paths connects some pair of settlements and is bidirectional.
Moreover, it is possible to reach any settlement from any other one by traversing one or several paths.

The distance between two settlements is the minimum number of paths that have to be crossed to get
from one settlement to the other one. Manao knows that the Book of Evil has got a damage range d.
This means that if the Book of Evil is located in some settlement, its damage (for example, emergence
of ghosts and werewolves) affects other settlements at distance d or less from the settlement where
the Book resides.

Manao has heard of m settlements affected by the Book of Evil. Their numbers are p1, p2, ..., pm.
Note that the Book may be affecting other settlements as well, but this has not been detected yet.
Manao wants to determine which settlements may contain the Book. Help him with this difficult task.

Input Format:
The first line contains three space-separated integers n, m, d (1 <= m <= n <= 100000; 0 <= d <= n - 1).
The second line contains m distinct space-separated integers p1, p2, ..., pm (1 <= pi <= n). Then n - 1
lines follow, each line describes a path made in the area. A path is described by a pair of space-
separated integers ai and bi representing the ends of this path.

Output Format:
Print a single number - the number of settlements that may contain the Book of Evil. It is possible
that Manao received some controversial information and there is no settlement that may contain the
Book. In such case, print 0.
*/

#include <bits/stdc++.h>
#define eb emplace_back
using namespace std;
const int inf = 1e9;

typedef vector<int> vi;
typedef vector<vi> graph_type;

void dfs(graph_type& adj, vi& dist, const vector<bool>& affected, int u, int d) {
    dist[u] = -inf;
    if (affected[u]) {  
        dist[u] = d;
    }
    
    for (int v : adj[u]) {
        if (dist[v] == -1) {
            dfs(adj, dist, affected, v, d + 1);
        }
    }
}

int main() {
    int n, m, d;
    cin >> n >> m >> d;
    
    vector<bool> affected(n);
    for (int i = 0, p; i < m; ++i) {
        cin >> p;
        affected[p - 1] = true;
    }
    
    graph_type adj(n);
    for (int i = 1, x, y; i < n; ++i) {
        cin >> x >> y;
        --x; --y;
        adj[x].eb(y);
        adj[y].eb(x);
    }
    
    vi dist0(n, -1), distu(n, -1), distv(n, -1);
    dfs(adj, dist0, affected, 0, 0);
    int u = std::max_element(dist0.begin(), dist0.end()) - dist0.begin();
    dfs(adj, distu, affected, u, 0);
    int v = std::max_element(distu.begin(), distu.end()) - distu.begin();

    distu = vi(n, -1);
    dfs(adj, distu, vector<bool>(n, true), u, 0);
    dfs(adj, distv, vector<bool>(n, true), v, 0);

    int res = 0;
    for (int i = 0; i < n; ++i) {
        if (max(distu[i], distv[i]) <= d) {
            res++;
        }
    }
    
    cout << res;
}