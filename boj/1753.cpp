#include <iostream>
#include <queue>
#define INT_MAX 987654321

using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int V,E,K;
	cin >> V >> E;
	cin >> K;
	
	vector< pair<int,int> > graph[V+1];
	vector<int> dist(V+1,INT_MAX);
	
	while(E--){
		int u,v,w;
		cin >> u >> v >> w;
		graph[u].push_back( make_pair(w,v));
	}
	
	priority_queue< pair<int,int> > pq;
	
	pq.push( make_pair(0,K));
	dist[K]=0;
	
	
	while(!pq.empty()){
		
		int curDist = -pq.top().first;
		int curVertex = pq.top().second;
		pq.pop();
		if(dist[curVertex] < curDist) continue;
		
		for(int i=0; i<graph[curVertex].size(); i++){
			int nextVertex = graph[curVertex][i].second;
			int nextDistance = graph[curVertex][i].first + curDist;
			
			if( dist[nextVertex] > nextDistance){
				dist[nextVertex] = nextDistance;
				pq.push( make_pair(-nextDistance,nextVertex));
			}
		}
	}
	
	for(int i=1; i<=V; i++){
		if(dist[i]==INT_MAX) cout << "INF\n";
		else cout << dist[i] << '\n';
	}
	return 0;
}
