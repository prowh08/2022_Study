package Study_2022.baekjoon.shim.Java.단계별로_풀어보기.정수론_및_조합론;

// import java.io.*;
// import java.util.*;

// public class n_2981 {
//     public static int gcd(int n, int m){
//         if(m==0)
//             return n;
//         else
//             return gcd(m,n%m);
//     }
//     public static void main(String[] args)throws IOException{
//         BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
//         int T=Integer.parseInt(br.readLine());
//         int arr[]=new int[T];
//         for(int i=0; i<T; i++)
//             arr[i]=Integer.parseInt(br.readLine());
//         Arrays.sort(arr);
//         int gcdn=arr[1]-arr[0];
//         for(int i=2; i<T; i++)
//             gcdn=gcd(gcdn,arr[i]-arr[i-1]);
//         for(int i=2; i<=gcdn; i++){
//             if(gcdn%i==0)
//                 System.out.print(i+" ");
//         }
//     }
// }

//리벤지전

import java.io.*;
import java.util.*;

public class n_2981 {
    public static int gcd(int n, int m){
        if(m==0)
            return n;
        else 
            return gcd(m,n%m);
    }
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        int n=Integer.parseInt(br.readLine()), arr[]=new int[n];
        for(int i=0; i<n; i++)
            arr[i]=Integer.parseInt(br.readLine());
        Arrays.sort(arr);
        int num=arr[1]-arr[0];
        for(int i=1; i<n; i++)
            num=gcd(num,arr[i]-arr[i-1]);
        for(int i=2; i<=num; i++)
            if(num%i==0)
                bw.write(i+" ");
        bw.flush();bw.close();
    }
}