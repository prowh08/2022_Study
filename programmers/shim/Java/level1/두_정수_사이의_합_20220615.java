package Study_2022.programmers.shim.Java.level1;

class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        for(int i=Math.min(a,b); i<=Math.max(a,b); i++)
            answer+=i;
        return answer;
    }
}