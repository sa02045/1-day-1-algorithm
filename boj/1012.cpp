#include<bits/stdc++.h>
using namespace std;

int adj[51][51];
bool visited[51][51];
int N,M,K;
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};
int cnt;

void dfs(int y, int x){

	visited[y][x] = true;
	
	for(int i=0; i<4; i++){
		
		int nextDy = y + dy[i];
		int nextDx = x + dx[i];
		
		if(nextDy<0 || nextDx <0  || nextDy >= N || nextDx >= M) continue;
		
		if(!visited[nextDy][nextDx] && adj[nextDy][nextDx] ==1){
			dfs(nextDy,nextDx);
		}
	}
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int T;
	cin >> T;
	
	while(T--){
		cin >> M >> N >> K;
		cnt = 0;
		memset(adj,0,sizeof(adj));
		memset(visited,0,sizeof(visited));
		while(K--){
			int X,Y;
			cin >> X >> Y;
			adj[Y][X] = 1;
		}
		
		for(int i=0; i<N; i++){
			for(int j=0; j<M; j++){
				if(adj[i][j] == 1 && !visited[i][j]){
					dfs(i,j);
					cnt++;
				}
			}
		}
		cout << cnt << '\n';
	}
	return 0;
}
