#include "practical5.h"

int main()
{
    map<int, vector<pair<int, int> >> adj_list;
    adj_list[1] = {{5, 2}};
    adj_list[2] = {{2, 3}}; // 1 -> 2 -> 3 -> 4 -> 5
    adj_list[3] = {{4, 4}};
    adj_list[4] = {{1, 5}};
    int init = 1, goal = 5;

    vertex_t *path = djikstra(adj_list, init, goal);
    while(path) {
        cout << path->v << " ";
        path = path->p;
    }
    cout << endl;
    return 0;
}
