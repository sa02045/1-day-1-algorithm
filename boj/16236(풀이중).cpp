#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int dy[4] = {-1,0,1,0};
int dx[4] = {0,-1,0,1};
bool visited[21][21];


int main(void){
	int N;
	cin >> N;
	int adj[21][21];
	
	vector<pair<int,int> > sharkStart;
	queue < pair<pair<int,int>,int> > q;
	int startSharkY;
	int startSharkX;
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			cin >> adj[i][j];			
			if(adj[i][j]==9){
				q.push( make_pair( make_pair(i,j) ,0) );
				visited[i][j]=true;
			}
		}
	}

	int sharkSize = 2;
	
	
	while(1){
		// 종료조건 
		bool exit = false;
		for(int i=0; i<N; i++){
			for(int j=0; j<N; j++){
				if(adj[i][j]!=0 && adj[i][j] < sharkSize) exit =true;
				break;
			}
		}
		if(!exit) break;
		
		
		int y = q.front().first.first;
		int x = q.front().first.first;
		int time = q.front().second;
		 
		q.pop();
		
		for(int i=0; i<4; i++){
			int nextY = y + dy[i];
			int nextX = x + dx[i];
			
			if(nextX<0 || nextX>=N || nextY<0 || nextY>=N) continue;
			
			if(adj[nextY][nextX] >= sharkSize) continue;
			
			q.push( make_pair(make_pair(nextY,nextX),time++) );
			visited[nextY][nextX] = true;
		}
		
	}
	
	while(!q.empty()){
		int y = q.front().first.first;
		int x = q.front().first.first;
		int time = q.front().second;
		 
		q.pop();
		
		for(int i=0; i<4; i++){
			int nextY = y + dy[i];
			int nextX = x + dx[i];
			
			if(nextX<0 || nextX>=N || nextY<0 || nextY>=N) continue;
			
			if(adj[nextY][nextX] >= sharkSize) continue;
			
			q.push( make_pair(make_pair(nextY,nextX),time++) );
			visited[nextY][nextX] = true;
		}
	}
	return 0;
}
