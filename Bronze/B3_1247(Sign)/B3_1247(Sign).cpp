// Problem title  :   Sign(부호)
// Problem Number :   1247
// Problem Tier   :   Bronze 3
// Date           :   2026/04/03, 23:16
// URL            :   https://www.acmicpc.net/problem/1247

// 문제
// N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.

// 입력
// 총 3개의 테스트 셋이 주어진다. 각 테스트 셋의 첫째 줄에는 N(1 ≤ N ≤ 100,000)이 주어지고, 둘째 줄부터 N개의 줄에 걸쳐 각 정수가 주어진다. 주어지는 정수의 절댓값은 9223372036854775807보다 작거나 같다.

// 출력
// 총 3개의 줄에 걸쳐 각 테스트 셋에 대해 N개의 정수들의 합 S의 부호를 출력한다. S=0이면 "0"을, S>0이면 "+"를, S<0이면 "-"를 출력하면 된다.

// 예제 입력                예제 출력
// 3                       0
// 0                       -
// 0                       +
// 0
// 10
// 1
// 2
// 4
// 8
// 16
// 32
// 64
// 128
// 256
// -512
// 6
// 9223372036854775807
// 9223372036854775806
// 9223372036854775805
// -9223372036854775807
// -9223372036854775806
// -9223372036854775804

/// C++ Version
#include<iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    for (int t = 0; t < 3; t++) 
    {
        int N;
        cin >> N;

        long long sum = 0;
        long long overflow = 0; 

        for (int i = 0; i < N; i++) 
        {
            long long val;
            cin >> val;

            long long prev_sum = sum;
            sum += val;

            if (val > 0 && prev_sum > 0 && sum <= 0) {overflow++;} 
            else if (val < 0 && prev_sum < 0 && sum >= 0) {overflow--;}
        }

        if (overflow > 0) {cout << "+" << "\n";} 
        else if (overflow < 0) {cout << "-" << "\n";}
        else 
        {
            if (sum > 0) {cout << "+" << "\n";}
            else if (sum < 0) {cout << "-" << "\n";}
            else {cout << "0" << "\n";}
        }
    }
}
