// Problem title  :   Odd number
// Problem Number :   2576
// Problem Tier   :   Bronze 3
// Date           :   2026/04/07, 21:54
// URL            :   https://www.acmicpc.net/problem/2576

// 문제
// 7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.
// 예를 들어, 7개의 자연수 12, 77, 38, 41, 53, 92, 85가 주어지면 이들 중 홀수는 77, 41, 53, 85이므로 그 합은
// 77 + 41 + 53 + 85 = 256이 되고,
// 41 < 53 < 77 < 85
// 이므로 홀수들 중 최솟값은 41이 된다.

// 입력
// 입력의 첫째 줄부터 일곱 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100보다 작다.

// 출력
// 홀수가 존재하지 않는 경우에는 첫째 줄에 -1을 출력한다. 홀수가 존재하는 경우 첫째 줄에 홀수들의 합을 출력하고, 둘째 줄에 홀수들 중 최솟값을 출력한다.

// 예제 입력                예제 출력
// 12                      256
// 77                      41
// 38
// 41
// 53
// 92
// 85

/// C++ Version
#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    vector<int> numbers(7);
    int minOddNumber = 101;
    int sumOddNumber = 0;
    
    
    for(int i =0; i < numbers.size(); i++)
    {
        cin >> numbers[i];

        if (numbers[i] % 2 == 1)
        {
            sumOddNumber += numbers[i];

            if (numbers[i] < minOddNumber) {minOddNumber = numbers[i];}
        }
    }

    if (minOddNumber == 101){cout << -1;}
    else {cout << sumOddNumber << "\n" << minOddNumber;} 
}
