// 이거는 2학년2학기때 했던 퀵 정렬 알고리즘 C언어로 구현한 예시

#include <stdio.h>
#include <stdlib.h>

void printQuickArray(int data[], int size)
{
    printf("퀵정렬 수행 >> ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", data[i]);
    }
    printf("\n");
}
void quickSortFirstIndexPivot(int data[], int start, int end)
{
    if (start > end)
        return;

    int pivot = start; // 피봇은 시작지점
    int i = start + 1;
    int j = end;
    int temp, count = 1;

    while (i <= j)
    {
        while (data[i] <= data[pivot]) // pivot보다 큰 값을 만날때 까지 오른쪽으로 이동
            i++;
        while (data[j] >= data[pivot] && j > start)
            j--;

        if (i > j)
        {
            temp = data[j];
            data[j] = data[pivot];
            data[pivot] = temp;
        }
        else
        {
            temp = data[j];
            data[j] = data[i];
            data[i] = temp;
        }
        printQuickArray(data, end + 1);
    }
    quickSortFirstIndexPivot(data, start, j - 1);
    quickSortFirstIndexPivot(data, j + 1, end);
}

int main(void)
{
    int *arr, arr_size;
    printf("배열의 크기 입력 : ");
    scanf("%d", &arr_size);

    if (arr_size < 0)
        return 1;

    arr = (int *)malloc(sizeof(int) * arr_size);

    printf("배열의 요소 입력 : ");
    for (int k = 0; k < arr_size; k++)
        scanf("%d", &arr[k]);
    if (!arr)
    {
        fprintf(stderr, "Memory allocate error :(\n");
        exit(1);
    }
    quickSortFirstIndexPivot(arr, 0, arr_size - 1);

    printf("퀵정렬 결과 : ");
    for (int z = 0; z < arr_size; z++)
        printf("%d ", arr[z]);

    free(arr);
}

// 아래 주석 처리된 부분은 이걸 GPT를 이용해서 자바로 변환했는데 맞는지는 모르겠음...

// import java.util.Scanner;

// public class QuickSort {

//     public static void printQuickArray(int[] data) {
//         System.out.print("퀵정렬 수행 >> ");
//         for (int i = 0; i < data.length; i++) {
//             System.out.print(data[i] + " ");
//         }
//         System.out.println();
//     }

//     public static void quickSortFirstIndexPivot(int[] data, int start, int end) {
//         if (start >= end)
//             return;

//         int pivot = start;
//         int i = start + 1;
//         int j = end;
//         int temp;

//         while (i <= j) {
//             while (i <= end && data[i] <= data[pivot])
//                 i++;
//             while (j > start && data[j] >= data[pivot])
//                 j--;

//             if (i > j) {
//                 temp = data[j];
//                 data[j] = data[pivot];
//                 data[pivot] = temp;
//             } else {
//                 temp = data[j];
//                 data[j] = data[i];
//                 data[i] = temp;
//             }
//             printQuickArray(data);
//         }
//         quickSortFirstIndexPivot(data, start, j - 1);
//         quickSortFirstIndexPivot(data, j + 1, end);
//     }

//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         System.out.print("배열의 크기 입력 : ");
//         int arrSize = scanner.nextInt();

//         if (arrSize < 0) {
//             System.out.println("잘못된 입력입니다.");
//             return;
//         }

//         int[] arr = new int[arrSize];

//         System.out.print("배열의 요소 입력 : ");
//         for (int k = 0; k < arrSize; k++)
//             arr[k] = scanner.nextInt();

//         quickSortFirstIndexPivot(arr, 0, arrSize - 1);

//         System.out.print("퀵정렬 결과 : ");
//         for (int z = 0; z < arrSize; z++)
//             System.out.print(arr[z] + " ");

//         scanner.close();
//     }
// }
