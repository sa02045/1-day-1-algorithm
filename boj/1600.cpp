#include<iostream>
#include<queue>

using namespace std;
int K,W,H;

int adj[201][201];
int visited[201][201][32];
typedef struct
{
	int y,x;
}Dir;

Dir dir[4] = { {1,0},{-1,0},{0,1},{0,-1}};
Dir knightDir[8] = {{ -1, -2 },{ -2, -1 },{ -2, 1 },{ -1, 2 },{ 2, 1 },{ 1, 2 },{ 2, -1 },{ 1, -2 }};

int bfs(int y, int x){
	queue <pair< pair<int,int>, pair<int,int> > > q;
	q.push(make_pair(make_pair(y,x) , make_pair(0,0)));
	visited[y][x][0]=1;
	
	while(!q.empty()){
		int curY = q.front().first.first;
		int curX = q.front().first.second;
		int knightCnt = q.front().second.first;
		int cnt = q.front().second.second;
		q.pop();
		
		if(curY == H-1 && curX == W-1){
			return cnt;
		}
		
		if(knightCnt < K){
			for(int i=0; i<8; i++){
				int nextY = curY + knightDir[i].y;
				int nextX = curX + knightDir[i].x;
				
				if(nextY <0 || nextX <0 || nextY > H || nextX > W) continue;
			
				if(!visited[nextY][nextX][knightCnt+1] && adj[nextY][nextX]==0){
					visited[nextY][nextX][knightCnt+1]=true;
					q.push( make_pair(make_pair(nextY,nextX),make_pair(knightCnt+1,cnt+1)));
				}
			}
		}
		
		for(int i=0; i<4; i++){
			int nextY = curY + dir[i].y;
			int nextX = curX + dir[i].x;
			
			if(nextY <0 || nextX <0 || nextY > H || nextX > W) continue;
			
			if(!visited[nextY][nextX][knightCnt] && adj[nextY][nextX]==0){
				visited[nextY][nextX][knightCnt] = true;
				q.push(make_pair(make_pair(nextY,nextX) , make_pair(knightCnt,cnt+1)));
			}
		}
	}
	return -1;
}

int main(void){
	cin.tie(0);
	cin >> K >> W >> H;
	for(int i=0; i<H; i++){
		for(int j=0; j<W; j++){
			cin >> adj[i][j];
		}
	}
	
	cout << bfs(0,0) << '\n';
	return 0;
}
