
#include <stdio.h>
#include <conio.h>
#include <iostream.h>
int main(void)
{
clrscr();
int jawab=0;
cout<<"hitung 5 x 5 = "<<endl;
do
{
cout<<"enter jawaban anda: ";
cin>>jawab;
} while(jawab != 25) ;
printf("benar, 5 x 5 = %d \n", jawab);
printf("Tekan Enter Untuk Melanjutkan!!!");
getch();
}