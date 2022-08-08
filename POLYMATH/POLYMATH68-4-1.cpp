#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <cmath>
#include <functional>
#include <utility>
#include <stack>
#include <queue>
#include <deque>
#include <cstring>
#include <thread>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> P;

ll N = 9, color = 10, res = 0;

P edge[9] = {
    {0,7},{0,5},
    {1,5},{1,3},
    {2,7},{2,6},
    {3,8},{4,8},{4,6}
};

ll solve(ll l, vector<ll> a) {
    if (l == N) {
        for (ll i = 0; i < 9; i++)
            if (a[edge[i].first] == a[edge[i].second]) return 0;
        if (a[N-1] == a[0]) return 0;
        // cout << "*";
        // for (ll i = 0; i < 9; i++)
        //     cout << a[i] << " ";
        // cout << "\n";
        res++;
        return 1;
    }

    ll ret = 0;
    a.push_back(0);
    for (ll i = 0; i < color; i++) {
        // if (l == 0) cout << i << "\n";
        if (l != 0 && a[l-1] == i) continue;
        a[l] = i;
        ret += solve(l+1, a);
        if (l==2) cout << ret << "\n";
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> color;
    cout << solve(2, {0, 1}) * color * (color-1);
}