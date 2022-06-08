#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 45;
    vector<int>::iterator cur = numbers.begin();
    for(;cur != numbers.end(); cur++)
        answer -= *cur;
    return answer;
}