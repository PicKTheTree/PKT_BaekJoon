// Problem title  :   light blub
// Problem Number :   21918
// Problem Tier   :   Bronze 2
// Date           :   2026/03/26, 10:57
// URL            :   https://www.acmicpc.net/problem/21918

// 문제
// 'visual code에서 지원되지 않는 형식이 많은 관계로, 사이트 참조'

// 입력


// 출력


// 예제 입력         예제 출력 
// 8 3              0 0 1 0 0 0 0 0
// 0 0 0 0 0 0 0 0                 
// 1 2 1                
// 1 4 1               
// 2 2 4



/// C++ Version


#include<iostream>
#include<vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    //     N           M 
    int blubCount, orderCount;
    cin >> blubCount >> orderCount;

    // 전구의 상태를 저장하는 vector, 전구의 현재 상태(s)를 입력받을 변수 blubStautsInput 선언
    vector<int> blubStautsVector; 
    int blubStautsInput;

    for (int i = 1; i <= blubCount; i++) 
    {
         cin >> blubStautsInput; 
         blubStautsVector.push_back(blubStautsInput);
    }

    // M(orderCount)만큼 명령어 입력
    int orderValueA, orderValueL, orderValueR;
    while (orderCount--)
    {
        cin >> orderValueA;

        switch (orderValueA)
        {
            case 1:

                cin >> orderValueL >> orderValueR;
                blubStautsVector[orderValueL - 1] = orderValueR;
                break;

            case 2:
            
                cin >> orderValueL >> orderValueR;
                
                for (int i = orderValueL - 1; i < orderValueR; i++)
                {
                    if (blubStautsVector[i] == 0) {blubStautsVector[i] = 1;}
                    else {blubStautsVector[i] = 0;}
                }
                break;
            
            case 3:

                cin >> orderValueL >> orderValueR;
                for (int i = orderValueL - 1; i < orderValueR; i++) {blubStautsVector[i] = 0;}
                break;

            case 4:

                cin >> orderValueL >> orderValueR;
                for (int i = orderValueL - 1; i < orderValueR; i++) {blubStautsVector[i] = 1;}
                break;

            default:
                cout << "Unknown\n";
                break;
        }
    }
    
    for (int i = 0; i < blubCount; i++) {cout << blubStautsVector[i] << " ";}
}