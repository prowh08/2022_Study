package Study_2022.programmers.shim.Java.level1;

class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        for(int i=0; i<absolutes.length; i++)
            answer+=absolutes[i]*(signs[i]==true?1:-1);
        return answer;
    }
}