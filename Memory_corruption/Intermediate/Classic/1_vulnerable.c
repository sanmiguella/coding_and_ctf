#include <unistd.h>
#include <stdio.h>

void vuln() {
    char buffer[16];
   
    /*
	0 - stdin 
	1 - stdout
	2 - stderr
    */ 
    read(0, buffer, 200);
    puts(buffer);
}

int main() {
    vuln();
}
