#include<iostream>
#include<queue>
#define INF 987654321

using namespace std;

vector<int> dijk(int start, vector< pair<int,int> > adj[]){
	vector<int> dist(1001,INF);
	dist[start]=0;
	priority_queue< pair<int,int> > pq;
	pq.push( make_pair(0,start));
	
	
	while(!pq.empty()){
		int curVer = pq.top().second;
		int curDist = -pq.top().first;
		pq.pop();
		
		if(dist[curVer] < curDist) continue;
		
		for(int i=0; i<adj[curVer].size(); i++){
			int nextVer = adj[curVer][i].second;
			int nextDist = adj[curVer][i].first + curDist;
			
			if(dist[nextVer] > nextDist){
				dist[nextVer] = nextDist;
				pq.push( make_pair(-nextDist,nextVer));
			}
		}
	}
	
	return dist;
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	
	int C;
	cin >> C;
	
	while(C--){
		int V,E,n,m;
		cin >> V >> E >> n >> m;
		
		vector< pair<int,int> > adj[1001];

		while(E--){
			int a,b,t;
			cin >> a >> b >> t;
			adj[a].push_back( make_pair(t,b));
			adj[b].push_back( make_pair(t,a));
		}
		
		vector<int> firePlace;
		while(n--){
			int fireNum;
			cin >> fireNum;
			firePlace.push_back(fireNum);
		}
		
		while(m--){
			int stationNum;
			cin >> stationNum;
			adj[0].push_back( make_pair(0,stationNum));
		}

		vector<int> result = dijk(0,adj);
		
		int sum=0;
		for(int i=0; i<firePlace.size(); i++){
			sum += result[firePlace[i]]; 
		}

		cout << sum << '\n';
	}
	return 0;
} 
