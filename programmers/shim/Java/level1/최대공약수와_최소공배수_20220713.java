package Study_2022.programmers.shim.Java.level1;

public class 최대공약수와_최소공배수_20220713 {
    public int gcd(int n, int m){
        if(m==0)
            return n;
        else
            return gcd(m,n%m);
    }
    public int[] solution(int n, int m) {
        int[] answer = {gcd(n,m),n/gcd(n,m)*m};
        return answer;
    }
}
