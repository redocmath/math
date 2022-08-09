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

ll N = 13, color;

ll solve( ll l, vector<ll> a) {
    if (l == N) {
        for (ll i = 0; i < N; i++) {
            if (a[i] == a[(i+3)%N]) return 0;
            if (a[i] == a[(i+4)%N]) return 0;
        }
        if (a[N-1] == a[0]) return 0;
        // cout << "*";
        // for (ll i = 0; i < 13; i++)
        //     cout << a[i] << " ";
        // cout << "\n";
        return 1;
    }

    ll ret = 0;
    a.push_back(0);
    // test
    for (ll i = 0; i < color; i++) {
        if (l==3) cout << a[l-1] << ": " << i;
        if (l != 0 && a[l-1] == i) continue;
        a[l] = i;

        ret += solve(l+1, a);
        if (l==3) cout << ": " << ret << "\n";
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    
    cin >> color;
    // cout << solve(3,{0,1,0}) << "\n";
    cout << (solve(3, {0,1,2})*(color-2)+solve(3,{0,1,0})) * color * (color-1) << "\n";
}