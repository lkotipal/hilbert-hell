#include "hsfc_hilbert_const.h"
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>

int main(int argc, char* argv[])
{
    int max {0};
    if (argc > 1) {
        max = 1 << 3*atoi(argv[1]);
        std::clog << max << std::endl;
    }

    std::cout << std::setprecision (std::numeric_limits<double>::max_digits10);
    //std::cout << std::hexfloat;
    for (int i = 0; i < max; ++i) {
        double x {static_cast<double>(i) / (max - 1)};
        std::array<double, 3> xyz {};
        Zoltan_HSFC_Hilbert3d(xyz.data(), x);
        std::cout << x << "\t" << xyz[0] << "\t" << xyz[1] << "\t" << xyz[2] << "\t" << Zoltan_HSFC_InvHilbert3d(xyz.data()) << "\n";
    }

    return 0;
}