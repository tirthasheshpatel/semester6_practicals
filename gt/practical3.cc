#include <iostream>
#include "practical3.h"

int main()
{
    std::vector<std::vector<int> > degrees = {
                                              {1, 1, 1, 1, 1},            // 1.  does NOT
                                              {1, 1, 1, 1, 1, 1},         // 2.  does
                                              {1, 1},                     // 3.  does
                                              {1, 1, 1},                  // 4.  does NOT
                                              {-1, -1, -1},               // 5.  does NOT
                                              {0, 0, 0, 0, 0},            // 6.  does
                                              {0, 0, 0, 0, 0, 0},         // 7.  does
                                              {1, 1, 2, 2, 5, 5, 6},      // 8.  does NOT
                                              {3, 3, 3, 3},               // 9.  does
                                              {},                         // 10. does
                                              {0},                        // 11. does
                                              {1},                        // 12. does NOT
                                              {-1, 1, 1, 1, 3},           // 13. does NOT
                                              {1, 1, 1, 3, 2, 2, 2, 2}    // 14. does
                                             };

    for ( size_t i=0 ; i<degrees.size() ; i++ )
        std::cout << i+1 \
                  << ". The given sequence " \
                  << (havel_hakimi(degrees[i]) ? "does" : "does NOT") \
                  << " constitute a graph!" << std::endl;

    return 0;
}
