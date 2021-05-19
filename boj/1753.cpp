#include<bits/stdc++.h>
using namespace std;

int V,E;
int K;

struct minheap{
	bool operator() (pair<int,int> a , pair<int,int> b){
		return a.second> b.second;
	}
};

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> V >> E;
	cin >> K;
	int distance[20001];
	vector< pair<int,int> > graph[20001];
	
	while(E--){
		int u,v,w;
		cin >> u >> v >> w;	
		graph[u].push_back( make_pair(v,w) );
	}
	
	for (int i = 1; i <= V; i++) {
		distance[i] = 987654321;
	}
	
	distance[K]=0;
	
	priority_queue< pair<int,int>, vector< pair<int,int> > , minheap > pq;
	
	pq.push( make_pair(K,0));
	
	while(!pq.empty()){
		int vertex = pq.top().first;
		int weight = pq.top().second;
		pq.pop();

		for(int i=0; i < graph[vertex].size(); i++){
			int nextV = graph[vertex][i].first;
			int nextDistance = graph[vertex][i].second + distance[vertex];
			
			if(distance[vertex] > nextDistance){
				distance[vertex] =  nextDistance;
				pq.push(make_pair(nextV,nextDistance));
			}
		}
		
	}
		for(int i=1; i<=V; i++){
			if(distance[i]==987654321) cout << "INF" << '\n';
			else cout << distance[i] << '\n';
		}
	
}
