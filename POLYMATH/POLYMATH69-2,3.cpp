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
#define A -10
#define B 5

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
    ll a = 0, b = 0;
    while (epoch--) {
        int tur = 0;
        while (tur != A && tur != B) {
            int res = dis(gen);
            if (res == 0) { tur--; continue;}
            tur++;
        }
        if (tur == A) a++;
        if (tur == B) b++;
    }
    cout << "Possibility to arrive A: " << (long double)(a)/(long double)(a+b)*100 << "%\n";
    cout << "Possibility to arrive B: " << (long double)(b)/(long double)(a+b)*100 << "%\n";
}