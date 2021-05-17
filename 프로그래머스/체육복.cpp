#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    
    for(int i=0; i<reserve.size(); i++){
        for(int j=0; j<lost.size(); j++){
            if(reserve[i]== lost[j]){
                lost[j] = -2;
                reserve[i] = -4;
            }
        }
    }
    
    for(int i=0; i<reserve.size(); i++){
        for(int j=0; j<lost.size(); j++){
            if(reserve[i]-1 == lost[j] || reserve[i]+1 ==lost[j]){
                lost[j] = -2;
                break;
            }
        }
    }
    
    int lostSize =0;
    for(int i=0; i<lost.size(); i++){
        if(lost[i]!=-2) lostSize++;
    }
    
    return n-lostSize;
}
