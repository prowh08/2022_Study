package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.함수;

public class n_15596 {
    long sum(int[] a) {
        long ans = 0;
        for(int i=0; i<a.length; i++)
            ans+=a[i];
        return ans;
    }
}
