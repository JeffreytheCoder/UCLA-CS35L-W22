#ifndef OPTIONS
#define OPTIONS

struct options {
  char* input;
  char* source;
  unsigned int byteSize;
};

int
checkArguments(int arg_c, char** arg_v, bool* val, long long* n_bytes, struct options* options);

#endif
