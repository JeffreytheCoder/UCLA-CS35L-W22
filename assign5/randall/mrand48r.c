#include <cpuid.h>
#include <immintrin.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "./mrand48r.h"

struct drand48_data buffer = {0};
long int x, y;

void
mrand48r_init (void)
{
  srand48_r(time(NULL), &buffer);
}

unsigned long long
mrand48r (void)
{
  mrand48_r(&buffer, &x);
  mrand48_r(&buffer, &y);

  // Combine two 32-bit integers into one 64-bit integer
  unsigned long long int result = (
    ((unsigned long long) x) << 32) 
    | ((unsigned long long) y & 0x00000000FFFFFFFF
  );
  return result;
}

void
mrand48r_fini (void)
{
}
