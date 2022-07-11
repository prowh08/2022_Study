package Study_2022.programmers.shim.Java.level1;

import java.util.*;

public class 정수_내림차순으로_배치하기_20220707 {
    public long solution(long n) {
        long answer = 0;
        String st[]=Long.toString(n).split("");
        Arrays.sort(st);
        for(int i=0; i<st.length; i++)
            answer+=Integer.parseInt(st[i])*Math.pow(10,i);
        return answer;
    }
    /*public long solution(long n) {
        String answer ="";
        String st[]=Long.toString(n).split("");
        Arrays.sort(st);
        for(int i=st.length-1; i>=0; i--)
            answer+=st[i];
        return Long.parseLong(answer);
    } */
}