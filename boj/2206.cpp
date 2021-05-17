#include <bits/stdc++.h>

using namespace std;

int N,M;
int adj[1001][1001];

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> M;
	
	for(int i=0; i<N; i++){
		string s;
		cin >> s;
		for(int j=0; j<M; j++){
			if(s[j]=='1'){
				adj[i][j] = 1;
			}
		}
	}
	
	bfs(0,0);
	
	return 0;
}
