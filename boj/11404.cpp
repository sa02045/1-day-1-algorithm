#include<iostream>
#define INF 987654321

using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int n,m;
	cin >> n >> m;
	
	int adj[101][101];

	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			if(i==j) adj[i][i] =0;
			else adj[i][j] = INF;
		}
	}
	
	while(m--){
		int a,b,c;
		cin >> a >> b >> c;
		if(c < adj[a][b]) adj[a][b] = c;	
	}
	
	for(int k=1; k<=n; k++){
		for(int i=1; i<=n; i++){
			for(int j=1; j<=n; j++){
				adj[i][j] = min( adj[i][j], adj[i][k] + adj[k][j]);
			}
		}
	}
	
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			if(adj[i][j] ==INF) cout << 0 << ' ';
			else cout << adj[i][j] << ' ';  
		}
		cout << '\n';
	}
	return 0;
}
