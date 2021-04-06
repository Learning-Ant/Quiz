#include <stdio.h>

// 1116kb	0ms

int main(void)
{
    int count, temp, i, j;
    scanf("%d", &count);
    int arr[count];
    for(i = 0; i<count; i++)
    {
        scanf("%d", arr+i);
    }

    for(i = 0; i<count; i++)
    {
        for(j = 0; j<count-1; j++)
        {
            if(arr[j]>arr[j+1])
            {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    for(i = 0; i<count; i++)
        printf("%d\n", arr[i]);

    return 0;
}
