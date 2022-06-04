package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.브루트포스;

import java.util.*;

public class n_2798 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), s=sc.nextInt(), arr[]=new int[n], result=0;
        for(int i=0; i<n; i++)
            arr[i]=sc.nextInt();
        for(int i=0; i<n-2; i++){
            for(int j=i+1; j<n-1; j++){
                for(int k=j+1; k<n; k++){
                    int sum=arr[i]+arr[j]+arr[k];
                    if(sum<=s&&sum>result)
                        result=sum;
                }
            }
        }
        System.out.println(result);
    }
}
