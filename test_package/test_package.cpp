#include <cstdlib>
#include <iostream>

#ifdef __cplusplus
extern "C" {
#endif

#include <getopt.h>

#ifdef __cplusplus
}
#endif


int main(int argc, char * argv[])
{
    while (true) {
        int option_index = 0;
        int c = getopt(argc, argv, "v");
        if (c == -1) {
            std::cout << "no more options" << std::endl;
            break;
        }
        if (c == 'v')
            std::cout << "version: " << 1 << std::endl;
    }
    return EXIT_SUCCESS;
}
