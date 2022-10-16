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
#define A 1

using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    ll epoch; cin >> epoch;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(0, 2);
    ll a = 0, b = epoch;
    while (epoch--) {
        int tur = 0; ll cnt = 0;
        while (tur != A) {
            int res = dis(gen);
            if (res == 0) { tur--; cnt++; continue;}
            tur++;
            cnt++;
        }
        if (tur == A) a += cnt;
    }
    cout << "Average of jump number to arrive " << A << ": " << (long double)(a) / (long double)(b) << "\n";
}