#include <stdio.h>
#include <string.h>
void test(){
    int z;
    char str1[]={"a","b","h","i","j","k","l"};
    char str2[]={"abc","def","ghi","jkl","mno"};
    for(int i=0;i<=5;i++)
    z=strcmp(str1[i],str2[i]);
    printf("%d",z);

}

int main() {
test();
char str[4][10],temp[10];
int i,j;
printf("Enter strings one by one : \n");
for(i=0;i<5;i++)
    scanf("%s",str[i]);

for(i=0;i<5;i++)
    for(j=i+1;j<5;j++)
        if(strcmp(str[i],str[j])<0){
        // if(strcmp(str[i],str[j])>0){
            strcpy(temp,str[i]);
            strcpy(str[i],str[j]);
            strcpy(str[j],temp);
        }
printf("\nSorted List : ");
for(i=0;i<5;i++)
    printf("\n%s",str[i]);
printf("\n\n");
return 0;
}
