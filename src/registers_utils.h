#pragma once
#ifndef __UTILS_H__
#define __UTILS_H__

#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stdio.h>

#define PAGE_SIZE    4096

unsigned char *mmap_page(unsigned int page);

void hex_print(const unsigned char* s, int size, FILE *fp);

void bit_print(size_t const size, void const * const ptr);

unsigned int atou(char* s);

unsigned int atox(char* s);



#endif
