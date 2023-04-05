#include<vector>
#include<iostream>
#include<algorithm>
#include<random>
#include<numeric>

    using namespace std;


// 입력 실패(문자열 입력, 범위 오류 등)가 일어 났을 때,
// C++의 에러를 방지하기 위한 함수 
void Clear_Buffer()
{
    cin.clear();
    cin.ignore(256, '\n');  
    cout << "\n\n\n";
}


// 선택 정렬과 버블 정렬에 사용되는 함수이다.
// 해당 함수는 두 개의 인덱스를 넘겨주면, 서로의 값을 바꿔준다.
// 삽입 정렬의 경우, 
// 쉬프트 연산(밀어내기)를 통해 자리를 바꿀 수 있으므로, 
// 해당 함수를 사용하지 않는다. (사용할 수는 있지만, 비효율적이다.)
template <typename T>
void Swap(T &Num_a, T &Num_b)
{
    T Num_temp;

    Num_temp = Num_a; 
    Num_a = Num_b; 
    Num_b = Num_temp;
}

// 현재 배열을 출력하는 함수
void Print_vector( vector<int>& Array, int Array_len )
{
    for( int Print = 0; Print < Array_len; Print++) { cout << Array[Print] << "  ";}
    cout<<"\n\n";
}


// 본격적인 정렬을 하는 함수이다.
// 입력받은 정렬 방식에 따라, 정렬을 한다.
void Sorting( int Sort, vector<int> Array, int len)
{
    int Num_temp; 
    int Search_index, Array_len = len;

    // 비교를 위해, 정렬 하기 전의 배열 복사
    vector<int> Array_before_sort; 
    for( int copy = 0; copy < Array_len; copy++) { Array_before_sort.push_back(Array[copy]);}

    printf("정렬을 시작합니다.\n\n"); 
    
    // 선택 정렬 방식                              
    if ( Sort == 1 )
    {                   
        printf("정렬 방식: \n\n선택 정렬( Selection Sorting )\n");
        printf("1. 배열에서 가장 큰 값을 찾는다. \n");
        printf("2. 최댓값을 가장 뒤로 보낸다. \n");
        printf("3. 탐색 범위를 줄이고, 위 과정을 반복한다.\n\n\n");                                                                           
        for( int i = 0; i < Array_len; i++ )             
        {
            Num_temp = 0;                                        
                                                                
            for( int j = 1; j < Search_index; j++ )             
            { 
                if( Array[ Num_temp ] <= Array[ j ] ) Num_temp = j; 
            }

            Swap( Array[ Num_temp ], Array[ Search_index - 1 ] ); 
            Search_index--;                                     
        }
    }

    // 버블 정렬 방식
    else if ( Sort == 2 )
    {
        printf("정렬 방식: \n\n버블 정렬( Bubble Sorting )\n");
        printf("1. 배열의 1(n) 번째 값과 2(n+1) 번째 값을 비교한다. \n");
        printf("2. 배열의 1(n) 번째 값이 2(n+1) 번째 값보다 크면 교체하고. 작으면 바꾸지 않는다.\n");
        printf("3. 비교하는 인덱스를 1씩 증가한다.\n");
        printf("   이 때, n+1이 배열의 끝에 도달하면, 1의 과정으로 돌아온다. \n");
        printf("   또한, 1(n) 번째 값을 정렬 범위에서 제외시킨다.(배열의 2(n+1) 번째 부터 시적한다.) \n");
        printf("4. 위 과정을 반복한다.\n");
        for ( int i = 0; i < Array_len - 1; i++ )
        {
		    for ( int j = 0; j < Array_len - i - 1; j++ ) 
            {
			    if ( Array[j] > Array[j + 1]) { Swap( Array[j], Array[j+1]); }
            }
        }
    }

    // 삽입 정렬 방식
    else if ( Sort == 3 )
    {
        printf("정렬 방식: \n\n삽입 정렬( Insertion Sorting )\n");
        printf("1. 배열의 인덱스 'n'에 대하여, 올바른 위치를 찾는다.\n");    
        printf("2. 해당 위치와 뒤에 있는 값들을 쉬프트 연산으로 옮긴다.\n");
        printf("3. 1번 과정에서 찾은 올바른 위치에 배열의 n 번째의 값을 삽입한다.\n");
        printf("4. 위 과정을 반복한다.\n\n\n");
        for (int i = 1; i < Array_len; i++ )
        {
            int Num_temp = Array[ i ];
            int j = i - 1;
                while (j >= 0 && Array[ j ] > Num_temp ) 
                {
                    Array[j + 1] = Array[j];
                    j--;
                }
            Array[j + 1] = Num_temp;
        }
    }



    printf("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\n");
    printf("정렬이 끝났습니다.\n\n");
    printf("정렬 전:\n"); Print_vector( Array_before_sort, Array_len);
    printf("정렬 후:\n"); Print_vector( Array, Array_len);
}


int main(void)
{
    random_device Random_num;
    mt19937 gen(Random_num());
    vector<int> Array(64);
    int Sort_method = -1;

    printf("1~64까지의 숫자가 중복하지 않고 배열을 구성하였습니다. \n\n");
    iota(Array.begin(), Array.end(), 1);
    shuffle(Array.begin(), Array.end(), gen);

    printf("현재 배열 상태: ");
    Print_vector( Array, Array.size());

    while ( 1 )
    {
        printf("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n");
        printf("정렬 방식을 입력받습니다 \n\n");
        printf("1 : 선택 정렬       2 : 버블 정렬\n");
        printf("3 : 삽입 정렬       그 외: 중단\n");
        printf("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\n");
        cin >> Sort_method;

        // 예외 처리
        
        if      ( Sort_method == 1 ) { Sorting( Sort_method, Array, Array.size() ); }  //선택 정렬
        else if ( Sort_method == 2 ) { Sorting( Sort_method, Array, Array.size() ); }  //버블 정렬
        else if ( Sort_method == 3 ) { Sorting( Sort_method, Array, Array.size() ); }  //삽입 정렬
        else                         { Clear_Buffer(); break;                       }  //예외 처리             
    }
}
