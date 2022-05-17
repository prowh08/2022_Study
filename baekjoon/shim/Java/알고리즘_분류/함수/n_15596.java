package Study_2022.baekjoon.shim.Java.알고리즘_분류.함수;

public class n_15596 {
    long sum(int[] a) {
        long ans = 0;
        for(int i=0; i<a.length; i++)
            ans+=a[i];
        return ans;
    }
}
