// Problem title  :   Min, Max
// Problem Number :   20053
// Problem Tier   :   Bronze 3
// Date           :   2026/03/27, 14:18
// URL            :   https://www.acmicpc.net/problem/20053

// 문제
// N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 두 줄로 이루어져 있다.
// 각 테스트 케이스의 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
// 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

// 출력
// 각 테스트 케이스마다 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 한 줄에 하나씩 차례대로 출력한다.

// 예제 입력         예제 출력 
// 3        
// 5                20 28
// 20 28 22 25 21   17 30
// 5                7  35
// 30 21 17 25 29
// 5 
// 20 10 35 30 7


/// C++ Version


#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int testcaseCount;
    cin >> testcaseCount;

    while(testcaseCount--)
    {
        int numCount, numInput;
        

        cin >> numCount;
        vector<int> num(numCount); 
        
        for(int i = 0; i < numCount; i++)
        {
            cin >> numInput;
            num[i] = numInput; 
        }

        cout << *min_element(num.begin(), num.end()) << " " << *max_element(num.begin(), num.end()) << "\n";
    }
    
    return 0;
}