#include <iostream>
#include <queue>
#define INF 987654321
using namespace std;

vector< pair<int,int> > adj[1001];
int N,M,X;
int result[1001];

vector<int> dijk(int start){
	vector<int> dist(N+1,INF);
	priority_queue < pair<int,int> > pq;
	dist[start] = 0;
	pq.push( make_pair(0,start) );
	
	while(!pq.empty()){
		
		int curDist = -pq.top().first;
		int curVertex = pq.top().second;
		pq.pop();
		
		if( dist[curVertex] < curDist) continue;
		
		for(int i=0; i<adj[curVertex].size(); i++){
			int nextVertex = adj[curVertex][i].second;
			int nextDist = adj[curVertex][i].first + curDist;
			
			if( nextDist < dist[nextVertex]){
				dist[nextVertex] = nextDist;
				pq.push( make_pair( -nextDist , nextVertex));
			}
		}
	}
	return dist;
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> M >> X;
	
	while(M--){
		int start,end,time;
		cin >> start >> end >> time;
		adj[start].push_back( make_pair (time,end));
	}
	
	vector <int> startDist = dijk(X);
	
	for(int i=1; i<=N; i++){
		result[i] =startDist[i] + dijk(i)[X];
	}

	
	
	int max;
	for(int i=1; i<=N; i++){
		if(i==1) max = result[i];
		
		if(max<result[i]){
			max = result[i];
		}
	}
	
	cout << max;
	return 0;
}
