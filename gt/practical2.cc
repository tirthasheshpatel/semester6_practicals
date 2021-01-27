#include <iostream>
#include "practical2.h"

int main()
{
    /*

    G1 -->  p --- r
            |     |
            |     |
            q --- s --- t

    G2 -->  a --- c
            |     |
            |     |
            d --- e --- b

    Given Graphs are Isomorphic with similar vertices:

    p --- a
    r --- c  OR  r --- d
    q --- d  OR  q --- c
    s --- e
    t --- b

    */

    std::set<char> V1 = {'p', 'q', 'r', 's', 't'};
    std::set<std::pair<char, char> > E1 = {{'p', 'q'},
                                           {'p', 'r'},
                                           {'r', 's'},
                                           {'q', 's'},
                                           {'s', 't'}};
    auto G1 = UndirectedGraph<char>(V1, E1);

    std::set<char> V2 = {'a', 'b', 'c', 'd', 'e'};
    std::set<std::pair<char, char> > E2 = {{'a', 'c'},
                                           {'a', 'd'},
                                           {'c', 'e'},
                                           {'d', 'e'},
                                           {'e', 'b'}};
    auto G2 = UndirectedGraph<char>(V2, E2);

    // std::set<int> V1 = {1, 2, 3, 4};
    // std::set<std::pair<int, int> > E1 = {{1, 2},
    //                                      {2, 3},
    //                                      {3, 4},
    //                                      {4, 1}};   /* Square Graph */
    // auto G1 = UndirectedGraph<int>(V1, E1);

    // std::set<int> V2 = {1, 2, 3, 4};
    // std::set<std::pair<int, int> > E2 = {{1, 3},
    //                                      {2, 4}};   /* Diagonal Graph */
    // auto G2 = UndirectedGraph<int>(V2, E2);

    auto result = G1.check_isomorphism(G2);

    if ( result.empty() ) {
        std::cout << "Given graphs are not isomorphic!!" << std::endl;
    }
    else {
        std::cout << "Given graphs are isomorphic!" << std::endl;
        std::cout << "Similar Vertices\n----------------" << std::endl;
        for ( const auto &verts : result ) {
            std::cout << "{" << verts.first << ", " << verts.second << "}" << std::endl;
        }
    }

    return 0;
}
