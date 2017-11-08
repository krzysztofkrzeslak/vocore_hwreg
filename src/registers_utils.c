#include "registers_utils.h"

// get one page, system memory map by page number.
unsigned char *mmap_page(unsigned int page)
{
    int fd = -1;
    unsigned char *mem = NULL;
    fd = open("/dev/mem", O_RDWR);
    if(fd < 0)
        return NULL;

    mem = (unsigned char *)mmap(0, PAGE_SIZE,
        PROT_READ | PROT_WRITE, MAP_SHARED, fd, page * PAGE_SIZE);
    close(fd);

    return mem;
}


void bit_print(size_t const size, void const * const ptr)
{

    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;
    int num=(size*8)-1;



    for (i=size-1;i>=0;i--)
    {
        for (j=7;j>=0;j--)
        {
            byte = (b[i] >> j) & 1;
            printf("%d : %d   ",num, byte);
            num--;

            //break;
        }
        puts("\n");
    }

}

   