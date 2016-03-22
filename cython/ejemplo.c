/* ejemplo.c */

#include "ejemplo.h"

int fact(int n) {
    if (n < 0){ /* Devolvería un error. Pero hacer esto es mas simple */
        return 0;
    }
    if (n == 0) {
        return 1;
    }
    else {
        /* Podríamos probar aquí si hay desbordamiento pero esto es solo un ejemplo*/
        return n * fact(n-1);
    }
}
