// Problem title  :   Add matrix(행렬 덧셈)
// Problem Number :   2738
// Problem Tier   :   Bronze 3
// Date           :   2025/04/04, 22:00
// URL            :   https://www.acmicpc.net/problem/2738

// 문제
// N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

// 출력
// 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

// 예제 입력         예제 출력 
// 3 3              4 4 4
// 1 1 1            6 6 6
// 2 2 2            5 6 100
// 0 1 0
// 3 3 3
// 4 4 4
// 5 5 100



/// C++ Version


#include<iostream>
#include<vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int col = 0, row = 0;
    cin >> col >> row; 
    vector<int> matrix_A(col * row);

    for(int i = 0; i < col * row; i++) cin >> matrix_A[i];
    for(int i = 0; i < col * row; i++)
    {
        int matrix_B_input = 0;
        cin >> matrix_B_input;
        matrix_A[i] += matrix_B_input;
    } 

    for(int i = 0; i < col * row; i++)
    {
        cout << matrix_A[i];
        if(i % row == 0) cout << '\n'; else cout << ' '; 
    }
    return 0;
}