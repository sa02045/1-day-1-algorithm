#include <iostream>

using namespace std;

int originAdj[8][8];
int copyAdj[8][8];
int N,M;
int minAnswer;


void makeWall(int cnt){
	if(cnt == 3){
		BFS();
		return ;
	}
	
	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			if(copyAdj[i][j] == 0){
				copyAdj[i][j] = 1;
				makeWall(cnt+1);
				copyAdj[i][j] = 0;
			}
		}
	}
}


void copyAdj(){
	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			copyAdj[i][j] = originAdj[i][j];
		}
	}
}

int main(void){
	cin >> N >> M;
	
	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			cin >> originAdj[i][j];
		}
	}
	
	
	
	
	
	// 1. input
	// 2. copy한 배열에 벽 3개 세우기
	// 3. copy배열을 spread
	// 4. 갯수 세고 미니멈 갱신
	// 5.  
	return 0;
}
