package Study_2022.programmers.shim.Java.level1;

public class 정수_제곱근_판별_20220707 {
    public long solution(long n) {
        long answer = 0;
        long sqrt=(long)Math.sqrt(n);
        answer=(long)Math.pow(sqrt,2)==n? (long)Math.pow(sqrt+1,2):-1;
        return answer;
    }
}
