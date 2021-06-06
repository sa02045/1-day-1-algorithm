#include<iostream>
#include<vector>
#include<queue>
#include<string.h>


using namespace std;

int dx[8]={-2,-2,-1,-1,1,1,2,2};
int dy[8]={-1,1,-2,2,-2,2,-1,1};
bool visited[300][300];
int T,L;
pair<int,int> night,dest;

int main(void){
	int T;
	cin >> T;
	cout << T;
	
	while(T--){
		cin >> L;
		cin >> night.first >> night.second;
		cin >> dest.first >> dest.second;
		
		memset(visited,false,sizeof(visited));
		visited[night.first][night.second] = true;
		queue< pair< pair<int,int> ,int> > q;
		q.push(make_pair(night,0));

int ans;
		while(!q.empty()){
			int curY = q.front().first.first;
			int curX = q.front().first.second;
			int curCnt = q.front().second;
 			q.pop();
			
			if(curY==dest.first && curX == dest.second){
				ans=curCnt;
				break;
			}
			
			for(int i=0; i<8; i++){
				int nextY = curY + dy[i];
				int nextX = curX + dx[i];
				
				if(nextX <0 || nextY<0 || nextX>=L || nextY>=L) continue;
				
				if(visited[nextY][nextX] ==false ){
					visited[nextY][nextX] = true;
					q.push( make_pair( make_pair(nextY,nextX),curCnt+1));		
				};
			}
		}
		cout << ans << '\n';
	}

	return 0;
}
