#include <iostream>
#include <queue>
#define INF 987654321

using namespace std;

vector< pair<int,int> > adj[801];

vector<int> dijk(int start){
	priority_queue < pair<int,int> > pq;
	vector<int> dist(801,INF);
	dist[start]=0;
	pq.push( make_pair(0,start));
	
	while(!pq.empty()){
		
		int curDist = -pq.top().first;
		int curVertex = pq.top().second;
		pq.pop();
		
		if(dist[curVertex] < curDist) continue;
		
		for(int i=0; i<adj[curVertex].size(); i++){
			int nextVertex = adj[curVertex][i].second;
			int nextDist = curDist + adj[curVertex][i].first;
			
			if(nextDist < dist[nextVertex]){
				dist[nextVertex] = nextDist;
				pq.push( make_pair( -nextDist,nextVertex));
			}
		}
	}
	return dist;
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int N,E;
	cin >> N >> E;
	
	while(E--){
		int a,b,c;
		cin >> a >> b >> c;
		adj[a].push_back( make_pair(c,b));
		adj[b].push_back( make_pair(c,a));
	}
	
	int v1,v2;
	cin >>v1 >>v2;

 	// start -> v1 -> v2 -> N
 	// start -> v2 -> v1 -> N
 	vector<int> startDist = dijk(1);
 	vector<int> v1Dist = dijk(v1);
 	vector<int> v2Dist = dijk(v2);
 	
 	if(startDist[v1]==INF && startDist[v2]==INF){
 		cout << -1;
 		return 0;
	 }
	 
	 if(v1Dist[v2] == INF || (v2Dist[N]==INF && v1Dist[N]==INF)){
	 	cout << -1;
	 	return 0;
	 }
	 
 
	cout << min(startDist[v1]+v1Dist[v2]+v2Dist[N] , startDist[v2]+v2Dist[v1]+v1Dist[N]);
	
	return 0;
}
