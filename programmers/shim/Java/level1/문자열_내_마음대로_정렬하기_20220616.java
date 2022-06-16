package Study_2022.programmers.shim.Java.level1;

import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        for(int i=0; i<strings.length; i++)
            answer[i]=strings[i].charAt(n)+strings[i];
        Arrays.sort(answer);
        for(int i=0; i<strings.length; i++)
            answer[i]=answer[i].substring(1);
        return answer;
    }
}
