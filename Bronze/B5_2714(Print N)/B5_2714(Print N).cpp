// Problem title  :   Print N
// Problem Number :   2714
// Problem Tier   :   Bronze 5
// Date           :   2026/04/08, 21:22
// URL            :   https://www.acmicpc.net/problem/2714

// 문제
// 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

// 출력
// 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
// 예제 입력         예제 출력 
// 3                4 2 0 4
// 124              1 0 0 0	  	
// 25				7 1 1 4
// 194                



/// C++ Version
#include <iostream>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) {cout << i << "\n";}
    return 0;
}
