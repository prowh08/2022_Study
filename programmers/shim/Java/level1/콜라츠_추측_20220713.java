package Study_2022.programmers.shim.Java.level1;

public class 콜라츠_추측_20220713 {
    public int solution(long num) {
        int answer = 0;
        while(num!=1){
            num=(num%2==0? num/2: num*3+1);
            if(answer==500)
                break;
            answer++;
        }
        return (answer==500? -1: answer);
    }
}
