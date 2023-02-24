// Problem title  :   Federation Favorites(약수들의 합)
// Problem Number :   9506
// Problem Tier   :   Bronze 1
// Date           :   2023/02/24, 20:11
// URL            :   https://www.acmicpc.net/problem/9506





// 문제
// 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다. 
// 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
// n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.


// 입력
// 입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100, 000)
// 입력의 마지막엔 -1이 주어진다.


// 출력
// 테스트케이스 마다 한줄에 하나씩 출력해야 한다.


// n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).
// 이때, 약수들은 오름차순으로 나열해야 한다.
// n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.



// 예제 입력 1      예제 출력 1 
// 6                6 = 1 + 2 + 3
// 12               12 is NOT perfect.
// 28               28 = 1 + 2 + 4 + 7 + 14
// -1






//// C++ Version

#include<stdio.h>
#include<iostream>
#include<vector>
using namespace std;

int main( void )
{
    int Number_inputed=0;
    int Number_sum=0; 

    
    while( 1 )
    {
        cin >> Number_inputed;
        if( Number_inputed == -1 ) break;
        Number_sum=0;
        vector<int> Number_Divisors;

        for(int i=1; i<=Number_inputed/2; i++)
        {
            if( Number_inputed % i == 0 )
            {
                Number_sum += i;
                Number_Divisors.push_back(i);

            }
        }
		
        if(Number_sum == Number_inputed)
        {
            cout << Number_inputed << " = ";

            for(int i=0; i<Number_Divisors.size(); i++)
            {
                cout << Number_Divisors[i];
                if(i == Number_Divisors.size()-1) break;
                cout << " + ";
            }
        }
        else
        {
			cout << Number_inputed << " is NOT perfect.";
		}
		cout << endl;
    }
    
    return 0;
}