#include<bits/stdc++.h>

using namespace std;

int N,M;
int dx[4] = {-1,0,1,0};
int dy[4] = {0,-1,0,1};
int adj[1001][1001];
bool visited[1001][1001];

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	queue< pair< pair<int,int>, int> > q;
	
	cin >> N >> M;
	
	for(int i=0; i<M; i++){
		for(int j=0; j<N; j++){
			cin >> adj[i][j];
			if(adj[i][j]==1){
				q.push( make_pair(make_pair(i,j),1));
				visited[i][j] = true;
			}
		}
	}
	
	
	
	while(!q.empty()){
		int y = q.front().first.first;
		int x = q.front().first.second;
		int count = q.front().second;
		q.pop();
		
		adj[y][x] = count;

		for(int i=0; i<4; i++){
			int nextDy = y + dy[i];
			int nextDx = x + dx[i];
			
			if(nextDy<0 || nextDx<0|| nextDx >=N || nextDy >=M ) continue;
			
			if(adj[nextDy][nextDx] == 0 && !visited[nextDy][nextDx]){
				q.push( make_pair(make_pair(nextDy,nextDx),count+1));
				visited[nextDy][nextDx] = true;
			}
		}
	}
	
	int max=0;
	
	for(int i=0; i<M; i++){
		for(int j=0; j<N; j++){
			if(adj[i][j]==0){
				cout << -1;
				return 0;
			}
			if(max < adj[i][j]){
				max = adj[i][j];
			}
		}
	}
	
	cout << max-1;
	return 0;
}
