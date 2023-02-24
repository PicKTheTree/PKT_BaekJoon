// Problem title  :   Federation Favorites(약수들의 합)
// Problem Number :   9506
// Problem Tier   :   Bronze 1
// Date           :   2023/02/24, 20:11
// URL            :   https://www.acmicpc.net/problem/9506




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