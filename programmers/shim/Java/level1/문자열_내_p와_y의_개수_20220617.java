package Study_2022.programmers.shim.Java.level1;

class Solution {
    boolean solution(String s) {
        int cnt=0;
        s=s.toLowerCase();
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='p') cnt++;
            if(s.charAt(i)=='y') cnt--;
        }
        return cnt==0? true:false;
    }
}