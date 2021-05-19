#include <string>
#include <vector>
#include <stack>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;

    int leftDay;
    int maxDay=0;
    
    for(int i=0; i<progresses.size(); i++){
       // leftDay =  ((100-progresses[i]) / speeds[i] );
        // if( (100-progresses[i]) % speeds[i] !=0) leftDay+=1;
        
        leftDay = (99-progresses[i]) / speeds[i] +1;
        
        if(answer.empty() || maxDay < leftDay){
        	answer.push_back(1);
		} else {
			++answer.back();
		}
		
		if(maxDay < leftDay){
			maxDay = leftDay;
		}
    }
    
    return answer;
}
