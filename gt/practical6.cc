#include "practical6.h"

int main()
{
    /* 

            10 
    (0)------->(3) 
        |     /|\ 
    5 |     | 
        |     | 1 
    \|/     | 
    (1)------->(2) 
            3

    */
    vector<vector<int> > graph =
                      {
                        {0  , 5  , INF, 10}, 
                        {INF, 0  , 3  , INF}, 
                        {INF, INF, 0  , 1}, 
                        {INF, INF, INF, 0} 
                      };
 
    // Print the solution
    floyd_warshall(graph, 4);
    return 0; 
}