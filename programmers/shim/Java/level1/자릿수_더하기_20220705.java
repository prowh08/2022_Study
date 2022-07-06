package Study_2022.programmers.shim.Java.level1;

public class 자릿수_더하기_20220705 {
    public int solution(int n) {
        int answer = 0;
        String str[]=Integer.toString(n).split("");
        for(int i=0; i<str.length; i++)
            answer+=Integer.parseInt(str[i]);
        return answer;
    }
}
