#include<stdio.h>
#include<conio.h>
#include<math.h>
int main(){
    int a,b,c;
    float d;
    printf("Enter the value of a,b,c");
    scanf("%d%d%d",&a,&b,&c);
    d = (a+b+c)/3;
    printf("The average of %d,%d,%d is %f",a,b,c,d);
    getch();
    return 0;
}