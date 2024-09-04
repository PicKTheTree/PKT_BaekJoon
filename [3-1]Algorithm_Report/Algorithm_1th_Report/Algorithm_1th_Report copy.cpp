#include <Stdio.h>
#include <stdlib.h>


#define max_n 10
#define max_value 100

int find_arr(int peb[4],int max){
    for(int i=0; i<4;i++){
        if(peb[i]== max){
            return i;

        }
    }

}


int find_max(int peb[4], int cse) {
    int result = 0;
    switch (cse) {
    case 0:
        result = peb[1] > peb[2] ? peb[1] : peb[2];
        break;
    case 1:
        result = peb[0] > peb[2] ? peb[0] : peb[2];
        result = result > peb[3] ? result : peb[3];
        break;
    case 2:
        result = peb[0] > peb[1] ? peb[0] : peb[1];
        break;
    case 3:
        result = peb[1];
        break;
    default:
        break;
    }
    return result;
}

int main(){ 

    int n;
    printf("열크기 n을 입력하시오 :");
    scanf("%d", &n);//열크기 입력받기 

    if (n > max_n) {
     printf("n은 %d보다 작거나 같아야 합니다.\n", max_n);
        return 0;
    }

    
    int ** arr = (int**)malloc(sizeof(int*)*3); //사용자 테이블 입력 
    
    for(int i=0; i<3;i++){
        arr[i] = (int*)malloc(sizeof(int) *n); 
    
    }
    


    int** pebble = (int**) malloc(sizeof(int*)*n);// 돌의합 출력하는 테이블 nx4

    for(int i=0; i<n; i++){
        pebble[i] =(int*) malloc (sizeof(int) * 4);
    }



    
    for(int i=0; i<3; i++){ 
        for(int j=0; j<n; j++){

            printf("테이블 [%d][%d] 입력:", i,j);
            scanf("%d", &arr[i][j]);
            if(arr[i][j] <-100 || arr[i][j] > 100){
                printf("정수 r에 들어가는 값은 -100과 100사이의 범위에 있어야합니다 .");
                return 0;
            }
            
        }
    }


    printf("입력한 테이블:\n");
    for(int i=0; i<3; i++){ 
        for(int j=0; j<n; j++){
            printf("[%d]", arr[i][j]);
        }
        printf("\n");
    }


   for(int i=0; i<4; i++){ //1,3,5,6 을챠ㅐ움 
            if(i==3){
                pebble[0][i]=arr[0][0]+arr[2][0];
            }
            else{
                pebble[0][i]=arr[i][0];
            }
        
    }

for (int i = 1; i < n; i++) {
        for (int j = 0; j < 4; j++) {
            int plus = 0;
            if (j < 3)
                plus = arr[j][i];
            else
                plus = arr[0][i] + arr[2][i];
            pebble[i][j] = plus + find_max(pebble[i - 1], j);

        }
    }


        printf("pebble테이블:\n");
    for(int i=0; i<n; i++){ 
        for(int j=0; j<4; j++){
            printf("[%d]", pebble[i][j]);
        }
        printf("\n");
    }


    int max= 0;
    int maxindex =0 ;

    for(int j=0; j<4; j++){
        if(pebble[n-1][j] > max){
                max= pebble[n-1][j];
                maxindex=j;
            }
        }
   printf("최대값:%d\n", max);



    printf("최대가 되는 좌표값(x,y):");
    int index_max = max; //max 를 한번더 돌리지 않기 위해 index_max를 max로 초기화 
  for (int k = n - 1; k >= 0; k--) {// k는 현재행을 말하는것 
    int max_index = find_arr(pebble[k], index_max);
    if (max_index == 3) {
        
      printf("(%d,%d)", k + 1, 1);
      printf("(%d,%d)\n", k + 1, 3);
      index_max -= (arr[0][k] + arr[2][k]);
    } else {
      printf("(%d,%d)\n", k + 1, max_index + 1);
      index_max -= arr[max_index][k];
    }
  } 


}
        




        



