package Study_2022.programmers.shim.Java.level1;

public class 약수의_합_20220629 {
    public int solution(int n) {
        int answer = 0;
        for(int i=1; i<=Math.sqrt(n); i++){
            if(n%i==0)
                answer+=i+(i*i==n? 0:n/i);
        }
        return answer;
    }
}
