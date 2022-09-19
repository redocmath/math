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
#include <map>
#include <random>

using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    ll n, epoch; cin >> n >> epoch;
    for (ll i = 1; i <= n; i++) {
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<int> dis(0, i-1);
        vector<bool> wasfilled(i);
        for (ll j = 1; j <= epoch; j++) {
            ll res = dis(gen);
        }
    }
}