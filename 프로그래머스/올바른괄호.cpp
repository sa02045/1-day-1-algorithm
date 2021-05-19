#include<string>
#include <iostream>
#include <stack>
using namespace std;

bool solution(string s)
{
    stack<int> st;
    for(int i=0; i<s.size(); i++){
        if(s[i]=='(' || st.empty()){
            st.push(s[i]);
        } else{
            if(st.top() !='(') return false;
            st.pop();
        }
    }
           
    return st.size()==0;
}
