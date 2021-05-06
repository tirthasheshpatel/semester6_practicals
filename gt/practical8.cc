#include <iostream>

using namespace std;

int main()
{
    int v, e;
    cout << "Enter no. of vertices in a graph: ";
    cin >> v;
    cout << "Enter no. of edges in a graph: ";
    cin >> e;

    if ( v%2 == 0 && e >= v*v/4 ) {
        // graph is complete bi-partite
        if ( e <= 2*v-4 ) {
            cout << "Graph is planar" << endl;
        }
        else {
            cout << "Graph is not planar" << endl;
        }
    }
    if ( e <= 3*v-6 ) {
        cout << "Graph is planar" << endl;
    }
    else {
        cout << "Graph is not planar" << endl;
    }

    return 0;
}

