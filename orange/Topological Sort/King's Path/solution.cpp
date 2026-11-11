/*
Problem: King's Path
Source: Codeforces
Difficulty: Secret
Time Limit: 1000ms
Memory Limit: 1024MB

The black king is standing on a chess field consisting of 10^9 rows and 10^9 columns. We will consider
the rows of the field numbered with integers from 1 to 10^9 from top to bottom. The columns are similarly
numbered with integers from 1 to 10^9 from left to right. We will denote a cell of the field that is
located in the i-th row and j-th column as (i, j).

You know that some squares of the given chess field are allowed. All allowed cells of th chess field
are given as n segments. Each segment is described by three integers ri, ai, bi (ai <= bi), denoting
that cells in columns from number ai to number bi inclusive in the ri-th row are allowed.

Your task is to find the minimum number of moves the king needs to get from square (x0, y0) to square
(x1, y1), provided that he only moves along the allowed cells. In other words, the king can be located
only on allowed cells on his way.

Let us remind that a chess king can move to any of the neighboring cells in one move. Two cells of a
chess field are considered neighboring if they share at least one point.

Input Format:
The first line contains four space-separated integers x0, y0, x1, y1 (1 <= x0, y0, x1, y1 <= 10^9),
denoting the initial and the final positions of the king.

The second line contains a single integer n (1 <= n <= 10^5), denoting the number of segments of
allowed cells. Next n lines contain the descriptions of these segments. The i-th line contains three
space-separated integers ri, ai, bi (1 <= ri, ai, bi <= 10^9, ai <= bi), denoting that cells in columns
from number ai to number bi inclusive in the ri-th row are allowed. Note that the segments of the
allowed cells can intersect and embed arbitrarily.

It is guaranteed that the king's initial and final position are allowed cells. It is guaranteed that
the king's initial and the final positions do not coincide. It is guaranteed that the total length
of all given segments doesn't exceed 10^5.

Output Format:
If there is no path between the initial and final position along allowed cells, print -1.
Otherwise print a single integer - the minimum number of moves the king needs to get from the initial
position to the final one.
*/

#include <iostream>
#include <set>
#include <map>
#include <queue>

using namespace std; 
const long long limit = 1000000000; 

set <long long> mark; 
map <long long, int> dist; 
long long x0, y0, x1, y1; 
int n; 
int dx[] = {0, 0, 1, -1, 1, -1, 1, -1}; 
int dy[] = {1, -1, 0, 0, 1, -1, -1, 1}; 

long long calc(long long x, long long y) {
	long long val = x; 
	val = val * 1000000000LL + y; 
	return val; 
}

void bfs() {
	queue <long long> myqueue;
	long long S = calc(x0, y0);
	myqueue.push(S);
	dist[S] = 0;

	while (!myqueue.empty()) {
		long long u = myqueue.front(); 
		myqueue.pop(); 
		long long x = u / limit; 
		long long y = u % limit;
		for (int i = 0; i < 8; i++) {
			long long xx = x + dx[i]; 
			long long yy = y + dy[i];
			long long v = calc(xx, yy);  
			if (xx >= 1 && xx <= limit && yy >= 1 && yy <= limit && (mark.find(v) != mark.end())) {
				if (dist.find(v) == dist.end()) {
					dist[v] = dist[u] + 1;          
					if (v == calc(x1, y1)) {
		        cout << dist[v]; 
						return; 
					}

					myqueue.push(v); 
				}
			}
		}
	}

  cout << -1;                            
}

int main () {
	// freopen("input.txt", "r", stdin);
	// freopen("output.txt", "w", stdout);
	cin >> x0 >> y0 >> x1 >> y1; 
	mark.insert(calc(x0, y0));   
	mark.insert(calc(x1, y1)); 

	cin >> n; 
	for (int i = 1; i <= n; i++) {
		long long r, a, b; 
		cin >> r >> a >> b; 
		for (long long j = a; j <= b; j++) {
			mark.insert(calc(r, j)); 
		}
	}
                             
  bfs();
  return 0; 
}