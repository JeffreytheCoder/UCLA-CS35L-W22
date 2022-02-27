#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <immintrin.h>
#include <unistd.h>
#include "./options.h"

int checkArgs(int argCount, char **args, struct options *options, long long *byteCount) 
{
  // possible options input: 
  // ./randall -i {source} {byteCount} 
  // ./randall -o {byteSize} {byteCount}
  // ./randall -i {source} -o {byteSize} {byteCount}
  // ./randall -o {byteSize} -i {source} {byteCount}

  int opt;
  options->byteSize = -1;
  options->input = "none";

  int err = 0;
  while ((opt = getopt(argCount, args, ":i:o:")) != -1) 
  {
    switch (opt) 
    {
      case 'i': 
        if (argCount != 4 && argCount != 6)
        {
          err = 1;
          break;
        }

        if (strcmp("rdrand", optarg) == 0)
        {
          options->input = "rdrand";
        }
        else if (strcmp("mrand48_r", optarg) == 0)
        {
          options->input = "mrand48_r";
        }
        else if (optarg[0] == '/')  // file input
        {
          options->input = "/f";
          options->source = optarg;
        }
        else
        {
          err = 1;
        }
        break;

      case 'o':
        if (argCount != 4 && argCount != 6)
        {
          err = 2;
          break;
        }

        if (strcmp("stdio", optarg) != 0) {
          options->byteSize = atoi(optarg);

          if (atoi(optarg) <= 0) {
            //	fprintf(stderr, "Must enter a positive integer\n");
            err = 3;
          break;
        }
      }
        break;

      case ':':
        fprintf(stderr, "Option -%c requires an operand\n", optopt);

        if (optopt == 'i')
          err = 1;
        else
          err = 2;
        break;
      
      case '?':
        fprintf(stderr, "Unrecognized option: '-%c'\n", optopt);
        break;

      default:
        break;
    }
  }

  if (optind >= argCount) // if no byteCount or format of options is wrong
  {
    return err;
  }

  *byteCount = atol(args[optind]);
  if (*byteCount < 0) // byteCount must best nonnegative
  {
    err = 3;
  }

  return err;
}
