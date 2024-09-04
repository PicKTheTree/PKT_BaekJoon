// Problem title  :   the sum of the integer N(정수 N개의 합)
// Problem Number :   15596
// Problem Tier   :   Bronze 2
// Date           :   2024/09/04, 16:00 
// URL            :   https://www.acmicpc.net/problem/15596


// 문제
// 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오. 작성해야 하는 함수는 다음과 같다.

// a: 합을 구해야 하는 정수 n개가 저장되어 있는 배열 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
// 리턴값: a에 포함되어 있는 정수 n개의 합.

#include <vector>
#include <iostream>

long long sum(std::vector<int> &a) {
	long long ans = 0;
    for(int i = 0; i < a.size(); i++){
        ans += a[i];
    }
	return ans;
}
