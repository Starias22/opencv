#include<iostream>
#include<vector>
#include<stack>
using namespace std;
bool empty(stack<int,vector<int>> stack){
    return stack.empty();
}

void push (stack<int,vector<int>> stack,int elt){
    stack.push(elt);
}
void pop (stack<int,vector<int>> stack){
    stack.pop();
}
int top (stack<int,vector<int>> stack){
    return stack.top();
}
void print_top (stack<int,vector<int>> stack){
    cout<<top(stack);
}
bool search(stack<int,vector<int>> stack,int elt){


}


int main()
{
    stack<int,vector<int>> stack;

    return 0;
}