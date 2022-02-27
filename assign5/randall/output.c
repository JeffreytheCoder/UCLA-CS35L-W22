#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include "./output.h"

bool
writebytes (unsigned long long x, int byteCount)
{
  do
    {
      if (putchar (x) < 0)
        return false;
      x >>= CHAR_BIT;
      byteCount--;
    }
  while (0 < byteCount);

  return true;
}
