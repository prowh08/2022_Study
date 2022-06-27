package Study_2022.programmers.shim.Java.level1;

public class 수박수박수박수박수박수_20220627 {
    public String solution(int n) {
        String answer = "";
        for(int i=0; i<n; i++)
            answer+=i%2==0?"수":"박";
        return answer;
    }
}
