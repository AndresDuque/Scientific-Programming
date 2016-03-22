/* example.i */
%module ejemplo

%{
#define SWIG_FILE_WITH_INIT
#include "ejemplo.h"
%}

int fact(int n);
