// Problem title  :   Sort Number(수 정렬하기)
// Problem Number :   2750
// Problem Tier   :   Bronze 2
// Date           :   2023/02/26, 15:22
// URL            :   https://www.acmicpc.net/problem/2750

// 문제
// N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

// 출력
// 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

// 예제 입력         예제 출력 
// 5
// 5                 1 
// 2                 2
// 3                 3
// 4                 4
// 1                 5




/// C++ Version


#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int array_len; cin >> array_len;
    vector<int> array; int number_inputed=0;

    for ( int i = 0; i < array_len; i++ ) { cin >> number_inputed; array.push_back( number_inputed ); }
    sort(array.begin(), array.end());
    for ( int i = 0; i < array_len; i++ ) { cout << array[i ]<< endl; }
}