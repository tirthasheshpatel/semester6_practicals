#include <iostream>
#include "practical1.h"

int main()
{
    std::set<int> V1 = {1, 2, 3, 4};
    std::set<std::pair<int, int> > E1 = {{1, 2}, {2, 3}, {3, 4}, {4, 1}};
    auto G1 = Graph(V1, E1);
    std::set<int> V2 = {1, 2, 3, 4};
    std::set<std::pair<int, int> > E2 = {{1, 3}, {2, 4}};
    auto G2 = Graph(V2, E2);

    auto G3 = G1.graph_union(G2);
    auto G4 = G1.graph_intersection(G2);
    auto G5 = G1.graph_ringsum(G2);

    std::cout << "G1:\n";
    std::cout << G1 << std::endl;
    std::cout << "G2:\n";
    std::cout << G2 << std::endl;
    std::cout << "\nUnion of the G1 and G2 is : " << std::endl;
    std::cout << "G3:\n";
    std::cout << G3 << std::endl;
    std::cout << "\nIntersection of the G1 and G2 is : " << std::endl;
    std::cout << "G4:\n";
    std::cout << G4 << std::endl;
    std::cout << "\nRing Sum of the G1 and G2 is : " << std::endl;
    std::cout << "G5:\n";
    std::cout << G5 << std::endl;

    return 0;
}
