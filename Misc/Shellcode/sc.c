/* This code is intented to be an example on how a shellcode can be embedded in a binary file 
 * Author: Marcus Botacin, 2017
 * This code is part of the "Anti.Analysis research project"
 */

#include <stdio.h>
#include <string.h>
 
int main(){
    /* Your own shellcode, not my ones */
	unsigned char shellcode[]="PUT.YOUR.SHELLCODE.HERE";
    /* just a verification message */
	fprintf(stdout,"Length: %d\n\n",strlen(shellcode));
    /* function pointer : run */
	(*(void(*)()) shellcode)();
    /* no return, may never return */
}
