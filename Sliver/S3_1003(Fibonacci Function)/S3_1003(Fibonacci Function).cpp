// Problem title  :   Fibonacci Function(피보나치 함수)
// Problem Number :   1003
// Problem Tier   :   Sliver 3
// Date           :   2023/02/28, 16:07
// URL            :   https://www.acmicpc.net/problem/1003

// 문제
// 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

// int fibonacci(int n) {
//     if (n == 0) { printf("0"); return 0; } 
//     else if (n == 1)  { printf("1"); return 1; } 
//     else { return fibonacci(n‐1) + fibonacci(n‐2); }
// }
// fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

// fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
// fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
// 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
// fibonacci(0)은 0을 출력하고, 0을 리턴한다.
// fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
// 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
// fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
// 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
// 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

// 출력
// 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

// 예제 입력     예제 출력
// 3              
// 0             1 0
// 1             0 1 
// 3             1 2
// 6             5 8


///// C++ Version

#include<iostream>
#include<vector>
using namespace std;



int main() {

    //Clear_buffer_code
    ios::sync_with_stdio(false); 
    cin.tie(0); 
    cout.tie(0);   
    
    //__init__
    int Time_case;
    int Number_inputed;  
    cin >> Time_case;
    vector<int> Array = { 0, 1, 1 };

    // Fibonacci(N) == Fibonacci(N-2) + Fibonacci(N-1) 
    for ( int i = 3; i < 41; i++ )  {

        Array.push_back( Array[ i - 2 ] + Array[ i - 1 ] );  

    }


    // Array[ Number_inputed - 1 ]  ==  Count_zero  (   == Fibonacci( Number_inputed - 1 ) )
    // Array[ Number_inputed     ]  ==  Count_one   (   == Fibonacci( Number_inputed     ) )    
    for ( int i=0; i<Time_case; i++ ) {

        cin >> Number_inputed;

        if ( Number_inputed == 0 )  cout << 1 << " " << 0 << "\n";

        else                        cout << Array[Number_inputed-1] << " " << Array[Number_inputed] << "\n"; 
        
    } 
 



}




///// C++ Fail Version (Time Out)
// #include<iostream>
// using namespace std;

// int Count_zero=0; int Count_one=0;

// int fibonacci(int n) {
//     if (n == 0) { Count_zero++; return 0; } 
//     else if (n == 1)  { Count_one++; return 1; } 
//     else { return fibonacci(n-1) + fibonacci(n-2); }
// }

// int main() {
//     int Time_case; int Number_inputed;
//     cin >> Time_case;


//     for (int i=0; i<Time_case; i++) {
        
//         cin >> Number_inputed;
//         fibonacci(Number_inputed);
//         cout << Count_zero << " " << Count_one << endl;
//         Count_one = 0; Count_zero = 0;
        
//     }

// }