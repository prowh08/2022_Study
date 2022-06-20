package Study_2022.programmers.shim.Java.level1;

import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String str[]=s.split("");
        Arrays.sort(str);
        for(int i=str.length-1; i>=0; i--)
            answer+=str[i];
        return answer;
    }
}