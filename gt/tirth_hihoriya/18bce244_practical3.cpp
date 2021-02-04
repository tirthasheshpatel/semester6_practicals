// Name: Tirth Hihoriya
// Roll no.: 18bce244
// Prac-3 : Havel Hakimi Theorem

#include <bits/stdc++.h>
using namespace std;

bool havel_hakimi(vector<int> ds)
{
    while(true)
    {
        sort(ds.begin(), ds.end(), greater<>());

        if (ds[0] == 0)
            return true;

        int first = ds[0];
        ds.erase(ds.begin());
 
        if (first > ds.size())
            return false;
 
        for (int i = 0; i < first; i++)
        {
            ds[i]--;

            if (ds[i] < 0)
                return false;
        }

        // for(int i=0; i<ds.size(); i++)   // Just to see the sequence in-between
        // {
        //     cout << ds[i] << ",";
        // }
        // cout << '\n';
    }

}

int main()
{

    int n;
    cout << "\nEnter the number of vertices in graph : ";
    cin >> n;
    vector<int> ds(n);
    cout << "Enter degree sequence : ";
    for(int i=0; i<n; i++)
        cin >> ds[i];

    if(havel_hakimi(ds))
        cout << "\n-->> Graph exists.\n\n";
    else
        cout << "\n-->> Graph do not exists.\n\n";

}