// quicksort.h
//
// Function prototype for quicksort. I'm using this because I couldn't get the
// stdlib's qsort to work - something to do with wiring/processing overwriting
// the abs function with a marco. In anycase it is a known bug and should be
// fixed in the near future. In the meantime I am using a version from the gnu
// c library. 
//
// Will Dickson, IO Rodeo Inc.
//
#ifndef _QSORT_H_
#define _QSORT_H_

#include <limits.h>
#include <string.h>

typedef int (*__compar_fn_t) (const void *, const void *);

void quicksort(void *pbase, size_t total_elems, size_t size, __compar_fn_t  cmp);

#endif
