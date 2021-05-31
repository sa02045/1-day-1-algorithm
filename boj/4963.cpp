#include<iostream>
#include<string.h>
using namespace std;

int w,h;
int adj[50][50];
bool visited[50][50];
int cnt;
int dx[8]={-1,0,1,0,-1,-1,1,1};
int dy[8]={0,-1,0,1,-1,1,-1,1};

void dfs(int y,int x){

	for(int k=0; k<8; k++){
		int nextY = y + dy[k];
		int nextX = x + dx[k];
		if(nextX < 0 || nextY < 0 || nextX >=w || nextY >=h ) continue;
		if(visited[nextY][nextX] == false && adj[nextY][nextX] == 1){
			visited[nextY][nextX] = true;
			dfs(nextY , nextX);
		}
	}
}

int main(void){
	while(1){
		cin >> w >> h;
		if(w==0 && h==0) break;
		memset(visited,false,sizeof(visited));
		
		cnt=0;
		for(int i=0; i<h; i++){
			for(int j=0; j<w; j++){
				cin >> adj[i][j];
			}
		}
		
		for(int i=0; i<h; i++){
			for(int j=0; j<w; j++){
				if(adj[i][j]==1 && visited[i][j]==false){
					dfs(i,j);
					cnt++;
				}
			}
		}
		
		cout <<  cnt << '\n';
	}
	
	return 0;
}

