package Study_2022.programmers.shim.Java.level1;

class Solution {
    public int solution(int n) {
        String st="";
        while(n>0){
            st+=n%3;
            n/=3;
        }
        int answer=Integer.parseInt(st,3);
        return answer;
    }
}