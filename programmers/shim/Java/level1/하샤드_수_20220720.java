package Study_2022.programmers.shim.Java.level1;

public class 하샤드_수_20220720 {
    public boolean solution(int x) {
        String s[]=Integer.toString(x).split("");
        int sum=0;
        for(int i=0; i<s.length; i++)
            sum+=Integer.parseInt(s[i]);
        return x%sum==0? true:false;
    }
}
