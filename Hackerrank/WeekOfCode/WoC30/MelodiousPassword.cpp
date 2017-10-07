#include <iostream>
#include <string>
#include <vector>
#include <ctime>
using namespace std;


vector<string> generateVowels(int n);
vector<string> generateConsonants(int n);

string Vowels[] = {"a","e","i","o","u"};
string Consonants[] = {"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"};
vector<string> generateVowels(int n){
    if(n==0){
        vector<string> v;
        v.push_back("");
        return v;
    }
    else{
        vector <string> res;
        for(int i=0;i<5;i++){
            vector<string> C = generateConsonants(n-1);
            for(int j=0; j<C.size(); j++){
                res.push_back(Vowels[i] + C[j]);
            }
        }
        return res;
    }
}
vector<string> generateConsonants(int n){
    if(n==0){
        vector<string> v;
        v.push_back("");
        return v;
    }
    else{
        vector <string> res;
        for(int i=0;i<20;i++){
            vector<string> C = generateVowels(n-1);
            for(int j=0; j<C.size(); j++){
                res.push_back(Consonants[i] + C[j]);
            }
        }
        return res;
    }
}

int main(){
    time_t now = time(0);
    int n;
    cin>>n;
    vector<string> c = generateVowels(n);
    for(int i=0; i<c.size() ; i++){
        cout<<c[i]<<endl;
    }
    c = generateConsonants(n);
    for(int i=0; i<c.size() ; i++){
        cout<<c[i]<<endl;
    }
    cout<<time(0)-now<<endl;
}