
#include<vector>
#include<list>
#include<stack>
#include<queue>



#include<iostream>

using namespace std;
int var=10;
/*int * ptr(int var){

return &var;
}*/
int &ptr2(){
 return var;
}
bool est_paire(int n){
    return !(n%2);
}
void display(vector<int>vect)
{
for (int elt:vect)
    cout<<elt<<'\t';
cout<<endl;

}

void display(list<int>vect)
{
for (int elt:vect)
    cout<<elt<<'\t';
cout<<endl;

}

int main()
{
    cout<<" before var: "<<var<<endl;
    ptr2()=5;
    cout<<" after var: "<<var<<endl;
    vector<int> vect(5);
    display(vect);
    vect.back()=25;
    vect.front()=99;
    display(vect);

    list<int> li={1,6,3,9,11,18,5};
    display(li);
    li.remove_if(est_paire);
        display(li);
        li.sort(greater<int>());
                display(li);


        list<int> li2={-1,-6,-3,-9,-11,-18,-5};
         li2.sort();
        auto it=li.begin();
        it++;
        li.splice(it,li2,li2.begin());
        display(li);
        stack<int, deque<int>> g;
        g.pop();
        g.push(5);






    return 0;
}