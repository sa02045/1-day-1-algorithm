#include <string>
#include <vector>

using namespace std;

int fibonacci[100001];

int solution(int n) {
    for(int i=0; i<=n; i++){
        if(i<=1) fibonacci[i] = i;
        else fibonacci[i] = (fibonacci[i-2] + fibonacci[i-1]) % 1234567;
    }
    
    return fibonacci[n];
}
