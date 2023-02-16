#include<iostream>
#include<vector>
#include<stack>
using namespace std;
/*void display(vector<int> vect)
{
    auto it=vect.begin();
    for (it=vect.end();it!=vet.)
}*/

int main()
{
     vector<int> vect={1,2,5,6,9};
    vector<int>::iterator it_v;

    for (it_v=vect.begin();it_v!=vect.end();it_v++)
    cout<<*it_v<<'\t';
    cout<<'\n';
    *(it_v+1)=456;
    vector<int>::const_iterator it_w;
    //*(it_w+1)=45;



    return 0;
}