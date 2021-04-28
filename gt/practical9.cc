#include <bits/stdc++.h>
using namespace std;

const int MAX = 100;

int store[MAX], n;

int graph[MAX][MAX];
  
bool is_clique(int b)
{

    for (int i = 1; i < b; i++)
        for (int j = i + 1; j < b; j++)
            if (graph[store[i]][store[j]] == 0)
                return false;
    return true;
}

int max_cliques(int i, int l)
{
    int max_length = 0;
  
    for (int j = i + 1; j <= n; j++) {
  
        store[l] = j;
  
        if (is_clique(l + 1)) {
  
            max_length = max(max_length, l);
  
            max_length = max(max_length, max_cliques(j, l + 1));
        }
    }
    return max_length;
}


int main()
{
    /*     TESTING ON A GRAPH
    
            1 ----------- 2
            |           / |
            |        /    |
            |     /       |
            |  /          |
            3 ----------- 4
    
    */
    int edges[][2] = { { 1, 2 }, { 2, 3 }, { 3, 1 }, 
                       { 4, 3 }, { 4, 2 }, { 4, 1 } };
    int size = sizeof(edges) / sizeof(edges[0]);
    n = 4;

    for (int i = 0; i < size; i++) {
        graph[edges[i][0]][edges[i][1]] = 1;
        graph[edges[i][1]][edges[i][0]] = 1;
    }

    cout << max_cliques(0, 1) << endl;

    return 0;
}
