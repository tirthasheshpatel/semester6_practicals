#ifndef GTLAB_PRACTICAL3
#define GTLAB_PRACTICAL3

#include <algorithm>
#include <vector>

static bool __all_zeros(const std::vector<int> &degrees, const int &i, const int &j)
{
    for ( int k=i ; k<=j ; k++ ) if ( degrees[k] != 0 ) return false;
    return true;
}

bool havel_hakimi(const std::vector<int> &degrees)
{
    if ( degrees.size() == 0 ) return true;
    for ( size_t k=0 ; k<degrees.size() ; k++ ) if ( degrees[k] < 0 ) return false;

    std::vector<int> degcopy = degrees;                  // [1, 1, 2, 2, 5, 5, 6]

    if ( !std::is_sorted(degcopy.begin(), degcopy.end()) ) {
        std::sort(degcopy.begin(), degcopy.end());
    }
    int i = degcopy.size() - 1;                          // 6
    int last = degcopy[i];                               // 6
    do {
        if ( i-last < 0 ) return false;                  // 0
        for ( int j=i-1 ; j>=i-last ; j-- ) {            // j=5 ; j>=0 ; j--
            if ( degcopy[j] <= 0 ) return false;         // skipped...
            degcopy[j]--;                                // [0, 0, 1, 1, 4, 4]
        }
        i--;                                             // 5
        std::sort(degcopy.begin(), degcopy.begin()+i+1); // 0, 6 ==> [0, 0, 1, 1, 4, 4, (6)]
        last = degcopy[i];                               // 4
    } while ( !__all_zeros(degcopy, 0, i) );             // 0, 5 ==> false
    return true;
}

#endif // GTLAB_PRACTICAL3
