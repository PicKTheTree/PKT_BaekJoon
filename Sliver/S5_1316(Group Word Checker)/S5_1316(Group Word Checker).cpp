// Problem title  :   Group Word Checker(그룹 단어 체커)
// Problem Number :   1316
// Problem Tier   :   Sliver 5
// Date           :   2023/03/02, 12:15
// URL            :   https://www.acmicpc.net/problem/1316


// 문제
// 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
// 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
// aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
// 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다.
// 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

// 출력
// 첫째 줄에 그룹 단어의 개수를 출력한다.

// 예제 입력 1     예제 출력 1 
// 3
// happy
// new
// year           3

// 예제 입력 2     예제 출력 2
// 4
// aba
// abab
// abcabc
// a              1



///// C++ Version
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main() {

    // init variable
    string Word_inputed;
    vector<char> Alphabet_array;
    int Time_case, Cnt_group_word;
    
    cin >> Time_case;
    Cnt_group_word = Time_case;

    for ( int Case = 0; Case < Time_case; Case++ )   {
    

        cin >> Word_inputed;
        Alphabet_array.push_back( Word_inputed[0] );


        for( int index = 0; index < Word_inputed.length(); index++ )    {
            
            // is Alphabet continuous? 
            if( Word_inputed[ index ] != Alphabet_array.back())   {
                
                // Was Alphabet appeared? 
                auto Group_word_checker=  find( Alphabet_array.begin(), Alphabet_array.end(), Word_inputed[ index ] ); 

                if ( Group_word_checker != Alphabet_array.end() )   { Cnt_group_word--; break; }
                    //Yes   >>  Non Group_Word
                    //No    >>  Continue 
            }

            Alphabet_array.push_back( Word_inputed[ index ] );
        }

        //Clear Array 
        Alphabet_array.clear();
    
    }

    //print Count of Group word
    cout << Cnt_group_word;
}
 

///// C++ Short Version
// #include<iostream>
// #include<string>
// #include<vector>
// #include<algorithm>
// using namespace std;
//
// int main() {
//     string V; vector<char> A; int T, C;
//     cin>>T;C=T;
//     for (int t=0;t<T;t++){
//         cin>>V;
//         A.push_back(V[0]);
//         for(int i=0;i<V.length();i++){ 
//             if(V[i]!=A.back()){auto G= find(A.begin(),A.end(),V[i]); if (G!=A.end()) {C--; break;}}
//             A.push_back(V[i]);
//         }
//         A.clear();
//     }
//     cout<<C;
// }