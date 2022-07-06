package Study_2022.programmers.shim.Java.level1;

public class 자연수_뒤집어_배열로_만들기_20220705 {
    public int[] solution(long n) {
        String[] str=Long.toString(n).split("");
        int[] answer = new int[str.length];
        for(int i=str.length-1; i>=0; i--)
            answer[i]=Integer.parseInt(str[str.length-i-1]);
        return answer;
    }
}
