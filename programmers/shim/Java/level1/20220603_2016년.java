package Study_2022.programmers.shim.Java.level1;

class Solution {
    public String solution(int a, int b) {
       String W[]={"THU","FRI","SAT","SUN","MON","TUE","WED"};
       int M[]={31,29,31,30,31,30,31,31,30,31,30,31};
        for(int i=0; i<a-1; i++)
            b+=M[i];
        return W[b%7];
    }
}