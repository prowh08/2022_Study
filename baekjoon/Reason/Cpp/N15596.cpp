#include <vector>
using namespace std;

long long sum(std::vector<int> &a) {
	long long ans = 0;
    vector<int>::iterator cur = a.begin();
    for(;cur != a.end(); cur++)
        ans += *cur;
	return ans;
}