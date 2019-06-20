#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vuln(char * s){
  char buf[100];

  strcpy(buf,s);

  printf("Buf: %s\n", buf);
}

void main(int argc, char * argv[]){

    vuln(argv[1]);
}
