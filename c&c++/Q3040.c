#include<stdio.h>

void printOriginal(int* numbers, int fake_a, int fake_b)
{
    int i;
    for(i = 0; i < 9; i++)
    {
        if(i!=fake_a && i!=fake_b)
            printf("%d\n",*(numbers+i));
    }
}

void FakeFinder(int* numbers, int sum)
{
    int i,j;
    int len = sizeof(numbers) / sizeof(int);
    int diff = sum-100;
    for(i = 0; i < 8; i++)
    {
        if(*(numbers + i) > diff)
            continue;
        else
        {
            for(j = i + 1; j < 9;j++)
            {
                if((*(numbers + i) + *(numbers + j)) == diff )
                {
                    printOriginal(numbers, i, j);
                    return;
                }

            }
        }
    }
}

int main()
{
    int i;
    int sum=0;
    int numbers[9];
    for(i = 0; i < 9;i++)
    {
        scanf("%d", numbers+i);
        sum += *(numbers+i);
    }
    FakeFinder(numbers, sum);

    return 0;
}
